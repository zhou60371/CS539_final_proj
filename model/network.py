import imageio
from statistics import median
from random import randint
from glob import glob
import pandas as pd
import numpy as np
from keras.layers.core import Flatten, Dropout
from keras.layers import Input, Dense, Lambda, Layer
from keras import backend as K
from keras import applications
from keras.models import Model
from keras.optimizers import Adam
from tensorflow.keras.applications.resnet import ResNet152


from model.utils import create_txt_encoder
from model.utils import create_img_encoder
from model.utils import euclidean_distance
from model.utils import eucl_dist_output_shape
from model.utils import contrastive_loss


resnet = ResNet152(include_top=True, weights='imagenet')

for layer in resnet.layers:
    layer.trainable = False


input_txt = Input(shape=(512,))
input_img = Input(shape=(224, 224, 3))

txt_enc = create_txt_encoder(input_txt)
img_enc = create_img_encoder(input_img, resnet)

encoded_txt = txt_enc(input_txt)
encoded_img = img_enc(input_img)

distance = Lambda(euclidean_distance, output_shape=eucl_dist_output_shape)(
    [encoded_txt, encoded_img])

model = Model([input_txt, input_img], distance)

adam = Adam(lr=0.00001)
model.compile(loss=contrastive_loss, optimizer=adam)
model.summary()

model.fit_generator(generator(30, df_train),
                    steps_per_epoch=int(int(num_samples * 0.8) / 30),
                    validation_data=generator(30, df_val),
                    validation_steps=int(int(num_samples*0.2)/30),
                    epochs=200, verbose=1)
