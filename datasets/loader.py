import math
import glob
import numpy as np
from PIL import Image
from random import randint
from tensorflow.keras.utils import Sequence
from tensorflow.keras.applications.resnet import preprocess_input


class DatasetSequence(Sequence):
    def __init__(self, dataset, batch_size=32):
        self.dataset = dataset
        self.batch_size = batch_size

        if dataset == 'train':
            self.offset = 0
        elif dataset == 'valid':
            self.offset = 5000
        elif dataset == 'test':
            self.offset = 6000

        self.pd_img = {}
        self.pd_txt = {}

    def __len__(self):
        f = glob.glob(f'./datasets/{self.dataset}/*/embedding.npy')
        return math.ceil(len(f) / self.batch_size)

    def __getitem__(self, index):
        batch_img = np.zeros((self.batch_size, 224, 224, 3))
        batch_txt = np.zeros((self.batch_size, 500))
        batch_labels = np.zeros((self.batch_size, 1))

        ti = self.offset + index

        for i in range(self.batch_size // 2):

            # correct
            img = self.read_image(self.dataset, ti)
            txt = self.read_text_embedding(self.dataset, ti)

            batch_img[i] = img
            batch_txt[i] = txt
            batch_labels[i] = 1

            j = self.batch_size - 1 - i

            # incorrect
            ii = ti
            while ii == ti:
                ii = self.offset + randint(0, self.__len__())

            img = self.read_image(self.dataset, ii)

            batch_img[j] = img
            batch_txt[j] = txt
            batch_labels[j] = 0

        return [batch_txt, batch_img], batch_labels

    def read_image(self, dataset, idx):
        if idx in self.pd_img:
            return self.pd_img[idx]

        img = Image.open(f'./datasets/{dataset}/{idx}/image.jpg')

        side = min(img.width, img.height)

        left = (img.width - side) / 2
        top = (img.height - side) / 2
        right = (img.width + side) / 2
        bottom = (img.height + side) / 2

        img = img.crop((left, top, right, bottom))
        img = img.resize((224, 224))
        img = np.asarray(img)
        img = np.expand_dims(img, axis=0)
        img = preprocess_input(img)

        self.pd_img[idx] = img

        return img

    def read_text_embedding(self, dataset, idx):
        if idx in self.pd_txt:
            return self.pd_txt[idx]

        embedding_data = np.load(f'./datasets/{dataset}/{idx}/embedding.npy')
        if embedding_data.shape[0] < 5:
            padding = np.zeros(((5 - embedding_data.shape[0]), 100))
            embedding_data = np.concatenate((embedding_data, padding), axis=0)
        else:
            embedding_data = embedding_data[:5, :]

        embedding_data = embedding_data.reshape(-1)
        self.pd_txt[idx] = embedding_data

        return embedding_data
