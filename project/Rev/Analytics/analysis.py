
# python 3 
# load library 
# op 
import pandas as pd
import numpy as np


def load_data():
	df = pd.read_csv('kc_house_data.csv')
	return df 


def get_avg_price_bedroom_bathroom(df):
	df['get_avg_price_bedroom']  = df['price']/df['bedrooms']
	df['get_avg_price_bathrooms']  = df['price']/df['bathrooms']
	print ('avg price bedroom & bathrooms : ')
	print (df.head(10)[['price','get_avg_price_bedroom', 'get_avg_price_bathrooms']])
	#return df 

def get_outlier(df):
	"""
	1) price : 
	there are numbers of house data with abnormal high price, filter them
	can better overall price data distribution for following modeling 
	( oversrve via price boxplot)
	2) avg_price_sqft_living :
	avg_price_sqft_living = price / sqft_living = "average price per living sqft"
	It's abnormal for some houses with too high avg_price_sqft_living 
	(but as same as other houses with other conditions )
	"""
	high_price_id = list(set(df[(df['price'] > df['price'].quantile(0.97))]['id']))
	df['avg_price_sqft_living'] = df['price']/df['sqft_living']
	high_price_sqft_living_id = list(set(df[(df['sqft_living'] > df['sqft_living'].quantile(0.97))]['id']))
	outlier_list = list(set(high_price_id) & set(high_price_sqft_living_id))
	#print (outlier_list)
	return outlier_list


if __name__ == '__main__':
	df = load_data()
	get_avg_price_bedroom_bathroom(df)
	outlier_list = get_outlier(df)
	print ('outlier_list : ')
	print (outlier_list)





    