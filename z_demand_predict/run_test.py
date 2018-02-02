# ops 
import pandas as pd 
import numpy as np
import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os
import math 

# UDF 
from grab_from_db import *
from sql_collect import * 
#------------------------


def get_data():
	sql_trips= sql['sql_trips']
	get_data_from_db = work_with_db(db_url)
	df_ = get_data_from_db.read_from_db(sql_trips)
	print (df_)
	return df_


def preprocess(df):
	df_ = df.copy()
	df_['trip_start_date'] = pd.to_datetime(df_.trip_start_date)
	df_['trip_start_day'] = pd.to_datetime(df_.trip_start_day)
	df_.loc[:, 'tripstart_day'] = df_['trip_start_date'].dt.day
	df_.loc[:, 'tripstart_weekday'] = df_['trip_start_date'].dt.weekday
	df_.loc[:, 'tripstart_month'] = df_['trip_start_date'].dt.month
	df_.loc[:, 'tripstart_year'] = df_['trip_start_date'].dt.year 
	df_.loc[:, 'tripstart_hour'] = df_['trip_start_date'].dt.hour
	df_.loc[:, 'tripstart_minute'] = df_['trip_start_date'].dt.minute
	df_.loc[:,'dayofyear'] = df_['trip_start_day'].apply(lambda x: x.dayofyear)
	df_['month_num'] = (df_['tripstart_day']-1)/30.
	df_['year_sin'] = (df_['dayofyear'] * 2 * math.pi).apply(math.sin)
	df_['year_cos'] = (df_['dayofyear'] * 2 * math.pi).apply(math.cos)
	df_['month_sin'] = (df_['month_num'] * 2 * math.pi).apply(math.sin)
	df_['month_cos'] = (df_['month_num'] * 2 * math.pi).apply(math.cos)
	print (df_)
	return df_











#------------------------


if __name__ == '__main__':
	df = get_data()
	preprocess(df)





