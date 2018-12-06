# python 3 



##########################################################
# ANALYSIS MYSQL DATA VIA SPARL OPS 
#
# REF  
# https://stackoverflow.com/questions/48054270/load-data-from-the-mysql-db-using-pyspark-in-python-3
#
#
#
##########################################################



# OP
import pandas as pd 
import os 
# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row


#------------------------------------------------------
# spark config 
conf = SparkConf().setAppName("LOAD PTT MYSQL DATABASE")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

# mysql credential
HOST = os.environ['HOST']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DATABASE = os.environ['DATABASE']
#------------------------------------------------------


#------------------------------------------------------
def get_mysql_creds():
	url = "jdbc:mysql://{}/{}".format(HOST, DATABASE)
	creds = {"url":url,
	"connectionProperties" : {
	"user" : USER,
	"password" : PASSWORD}}
	return creds 


def get_ptt_table_data(creds, table):
	creds = get_mysql_creds()
	spark_df = sqlContext.read.jdbc(url=creds['url'],properties=creds['connectionProperties'], table=table )
	#spark_df = sqlContext.read.jdbc(url=creds['url'],properties=creds['connectionProperties'], dbtable=SQL )
	pandas_df = spark_df.toPandas()
	return spark_df, pandas_df 


def query_spark_SQL(spark_df,SQL):
	spark_df.registerTempTable("temp_sql_table")
	print (SQL)
	spark_sql_output=sqlContext.sql(SQL) 	
	return spark_sql_output


def digest_ptt_data(spark_df):
	# conver Spark df back to Spark RDD
	# https://stackoverflow.com/questions/29000514/how-to-convert-a-dataframe-back-to-normal-rdd-in-pyspark
	spark_RDD = spark_df.rdd
	digested_RDD = spark_RDD.map(
	lambda x: Row(
	author_ip = x['author_ip'],
	timestamp=x['date'].strftime('%Y-%m-%d')))\
	.take(10)
	print (digested_RDD)
	return digested_RDD


#------------------------------------------------------
 

if __name__ == '__main__':
	creds = get_mysql_creds()
	spark_df, pandas_df  = get_ptt_table_data(creds, "Soft_Job")
	print ('='*70)
	print ('spark_df : ', spark_df.take(30))
	print (type(spark_df))
	print ('pandas_df : ', pandas_df)
	print (type(pandas_df))
	#SQL="""SELECT author_ip,count(*) from temp_sql_table group by 1  order by 2 desc"""
	SQL="""SELECT author_ip, date from temp_sql_table limit 1000 """
	spark_sql_output = query_spark_SQL(spark_df, SQL)
	print ('Spark_SQL_output : ', spark_sql_output.take(30))
	digested_ptt_data = digest_ptt_data(spark_df)
	print ('digest_ptt_data : ', digested_ptt_data)
	print ('='*70)


	##### run via command line #####   
	# spark-submit --packages mysql:mysql-connector-java:5.1.38 Spark_load_MySQL_demo.py


