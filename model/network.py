import config
from keras.models import Model
from keras.layers import Input, Lambda
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.resnet50 import ResNet50

from model.utils import create_txt_encoder
from model.utils import create_img_encoder
from model.utils import euclidean_distance
from model.utils import eucl_dist_output_shape


if config.IMAGE_ENCODER == 'vgg':
    img_encoder = VGG19()
elif config.IMAGE_ENCODER == 'resnet':
    img_encoder = ResNet50(include_top=True, weights='imagenet')
else:
    raise ValueError(
        f'Unrecognized IMAGE_ENCODER value: {config.IMAGE_ENCODER}')

# Disable ImageEncoder training
for layer in img_encoder.layers:
    layer.trainable = False

# create network structures
input_txt = Input(shape=(config.SENTENCE_EMBEDDING_LENGTH,))
input_img = Input(shape=(224, 224, 3))

encoded_txt = create_txt_encoder()(input_txt)
encoded_img = create_img_encoder(img_encoder)(input_img)

distance = Lambda(euclidean_distance,
                  output_shape=eucl_dist_output_shape)([encoded_txt, encoded_img])

model = Model(inputs=[input_txt, input_img], outputs=distance)
