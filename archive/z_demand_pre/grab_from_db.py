
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


# ==================



class work_with_db:
	def __init__(self,db_url):
		self.db_url = db_url 
        
	def read_from_db(self,sql):
		engine = create_engine(self.db_url)
		conn =  engine.connect()
		try:
			# need to double check 
			print (sql)
			#print ('table_name : ', table_name )
			df = pd.read_sql(sql=sql, con= engine)
			# close the connection after imput data 
			conn.close()
			print (df.head())
			return df 
			print("extract data ok")

		except Exception as e:
			print (e)
			conn.close()
			print ('fail to get data from db')

	def get_table_list(self):
		pass 


	def get_view_list(self):
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


