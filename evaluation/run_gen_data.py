from datasets.generate import DataGenerator

if __name__ == "__main__":
    data_generator = DataGenerator('./datasets/info/captions_train2014.json')
    data_generator.generate_data(list(range(0, 10000)), './datasets/train')
    data_generator.generate_data(list(range(10000, 11000)), './datasets/valid')
    data_generator.generate_data(list(range(11000, 12000)), './datasets/test')
