from datasets.generate import DataGenerator

if __name__ == "__main__":
<<<<<<< HEAD
    data_generator = DataGenerator('../datasets/info/captions_train2014.json')
    data_generator.generate_data(list(range(0, 5000)), '../datasets/train')
    data_generator.generate_data(list(range(5000, 6000)), '../datasets/valid')
    data_generator.generate_data(list(range(6000, 7000)), '../datasets/test')
=======
    data_generator = DataGenerator('./datasets/info/captions_train2014.json')
    data_generator.generate_data(list(range(0, 10000)), './datasets/train')
    data_generator.generate_data(list(range(10000, 11000)), './datasets/valid')
    data_generator.generate_data(list(range(11000, 12000)), './datasets/test')
>>>>>>> 05234b15729f5d34f37936bade87334fdf932d87
