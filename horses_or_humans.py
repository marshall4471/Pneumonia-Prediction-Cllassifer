# -*- coding: utf-8 -*-
"""horses_or_humans.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ta4TDj8LS8uPgRdNcfFYCFT6ISDH6Bj2
"""



from google.colab import drive
drive.mount("/content/gdrive")

file1 = ("/content/gdrive/MyDrive/horses_or_humans/horse-or-human/train")

file2 = ("/content/gdrive/MyDrive/horses_or_humans/horse-or-human/validation")

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

train_set = train_datagen.flow_from_directory(file1,
                                                 target_size = (64, 64),
                                                 batch_size = 32,
                                                 class_mode = 'binary')

import tensorflow as tf

test_datagen = ImageDataGenerator(rescale = 1./255)

test_set = test_datagen.flow_from_directory(file2,
                                            target_size = (64, 64),
                                            batch_size = 32,
                                            class_mode = 'binary')



cnn = tf.keras.models.Sequential()
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=[64, 64, 3]))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Conv2D(filters=32, kernel_size=3, activation='relu'))
cnn.add(tf.keras.layers.MaxPool2D(pool_size=2, strides=2))
cnn.add(tf.keras.layers.Flatten())
cnn.add(tf.keras.layers.Dense(units=128, activation='relu'))
cnn.add(tf.keras.layers.Dense(units=1, activation='sigmoid'))
cnn.compile(optimizer = 'adam', loss='binary_crossentropy', metrics=['accuracy'])
cnn.summary()

history = cnn.fit(train_set, validation_data =test_set, epochs=25, verbose=2)

cnn.save('horses_or_humans.h5')