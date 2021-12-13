from datasets.generate import DataGenerator

if __name__ == "__main__":
    data_generator = DataGenerator('../datasets/info/captions_train2014.json')
    data_generator.generate_data(list(range(0, 5000)), '../datasets/train')
    data_generator.generate_data(list(range(5000, 6000)), '../datasets/valid')
    data_generator.generate_data(list(range(6000, 7000)), '../datasets/test')
