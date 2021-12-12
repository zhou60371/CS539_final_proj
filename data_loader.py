import numpy as np
import json
import os
import requests

root = "./datasets"
data_info_file = "captions_train2014.json"

class data_loader():
    def __init__(self, root, data_info_file):
        self.root = root
        with open(os.path.join(root, data_info_file), "r") as f:
            self.data_info = json.load(f)
        self.length = 8000

    def get_imgName(self, index):
        return self.data_info["images"][index]["file_name"]

    def get_imgId(self, index):
        return self.data_info["images"][index]["id"]

    def get_caption(self, imgId):
        caption_list = []
        for caption in self.data_info["annotations"]:
            if caption["image_id"]==imgId:
                caption_list.append(caption["caption"])

        return caption_list

    def get_img(self, index):
        img_url = self.data_info["images"][index]["coco_url"]
        img = requests.get(img_url)
        return img

    def dump_data(self):
        for index in range(self.length):
            imgName = self.get_imgName(index)
            imgId = self.get_imgId(index)
            img = self.get_img(index)
            caption = self.get_caption(imgId)
            if os.path.exists(os.path.join(self.root, str(imgId))):
                pass
            else:
                os.mkdir(os.path.join(self.root, str(imgId)))
                with open(os.path.join(self.root, str(imgId), imgName), "wb") as f:
                    f.write(img.content)
                with open(os.path.join(self.root, str(imgId), "annotations.txt"), "w") as f:
                    for sentence in caption:
                        f.write(sentence)
                        f.write("\n")

if __name__=="__main__":
    data_loader = data_loader(root, data_info_file)
    data_loader.dump_data()
