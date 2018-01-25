
# python 3 


import pandas as pd 
import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os


# get db_url via env variable export 
db_url = os.environ['db_url']
print ('db_url : ' , db_url)




class extract_from_db(object):
	def __init__(self,db_url):
		self.db_url = db_url 
		self.engine = create_engine(db_url)
		self.conn =  engine.connect()


	def get_data_from_fb(sql, table_name):
		db_url = self.db_url
		engine = self.engine
		conn = self.conn 
		try:
			# need to double check 
			print (sql)
			print ('table_name : ', table_name )
			df = df.from_sql(sql=sql, name= table_name, con= engine)
			# close the connection after imput data 
			conn.close()
			print (df.head())
			return df 
			print("extract data ok")

		except Exception as e:
			print (e)
			print ('fail to get data from db') 

	def get_table_list():
		pass 


	def get_view_list():
		pass 















# ==================

# pandas.read_sql(sql, con, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None)[source]
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_sql.html

def get_data_from_db(sql, db_url):
    try:
        engine = create_engine(db_url)
        #conn = engine.connect()
        # need to double check 
        print (sql)
        df = pd.read_sql(sql=sql, con= engine)
        # close the connection after imput data 
        #conn.close()
        print (df.head())
        return df 
        print("extract data ok")
    except Exception as e:
        print (e)
        print ('fail to get data from db')


# ==================


