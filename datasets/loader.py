import math
import glob
import numpy as np
from PIL import Image
from random import randint
from tensorflow.keras.utils import Sequence
from tensorflow.keras.applications.resnet import preprocess_input


def read_text_embedding(dataset, idx):
    embedding_data = np.load(f'./datasets/{dataset}/{idx}/embedding.npy')
    if embedding_data.shape[0] < 5:
        padding = np.zeros(((5 - embedding_data.shape[0]), 100))
        embedding_data = np.concatenate((embedding_data, padding), axis=0)
    else:
        embedding_data = embedding_data[:5, :]

    embedding_data = embedding_data.reshape(-1)

    return embedding_data


def read_image(dataset, idx):
    img = Image.open(f'./datasets/{dataset}/{idx}/image.jpg')

    side = min(img.width, img.height)

    left = (img.width - side) / 2
    top = (img.height - side) / 2
    right = (img.width + side) / 2
    bottom = (img.height + side) / 2

    img = img.crop((left, top, right, bottom))
    img = img.resize((224, 224))

    return np.asarray(img)


class DatasetSequence(Sequence):
    def __init__(self, dataset, batch_size=32):
        self.dataset = dataset
        self.batch_size = batch_size

    def __len__(self):
        f = glob.glob(f'./datasets/{self.dataset}/*/embedding.npy')
        return math.ceil(len(f) / self.batch_size)

    def __getitem__(self, index):
        batch_img = np.zeros((self.batch_size, 224, 224, 3))
        batch_txt = np.zeros((self.batch_size, 500))
        batch_labels = np.zeros((self.batch_size, 1))

        for i in range(self.batch_size // 2):

            i = i * 2

            # correct
            im = read_image(self.dataset, index)
            im = np.expand_dims(im, axis=0)
            im = preprocess_input(im)

            correct_txt = read_text_embedding(self.dataset, index)

            batch_img[i - 2] = im
            batch_txt[i - 2] = correct_txt
            batch_labels[i - 2] = 1

            # incorrect
            ii = index
            while ii == index:
                ii = randint(0, self.__len__())

            im = read_image(self.dataset, index)
            im = np.expand_dims(im, axis=0)
            im = preprocess_input(im)

            batch_img[i - 1] = im
            batch_txt[i - 1] = correct_txt
            batch_labels[i - 1] = 0

        return [batch_txt, batch_img], batch_labels


def loader(dataset, batch_size):
    f = glob.glob(f'./datasets/{dataset}/*/embedding.npy')

    batch_img = np.zeros((batch_size, 224, 224, 3))
    batch_txt = np.zeros((batch_size, 500))
    batch_labels = np.zeros((batch_size, 1))

    length = len(f)

    while True:
        for i in range(batch_size // 2):

            i = i * 2

            # correct
            im = read_image(dataset, i)
            im = np.expand_dims(im, axis=0)
            im = preprocess_input(im)

            correct_txt = read_text_embedding(dataset, i)

            batch_img[i - 2] = im
            batch_txt[i - 2] = correct_txt
            batch_labels[i - 2] = 1

            # incorrect
            ii = i
            while ii == i:
                ii = randint(0, length)
                print(ii, i, ii == i)

            im = read_image(dataset, i)
            im = np.expand_dims(im, axis=0)
            im = preprocess_input(im)

            batch_img[i - 1] = im
            batch_txt[i - 1] = correct_txt
            batch_labels[i - 1] = 0

        yield [batch_txt, batch_img], batch_labels
