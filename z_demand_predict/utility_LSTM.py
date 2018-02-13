# ops 
import pandas as pd 
import numpy as np
import datetime
import os


# ML

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.recurrent import LSTM, GRU
from keras.layers import Convolution1D, MaxPooling1D
from keras.callbacks import Callback
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error



# data preprocess 
# ----------------

# from dataframe to float32 numpy metrix 
def prepare_data(df,cols):
	print (cols)
	df__ = df_[cols]
	dataset = df__.values
	dataset = dataset.astype('float32')
	return dataset



# credit 
# https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/
# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
	"""
	LSTM for Regression with Window Method : can modify look_back, e.g.  look_back = 1,2,3...
	"""
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return np.array(dataX), np.array(dataY)


def reshape_dataset(data_,time_series=False):
	if time_series=False:
		"""
		reshape input to be [samples, time steps, features]
		e.g.
		trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
		testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
		"""
		data_reshape = numpy.reshape(data_, (data_.shape[0], 1, data_.shape[1]))

	else:
		"""
		reshape input to be [samples, time steps, features]
		e.g.
		trainX = numpy.reshape(trainX, (trainX.shape[0], trainX.shape[1], 1))
		testX = numpy.reshape(testX, (testX.shape[0], testX.shape[1], 1))
		"""
		data_reshape = numpy.reshape(data_, (data_.shape[0], data_.shape[1], 1))

	return data_reshape



# model 
# ----------------


def simple_LSTM(trainX,trainY):
	model = Sequential()
	model.add(LSTM(4, input_shape=(1, look_back)))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	model.fit(trainX, trainY, epochs=20, batch_size=1, verbose=2)
	return model



def LSTM_model_memory_batch(trainX,trainY):
	model = Sequential()
	model.add(LSTM(4, batch_input_shape=(batch_size, look_back, 1), stateful=True))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	for i in range(100):
		model.fit(trainX, trainY, epochs=1, batch_size=batch_size, verbose=2, shuffle=False)
		model.reset_states()
	return model 












