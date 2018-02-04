# ops 
import pandas as pd 
import numpy as np
import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os
import math
#from folium.plugins import HeatMap


# ML

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.recurrent import LSTM, GRU
from keras.layers import Convolution1D, MaxPooling1D
from keras.callbacks import Callback
from keras.layers import BatchNormalization
from keras.layers import LeakyReLU
from keras.callbacks import ReduceLROnPlateau
from keras import optimizers
from keras import regularizers


# UDF 
from grab_from_db import *
from sql_collect import * 
#------------------------



def get_data(from_db= False):

	if from_db==True:

		sql_trips= sql_agg['day_zone_trip']
		#sql_trips_agg= sql['sql_trips_agg']
		get_data_from_db = work_with_db(db_url)
		df_ = get_data_from_db.read_from_db(sql_trips)
		print (df_)
		return df_
	else:
		df_ = pd.read_csv('trip_zone_agg_20180203.csv') 

	print (df_.head())
	return df_ 


def preprocess(df):
	df_ = df.copy()
	df_['trip_start_day'] = pd.to_datetime(df_.trip_start_day)
	df_.loc[:, 'tripstart_day_'] = df_['trip_start_day'].dt.day
	df_.loc[:, 'tripstart_weekday'] = df_['trip_start_day'].dt.weekday
	df_.loc[:, 'tripstart_month'] = df_['trip_start_day'].dt.month
	df_.loc[:, 'tripstart_year'] = df_['trip_start_day'].dt.year 
	df_.loc[:, 'tripstart_day'] = df_['trip_start_day'].dt.day
	df_.loc[:,'dayofyear'] = df_['trip_start_day'].apply(lambda x: x.dayofyear)
	df_['month_num'] = (df_['tripstart_day']-1)/30.
	df_['year_sin'] = (df_['dayofyear'] * 2 * math.pi).apply(math.sin)
	df_['year_cos'] = (df_['dayofyear'] * 2 * math.pi).apply(math.cos)
	df_['month_sin'] = (df_['month_num'] * 2 * math.pi).apply(math.sin)
	df_['month_cos'] = (df_['month_num'] * 2 * math.pi).apply(math.cos)
	print (df_)
	return df_ 



# -------------- Classification 
def classify_model():
	pass 


# -------------- Regression 

def regression_model(df):
	# fitting with scaled data 
	model = Sequential()
	model.add(Dense(500, input_shape = (1, )))
	model.add(Activation('relu'))
	model.add(Dropout(0.25))
	model.add(Dense(250))
	model.add(Activation('relu'))
	model.add(Dense(1))
	model.add(Activation('linear'))
	model.compile(optimizer='adam', loss='mse')
# --------------
	### only get pickups as input / target data values 
	x__ = df_.pickups
	Y_train = df_.pickups
	params = []
	for xt in x__: # taking training data from unscaled array
		xt = np.array(xt)
		#print (xt)
		mean_ = xt.mean()
		scale_ = x__.std()
		params.append([mean_, scale_])

	predicted = model.predict(x__)
	new_predicted = []

	# restoring data
	for pred, par in zip(predicted, params):
		a = pred*par[1]
		a += par[0]
		new_predicted.append(a)

# --------------
	new_predicted_ = np.array(new_predicted).flatten()
	new_predicted_ = pd.DataFrame(new_predicted_, dtype='str')
	output=pd.DataFrame()
	output['actual'] =Y_train
	output['predict'] =new_predicted_
	output
	print (output)
	#return output 

# --------------



if __name__ == '__main__':
	df = get_data()
	df_ = preprocess(df)
	regression_model(df_)







