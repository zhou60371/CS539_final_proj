from keras.layers import Input, Dense, Lambda, Layer
from keras import backend as K
from keras.models import Model
from tensorflow.keras.applications.resnet50 import ResNet50

from model.utils import create_txt_encoder
from model.utils import create_img_encoder
from model.utils import euclidean_distance
from model.utils import eucl_dist_output_shape

from network.text_processing import text_processing


resnet = ResNet50(include_top=True, weights='imagenet')

for layer in resnet.layers:
    layer.trainable = False

input_txt = Input(shape=(500,))
input_img = Input(shape=(224, 224, 3))

encoded_txt = create_txt_encoder()(input_txt)
# encoded_txt = bert_txt_encoder(input_txt)
encoded_img = create_img_encoder(resnet)(input_img)

<<<<<<< HEAD
# txt_enc = text_processing()
# encoded_txt = txt_enc.text_encoder(input_txt)

encoded_txt = txt_enc(input_txt)
encoded_img = img_enc(input_img)
=======
>>>>>>> 05234b15729f5d34f37936bade87334fdf932d87

distance = Lambda(euclidean_distance,
                  output_shape=eucl_dist_output_shape)([encoded_txt, encoded_img])

model = Model(inputs=[input_txt, input_img], outputs=distance)
