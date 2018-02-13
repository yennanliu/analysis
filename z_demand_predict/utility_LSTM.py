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


# model 
# ----------------





