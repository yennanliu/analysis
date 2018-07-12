# python 3 

# ops 
import pandas as pd 
import numpy as np
import psycopg2
from sqlalchemy import create_engine
import math

# ML
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


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
	df_x = df.copy()
	df_x['date'] =pd.to_datetime(df_x.date)
	df_x.loc[:, 'weekday'] = df_x['date'].dt.weekday
	df_x.loc[:, 'day'] = df_x['timestamp_live_vec_table'].dt.day
	df_x.loc[:, 'month'] = df_x['timestamp_live_vec_table'].dt.month
	df_x.loc[:, 'year'] = df_x['timestamp_live_vec_table'].dt.year
	df_x.loc[:, 'hour'] = df_x['timestamp_live_vec_table'].dt.hour
	df_x.loc[:, 'minute'] = df_x['timestamp_live_vec_table'].dt.minute
	df_x.loc[:,'dayofyear'] = df_x['timestamp_live_vec_table'].apply(lambda x: x.dayofyear)
	df_x['year_sin'] = (df_x['dayofyear'] * 2 * math.pi).apply(math.sin)
	df_x['year_cos'] = (df_x['dayofyear'] * 2 * math.pi).apply(math.cos)
	print (df_x.head())
	return df_x 


def get_train_test_data(df):
	cols = ['lat',
			'lon', 
			'weekday',
			'day', 
			'month',
			'year', 
			'hour', 
			'minute',
			'dayofyear',
			'year_sin', 
			'year_cos',
			'lag_idle_day']
	df_ = df[cols]
	df_ = df_.dropna()
	# ----
	X = df_.iloc[:,:-1]
	y = df_.iloc[:,-1:]
	# train, test split 
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	return  X_train, X_test, y_train, y_test


def train_model(X_train, X_test, y_train, y_test):
	rf_model = RandomForestRegressor(max_depth=2, random_state=0)
	rf_model.fit(X_train,y_train)
	print (rf_model.score(X_test,y_test))
	output = pd.DataFrame({'actual':y_test['lag_idle_day'],'pred':rf_model.predict(X_test)})
	print (output)
	return rf_model, output


if __name__ == '__main__':
	df = get_data()
	df_ = preprocess(df)
	X_train, X_test, y_train, y_test = get_train_test_data(df_)
	train_model(X_train, X_test, y_train, y_test)




