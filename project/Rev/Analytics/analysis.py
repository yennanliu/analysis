
# python 3 
# load library 
# op 
import pandas as pd
import numpy as np



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








    