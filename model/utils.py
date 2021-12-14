import config
from keras.layers.core import Dropout
from keras.layers import Dense
from keras import backend as K
from keras.models import Sequential

def euclidean_distance(vects):
    x, y = vects
    return K.sqrt(K.maximum(K.sum(K.square(x - y), axis=1, keepdims=True), K.epsilon()))


def eucl_dist_output_shape(shapes):
    shape1, shape2 = shapes
    return (shape1[0], 1)


def contrastive_loss(y_true, y_pred):
    margin = 1
    return K.mean(y_true * K.square(y_pred) + (1 - y_true) * K.square(K.maximum(margin - y_pred, 0)))


def create_img_encoder(resnet):
    x = Sequential()
    x.add(resnet)
    x.add(Dense(500, activation="relu"))
    # x.add(Dropout(0.5))
    x.add(Dense(512, activation="relu"))
    return x


def create_txt_encoder():
    x = Sequential()
    x.add(Dense(500, input_shape=(config.SENTENCE_EMBEDDING_LENGTH,), activation="relu"))
    # x.add(Dropout(0.5))
    x.add(Dense(512, activation="relu"))
    return x


def compute_accuracy(predictions, labels):
    return labels[predictions.ravel() < 0.5].mean()
