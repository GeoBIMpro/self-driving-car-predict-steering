from __future__ import print_function

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Merge
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, SpatialDropout2D
from keras.utils.visualize_util import plot

left_model = Sequential()
center_model = Sequential()
right_model = Sequential()

#First Convolutional Layer with stride of 2x2 and kernel size 5x5
left_model.add(Convolution2D(24, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same', input_shape=(3,120,160)))
left_model.add(SpatialDropout2D(0.5))
#Second Convolutional Layer with stride of 2x2 and kernel size 5x5
left_model.add(Convolution2D(36, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same'))
left_model.add(SpatialDropout2D(0.5))
#Third Convolutional Layer with stride of 2x2 and kernel size 5x5
left_model.add(Convolution2D(48, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same'))
left_model.add(SpatialDropout2D(0.5))
#Fourth Convolutional Layer with no stride and kernel size 3x3
left_model.add(Convolution2D(64, 3, 3, activation='relu', border_mode = 'same'))
left_model.add(SpatialDropout2D(0.5))
#Fifth Convolutional Layer with no stride and kernel size 3x3
left_model.add(Convolution2D(64, 3, 3, activation='relu', border_mode = 'same'))
left_model.add(Flatten())

#First Convolutional Layer with stride of 2x2 and kernel size 5x5
center_model.add(Convolution2D(24, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same', input_shape=(3,120,160)))
center_model.add(SpatialDropout2D(0.5))
#Second Convolutional Layer with stride of 2x2 and kernel size 5x5
center_model.add(Convolution2D(36, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same'))
center_model.add(SpatialDropout2D(0.5))
#Third Convolutional Layer with stride of 2x2 and kernel size 5x5
center_model.add(Convolution2D(48, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same'))
center_model.add(SpatialDropout2D(0.5))
#Fourth Convolutional Layer with no stride and kernel size 3x3
center_model.add(Convolution2D(64, 3, 3, activation='relu', border_mode = 'same'))
center_model.add(SpatialDropout2D(0.5))
#Fifth Convolutional Layer with no stride and kernel size 3x3
center_model.add(Convolution2D(64, 3, 3, activation='relu', border_mode = 'same'))
center_model.add(Flatten())

#First Convolutional Layer with stride of 2x2 and kernel size 5x5
right_model.add(Convolution2D(24, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same', input_shape=(3,120,160)))
right_model.add(SpatialDropout2D(0.5))
#Second Convolutional Layer with stride of 2x2 and kernel size 5x5
right_model.add(Convolution2D(36, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same'))
right_model.add(SpatialDropout2D(0.5))
#Third Convolutional Layer with stride of 2x2 and kernel size 5x5
right_model.add(Convolution2D(48, 5, 5, activation='relu', subsample = (2, 2), border_mode = 'same'))
right_model.add(SpatialDropout2D(0.5))
#Fourth Convolutional Layer with no stride and kernel size 3x3
right_model.add(Convolution2D(64, 3, 3, activation='relu', border_mode = 'same'))
right_model.add(SpatialDropout2D(0.5))
#Fifth Convolutional Layer with no stride and kernel size 3x3
right_model.add(Convolution2D(64, 3, 3, activation='relu', border_mode = 'same'))
right_model.add(Flatten())

merged = Merge([left_model, center_model, right_model], mode='concat')

model = Sequential()
model.add(merged)
model.add(Dense(1164, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(100, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(50, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='tanh'))
model.summary()

#plot(left_model, to_file='left_model.png')
#plot(center_model, to_file='center_model.png')
#plot(right_model, to_file='right_model.png')
#plot(model, to_file='model_merged.png')

model_json = model.to_json()
with open("model_merged.json", "w") as json_file:
    json_file.write(model_json)