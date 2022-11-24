from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255,shear_range=2.0,zoom_range=2.0,horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
x_train = train_datagen.flow_from_directory(r'C:\Users\gowtham\Downloads\IBM\Dataset\TRAIN_SET',target_size=(64,64),batch_size=5,color_mode='rgb',class_mode='sparse')
x_test = train_datagen.flow_from_directory(r'C:\Users\gowtham\Downloads\IBM\Dataset\TEST_SET',target_size=(64,64),batch_size=5,color_mode='rgb',class_mode='sparse')
print(x_train.class_indices)

print(x_test.class_indices)


from collections import Counter as c
c(x_train.labels)
import numpy as np
import tensorflow

from tensorflow.keras.models import Sequential
from tensorflow.keras import layers

from tensorflow.keras.layers import Dense,Flatten

from tensorflow.keras.layers import Conv2D,MaxPooling2D,Dropout
model=Sequential()
## add and initializing CNN(Convolutional Neural Net) layer

classifier=Sequential()
classifier.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Conv2D(32,(3,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Flatten())
## adding denser layer

classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=5, activation='softmax'))
classifier.summary()


