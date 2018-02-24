# python 3 

# ops 
import pandas as pd 
import numpy as np
import psycopg2
from sqlalchemy import create_engine

# ML
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.recurrent import LSTM, GRU
from keras.layers import Convolution1D, MaxPooling1D
from keras.callbacks import Callback

# UDF 
from grab_from_db import *
from sql_collect import * 
#------------------------


def get_data():
	sql_itime_zone= sql_itime['itime_zone']
	#sql_trips_agg= sql['sql_trips_agg']
	get_data_from_db = work_with_db(db_url)
	df_ = get_data_from_db.read_from_db(sql_itime_zone)
	print (df_)
	return df_

def preprocess(df):
	df_ = df.copy()
	df_ = df_.dropna()
	df_['date'] =pd.to_datetime(df_.date)
	df_.loc[:, 'weekday'] = df_['date'].dt.weekday
	return df_ 


def get_train_data(df):
	df_expo = df[df.drop_off_addr == 'expo']
	dataset = df_expo.groupby('timestamp_live_vec_table')\
					 .median()[['lag_idle_day']]\
					 .values
	dataset = dataset.astype('float32')
	#print (shape(dataset))
	print (dataset) 
	return dataset


#------------------------
# DL 

# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return np.array(dataX), np.array(dataY)


def one_input_LSTM(dataset):
	# normalize the dataset
	scaler = MinMaxScaler(feature_range=(0, 1))
	dataset = scaler.fit_transform(dataset)
	# split into train and test sets
	train_size = int(len(dataset) * 0.67)
	test_size = len(dataset) - train_size
	train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
	# reshape into X=t and Y=t+1
	look_back = 1
	trainX, trainY = create_dataset(train, look_back)
	testX, testY = create_dataset(test, look_back)
	# reshape input to be [samples, time steps, features]
	trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
	testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
	# create and fit the LSTM network
	model = Sequential()
	model.add(LSTM(4, input_shape=(1, look_back)))
	model.add(Dense(1))
	model.compile(loss='mean_squared_error', optimizer='adam')
	model.fit(trainX, trainY, epochs=20, batch_size=1, verbose=2)
	# make predictions
	trainPredict = model.predict(trainX)
	testPredict = model.predict(testX)
	# invert predictions
	trainPredict = scaler.inverse_transform(trainPredict)
	trainY = scaler.inverse_transform([trainY])
	testPredict = scaler.inverse_transform(testPredict)
	testY = scaler.inverse_transform([testY])
	# calculate root mean squared error
	trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
	print('Train Score: %.2f RMSE' % (trainScore))
	testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
	print('Test Score: %.2f RMSE' % (testScore))
	# shift train predictions for plotting
	trainPredictPlot = np.empty_like(dataset)
	trainPredictPlot[:, :] = np.nan
	trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
	# shift test predictions for plotting
	testPredictPlot = np.empty_like(dataset)
	testPredictPlot[:, :] = np.nan
	testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict





if __name__ == '__main__':
	# prepare data 
	df_ = get_data()
	df_ = preprocess(df_)
	dataset = get_train_data(df_)
	# ML 
	one_input_LSTM(dataset)










