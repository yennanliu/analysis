# ops 
import pandas as pd 
import numpy as np
import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os
import math 

# ML 
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeRegressor
from sklearn import preprocessing

# UDF 
from grab_from_db import *
from sql_collect import * 
#------------------------


def get_data():
	sql_trips= sql_agg['day_zone_trip']
	#sql_trips_agg= sql['sql_trips_agg']
	get_data_from_db = work_with_db(db_url)
	df_ = get_data_from_db.read_from_db(sql_trips)
	print (df_)
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


#----------------
# dev 

def extract_feature(df):
	# onehot encode start_zone_name 
	# http://www.ritchieng.com/machinelearning-one-hot-encoding/
	df_ = df.copy()
	enc = preprocessing.OneHotEncoder()
	enc.fit(df_.start_zone_id.reshape(-1, 1) )
	onehotlabels = enc.transform(df_.start_zone_id.reshape(-1, 1)).toarray()
	return df_ 

#----------------



def get_train_test_set(df):
	xcols = ['start_zone_id', 'tripstart_day_',
	'tripstart_weekday', 'tripstart_month', 'tripstart_year', 'dayofyear',
	'tripstart_day', 'month_num', 'year_sin',  'month_sin',
	'month_cos']
	ycols = ['pickups'] 

	x = df[xcols]
	y = df[ycols]
	return x, y 


def train(x,y):
	regr_1 = DecisionTreeRegressor(max_depth=4)
	regr_1.fit(x,y)
	regr_1.predict(x)
	output = pd.DataFrame({'actual':y.pickups,'pred':regr_1.predict(x)})
	print (output)




#------------------------


if __name__ == '__main__':
	df = get_data()
	df_ = preprocess(df)
	x,y = get_train_test_set(df_)
	train(x,y)





