# ops 
import pandas as pd 
import numpy as np
import psycopg2
from sqlalchemy import create_engine
from pytz import timezone
import datetime
import os

# UDF 
from grab_from_db import *


def get_data():
	sql_test = """
				SELECT * FROM rw.blue_move
				limit 10 
				"""
	get_data_from_db = work_with_db(db_url)
	df_ = get_data_from_db.read_from_db(sql_test)
	print (df_)
	return df_



if __name__ == '__main__':
	get_data()


