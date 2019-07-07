import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
import numpy as np
from keras.utils import np_utils
from keras.datasets import mnist
import matplotlib.pyplot as plt

(train_images, train_labels), (test_images, test_labels)= mnist.load_data()
#print (train_images.shape)
#preprocess images because we need to specify 1 channel
train_images = train_images.reshape(train_images.shape[0], 28, 28, 1)
#print (train_images.shape)
test_images = test_images.reshape(test_images.shape[0], 28, 28, 1)
train_images = train_images / 255.0
test_images = test_images / 255.0
#preprocess labels because only 10 labels
train_labels = np_utils.to_categorical(train_labels, 10)
test_labels = np_utils.to_categorical(test_labels, 10)


model = Sequential()
model.add(Convolution2D(32,(3,3),activation = 'relu', input_shape=(28,28,1)))
model.add(Convolution2D(32,(3,3), activation = 'relu'))
model.add(MaxPooling2D( pool_size = (2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(train_images, train_labels, batch_size=32, epochs=5, verbose=1)
score = model.evaluate(test_images, test_labels)

#loss: 0.0469 accuracy: 0.9854
