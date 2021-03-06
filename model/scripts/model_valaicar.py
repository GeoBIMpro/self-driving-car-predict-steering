from __future__ import print_function

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, SpatialDropout2D
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D

model_val = Sequential()

#First Convolutional Layer with stride of 2x2 and kernel size 5x5
model_val.add(Convolution2D(24, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same', input_shape=(3,120,160), init = "normal", bias = True))
#model_val.add(SpatialDropout2D(0.5))

#Second Convolutional Layer with stride of 2x2 and kernel size 5x5
model_val.add(Convolution2D(36, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same', init = "normal", bias = True))
#model_val.add(SpatialDropout2D(0.5))

#Third Convolutional Layer with stride of 2x2 and kernel size 5x5
model_val.add(Convolution2D(48, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same', init = "normal", bias = True))
#model_val.add(SpatialDropout2D(0.5))

#Fourth Convolutional Layer with no stride and kernel size 3x3
model_val.add(Convolution2D(64, 5, 5, activation='relu', border_mode = 'same', init = "normal", bias = True))
#model_val.add(SpatialDropout2D(0.5))

#Fifth Convolutional Layer with no stride and kernel size 3x3
model_val.add(Convolution2D(64, 8, 8, activation='relu', border_mode = 'same', init = "normal", bias = True))

model_val.add(Flatten())
model_val.add(Dense(1164, activation='relu', init = "normal", bias = True))
model_val.add(Dense(100, activation='relu', init = "normal", bias = True))
model_val.add(Dense(50, activation='relu', init = "normal", bias = True))
model_val.add(Dense(10, activation='relu', init = "normal", bias = True))
model_val.add(Dense(1, activation='tanh', init = "normal", bias = True))
model_val.summary()

model_val_json = model_val.to_json()
with open("model_valaicar.json", "w") as json_file:
    json_file.write(model_val_json)
