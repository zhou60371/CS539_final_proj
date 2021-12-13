import torch
import transformers
from transformers import BertModel, BertTokenizer
from transformers import pipeline

class text_processing():
    def __init__(self):
        self.model = BertModel.from_pretrained("bert-base-uncased")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")


    # Apply Bert to obtain embedding
    # pending for pad, mask usage
    def text_encoder(self, text):
        ids = self.tokenizer(text, add_special_tokens=True, padding=True, truncation=True, return_tensors="pt")
        embedding = self.model(**ids)
        return embedding

embedding = text_processing().text_encoder(("I love you"))
print(embedding)