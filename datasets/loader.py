import math
import glob
import numpy as np
from PIL import Image
from random import randint
from tensorflow.keras.utils import Sequence
from tensorflow.keras.applications.resnet50 import preprocess_input


class DatasetSequence(Sequence):
    def __init__(self, dataset, batch_size=32):
        self.dataset = dataset
        self.batch_size = batch_size

        if dataset == 'train':
            self.offset = 0
        elif dataset == 'valid':
            self.offset = 10000
        elif dataset == 'test':
            self.offset = 11000

        self.pd_img = {}
        self.pd_txt = {}

    def __len__(self):
        f = glob.glob(f'./datasets/{self.dataset}/*/embedding.npy')
        return math.ceil(len(f) / self.batch_size)

    def __getitem__(self, index):
        batch_img = np.zeros((self.batch_size, 224, 224, 3))
        batch_txt = np.zeros((self.batch_size, 500))
        batch_labels = np.zeros((self.batch_size, 1))

        ti = self.offset + index * self.batch_size

        for i in range(self.batch_size // 2):

            ii = ti + i

            # correct
            img = self.read_image(ii)
            txt = self.read_text_embedding(ii)

            batch_img[i] = img
            batch_txt[i] = txt
            batch_labels[i] = 1

            j = self.batch_size - 1 - i

            # incorrect
            ji = ii
            while ji == ti:
                ji = self.offset + randint(0, self.__len__() * self.batch_size - 1)

            img = self.read_image(ji)

            batch_img[j] = img
            batch_txt[j] = txt
            batch_labels[j] = 0

        return [batch_txt, batch_img], batch_labels

    def read_image(self, idx):
        if idx in self.pd_img:
            return self.pd_img[idx]

        img = Image.open(f'./datasets/{self.dataset}/{idx}/image.jpg')

        side = min(img.width, img.height)

        left = (img.width - side) / 2
        top = (img.height - side) / 2
        right = (img.width + side) / 2
        bottom = (img.height + side) / 2

        img = img.crop((left, top, right, bottom))
        img = img.resize((224, 224))
        img = np.asarray(img)

        if len(img.shape) == 2:
            img = np.stack([img, img, img], axis=-1)

        # img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)

        self.pd_img[idx] = img

        return img

    def read_text_embedding(self, idx):
        if idx in self.pd_txt:
            return self.pd_txt[idx]

        embedding_data = np.load(f'./datasets/{self.dataset}/{idx}/embedding_50.npy')
        truncate_length = 10

        if embedding_data.shape[0] < truncate_length:
            padding = np.zeros(((truncate_length - embedding_data.shape[0]), embedding_data.shape[1]))
            embedding_data = np.concatenate((embedding_data, padding), axis=0)
        else:
            embedding_data = embedding_data[:truncate_length, :]

        embedding_data = embedding_data.reshape(-1)

        self.pd_txt[idx] = embedding_data

        return embedding_data
