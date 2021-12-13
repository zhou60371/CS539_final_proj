from keras.optimizers import adam_v2
from datasets.loader import DatasetSequence
from model.network import model
from model.utils import contrastive_loss

adam = adam_v2.Adam(lr=0.00001)
model.compile(loss=contrastive_loss, optimizer=adam)
model.summary()

model.fit(DatasetSequence('train'),
          validation_data=DatasetSequence('valid'),
          epochs=30, verbose=1)
