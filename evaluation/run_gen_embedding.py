import re
import nltk
import glob
import numpy as np
from tqdm import tqdm
import gensim.downloader
from string import punctuation
from transformers import BertModel, BertTokenizer


class BertEncoder():
    def __init__(self):
        self.model = BertModel.from_pretrained("bert-base-uncased")
        self.tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

    # Apply Bert to obtain embedding
    # pending for pad, mask usage
    def encode(self, text):
        ids = self.tokenizer(text, add_special_tokens=True,
                             padding=True, truncation=True, return_tensors='pt')
        embedding = self.model(**ids)
        embedding = embedding.last_hidden_state
        embedding = embedding.detach().numpy()
        return embedding


nltk.download('punkt')
nltk.download('stopwords')
nltk.download('gutenberg')
nltk.download('averaged_perceptron_tagger')

wpt = nltk.WordPunctTokenizer()
stop_words = nltk.corpus.stopwords.words('english')
remove_terms = punctuation + '0123456789'


def read_first_line(f_txt):
    with open(f_txt, 'r') as f:
        return f.read().split('\n')[0]


class TextProcessor:
    def __init__(self, embedding_dim=100):
        self.embedding_dim = embedding_dim
        self.vectors = gensim.downloader.load('glove-wiki-gigaword-50')
        self.bert_encoder = BertEncoder()

    def normalize_document(self, doc):
        # lower case and remove special characters\whitespaces
        doc = re.sub(r'[^a-zA-Z\s]', '', doc, re.I | re.A)
        doc = doc.lower()
        doc = doc.strip()
        # tokenize document
        tokens = wpt.tokenize(doc)
        # filter stopwords out of document
        filtered_tokens = [
            token for token in tokens if token not in stop_words]
        return filtered_tokens

    def process(self, dataset):
        for f in tqdm(glob.glob(f'./datasets/{dataset}/*/annotations.txt')):
            sentence = read_first_line(f)

            # Generate Bert embedding
            # bert_vec = self.bert_encoder.encode(sentence)
            # np.save(f.replace('annotations.txt', 'bert_512.npy'), bert_vec)

            # Word2vec embedding
            words = [word.lower() for word in sentence.split()
                     if word not in remove_terms]
            words = self.normalize_document(' '.join(words))

            res = []

            for w in words:
                if w in self.vectors:
                    res.append(self.vectors[w])
                else:
                    res.append(self.vectors['unknown'])

            vectors = np.array(res)
            np.save(f.replace('annotations.txt', 'embedding_50.npy'), vectors)


if __name__ == '__main__':
    text_processor = TextProcessor()
    text_processor.process('train')
    text_processor.process('valid')
    text_processor.process('test')
