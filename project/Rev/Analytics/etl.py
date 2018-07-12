# python 3 

import pandas as pd
import psycopg2
import sys



def get_data_source():
	# load the data source
	print ('load data source ') 
	df=pd.read_csv('kc_house_data.csv')
	print (df.head(3))
	return df 

def store_data_DB(df):
	# make db connetion
	print ('connect to DB')
	# conn = psycopg2.connect(database = "projetofinal", user = "postgres", password = "admin", host = "localhost", port = "5432")
	connection = psycopg2.connect(database = database, user = user, password = password, host = host, port = "5432")
	cursor = connection.cursor()
	print ('start insert data to DB')
	count = 0 
	try:
		for row in df.itterows():
			# print(mems['change_id'], mems['member_id'], mems['phone_number'])
			cursor.execute(
			"""INSERT into kc_house_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
			(row['id'], row['date'], row['price'], row['bedrooms'],
			row['bathrooms'],row['sqft_living'], row['sqft_lot'], row['floors'], 
			row['waterfront'],row['view'], row['condition'], row['grade'],
			row['sqft_above'], row['sqft_basement'], row['yr_built'], row['yr_renovated'],
			row['zipcode'], row['lat'], row['long'], row['sqft_living15'],
			row['sqft_lot15']))
			count += 1
			cursor.execute('COMMIT;')
			print ('insert {} rows into DB !'.format(str(count)))
	except Exception as e:
		print (e)
		print ('insert failed')


def create_table(db_url):
	connection = psycopg2.connect(database = database, user = user, password = password, host = host, port = "5432")
	cursor = connection.cursor() 
	pass 









