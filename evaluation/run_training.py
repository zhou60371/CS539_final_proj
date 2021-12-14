from keras.optimizers import adam
from datasets.loader import DatasetSequence
from model.network import model
from model.utils import contrastive_loss
from keras.metrics import BinaryAccuracy
from keras.callbacks import ModelCheckpoint

checkpoint = ModelCheckpoint(
    "./model/weights/saved-model-{epoch:02d}.hdf5",
    verbose=1, save_best_only=False, mode='max')

adam = adam.Adam()
model.compile(loss=contrastive_loss,
              optimizer=adam,
              metrics=[BinaryAccuracy()])
model.summary()

model.fit(DatasetSequence('train', 50),
          validation_data=DatasetSequence('valid', 50),
          epochs=100, verbose=1, callbacks=[checkpoint])
