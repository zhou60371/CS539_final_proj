import torch
import transformers
from transformers import BertModel, BertTokenizer

class text_processing():
    def __init__(self, text):
        self.model = BertModel.from_pretrained("bert-base-uncase")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncase")
        self.text = text

    # Apply Bert to obtain embedding
    # pending for pad, mask usage
    def text_encoder(self, text):
        ids = torch.tensor([self.tokenizer(text, add_special_tokens=True)])
        embedding = self.model(ids)
        return embedding

    def grab_position(self, text, entity):
        pass

