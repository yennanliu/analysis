# python 3 

import pandas as pd
import psycopg2
import sys


# help function 
# ---------------------------------------
def get_data_source():
	# load the data source
	## data has multiple Ids ### 
	print ('load data source ') 
	df=pd.read_csv('kc_house_data.csv')
	print (df.head(3))
	return df 

def connect(user, password, db, host, port):
    return "host='" + host + "' dbname='" + db + "' user='" + user + "' password='" + password + "' port='" + port + "'"


def store_data_DB(df,database,user,password,host,port):
	# make db connetion
	print ('connect to DB')
	
	# conn = psycopg2.connect(database = "projetofinal", user = "postgres", password = "admin", host = "localhost", port = "5432")
	connection = psycopg2.connect(database = database, user = user, password = password, host = host, port = port)
	cursor = connection.cursor()
	print ('start insert data to DB')
	count = 0 
	try:
		for row in df.itterows():
			# print(mems['change_id'], mems['member_id'], mems['phone_number'])
			cursor.execute(
			"""INSERT into public.kc_house_data VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
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
	cursor.close()
	connection.close()




def create_table(database,user,password,host,port):
	connection = psycopg2.connect(database = database, user = user, password = password, host = host, port = port)
	cursor = connection.cursor() 
	sql_drop_table="""
	DROP TABLE IF EXISTS public.kc_house_data; 
	"""
	sql_create_table ="""
	CREATE TABLE public.kc_house_data 
	(id serial,
	 date TIMESTAMP without time zone, 
	 price numeric,
	 bedrooms INTEGER, 
	 bathrooms DECIMAL(3,2),
	 sqft_living  INTEGER,
	 sqft_lot  INTEGER,
	 floors  DECIMAL(3,2),
	 waterfront BOOLEAN,
	 view  INTEGER,
	 condition INTEGER, 
	 sqft_above INTEGER,
	 sqft_basement INTEGER,
	 yr_built INTEGER,
	 yr_renovated INTEGER,
	 zipcode VARCHAR,
	 lat DECIMAL(10,2),
	 long DECIMAL(10,2),
	 sqft_living15 INTEGER,
	 sqft_lot15 INTEGER );

	"""
	sql_alter_dtype = """
	ALTER TABLE public.kc_house_data  ALTER COLUMN id TYPE BIGINT;
	"""
	try:
		cursor.execute(sql_drop_table)
		cursor.execute('COMMIT;')
		cursor.execute(sql_create_table)
		cursor.execute('COMMIT;')
		cursor.execute(sql_alter_dtype)
		cursor.execute('COMMIT;')
		print ('create table OK')
	except Exception as e:
		print (e)
		print ('fail to create table')

	cursor.close()
	connection.close()

# ---------------------------------------


if __name__ == '__main__':
	# get data 
	df = get_data_source()
	# create table before dump data 
	create_table(database,user,password,host,port)
	# dump data into DB 
	store_data_DB(df,database,user,password,host,port)






