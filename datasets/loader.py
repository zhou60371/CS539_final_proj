import glob
import imageio
import numpy as np
from PIL import Image
from random import randint


def loader(dataset, batch_size):
    f = glob.glob(f'./datasets/{dataset}/*/embedding.npy')

    batch_img = np.zeros((batch_size, 224, 224, 3))
    batch_txt = np.zeros((batch_size, 512))
    batch_labels = np.zeros((batch_size, 1))

    length = len(f)

    while True:
        for i in range(batch_size // 2):

            i = i * 2

            # correct
            sample = randint(0, length)
            file = video_ids.iloc[sample]

            correct_txt = video_txt.iloc[sample]

            im = load_img(file, target_size=(224, 224))
            im = img_to_array(im)
            im = np.expand_dims(im, axis=0)
            im = preprocess_input(im)

            batch_img[i-2] = im
            batch_txt[i-2] = correct_txt
            batch_labels[i-2] = 1

            # incorrect
            file = video_ids.iloc[randint(0, length)]

            im = load_img(file, target_size=(224, 224))
            im = img_to_array(im)
            im = np.expand_dims(im, axis=0)
            im = preprocess_input(im)

            batch_img[i-1] = im
            batch_txt[i-1] = correct_txt
            batch_labels[i-1] = 0

        yield [batch_txt, batch_img], batch_labels
