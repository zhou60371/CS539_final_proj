import os
import json
import requests
from tqdm import tqdm


class DataGenerator():
    def __init__(self, f_info):
        with open(f_info, "r") as f:
            self.data_info = json.loads(f.read())

    def get_img_name(self, index):
        return self.data_info["images"][index]["file_name"]

    def get_img_id(self, index):
        return self.data_info["images"][index]["id"]

    def get_captions(self, img_id):
        caption_list = []
        for caption in self.data_info["annotations"]:
            if caption["image_id"] == img_id:
                caption_list.append(caption["caption"])

        return caption_list

    def get_img(self, index):
        img_url = self.data_info["images"][index]["coco_url"]
        img = requests.get(img_url)
        return img

    def generate_data(self, i_samples, dist_path):
        for index in tqdm(i_samples):
            img = self.get_img(index)
            img_id = self.get_img_id(index)
            img_name = self.get_img_name(index)
            img_captions = self.get_captions(img_id)
            img_id = str(img_id)

            # Make dist folder
            p_dist = os.path.join(dist_path, str(index))
            if not os.path.exists(p_dist):
                os.mkdir(p_dist)

            # Assume image is in jpg format, this does not affect modern image loaders
            with open(os.path.join(p_dist, "image.jpg"), "wb") as f:
                f.write(img.content)

            with open(os.path.join(p_dist, "annotations.txt"), "w") as f:
                for sentence in img_captions:
                    f.write(sentence + "\n")

            with open(os.path.join(p_dist, "meta.json"), "w") as f:
                f.write(json.dumps({
                    "index": index,
                    "img_id": img_id,
                    "img_name": img_name,
                    "n_sentences": len(img_captions)
                }))
