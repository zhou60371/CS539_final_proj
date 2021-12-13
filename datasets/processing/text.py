import torch
from transformers import BertModel, BertTokenizer

class TextEmbedder():
    def __init__(self):
        self.model = BertModel.from_pretrained("bert-base-cased")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

    # Apply Bert to obtain embedding
    # pending for pad, mask usage
    def embed(self, text):

        ids = self.tokenizer(text, add_special_tokens=True)
        print(ids)
        embedding = self.model(ids['input_ids'])
        return embedding

