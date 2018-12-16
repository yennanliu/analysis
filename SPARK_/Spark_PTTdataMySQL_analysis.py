# python 3 

####################################################################################################################
# ANALYZE MYSQL DATA VIA SPARK OPS 
#
# REF  
# https://stackoverflow.com/questions/48054270/load-data-from-the-mysql-db-using-pyspark-in-python-3
#
# PROCESS/ANALYZE DATA VIA BASIC SPARK OP (map, flatmap, groupbykey, reducebykey, SQL...)
# 
#
#
# QUICK START 
# 1) install spark 
# https://github.com/yennanliu/utility_shell/blob/master/spark/install_pyspark.sh
# 2) launch spark env 
# https://github.com/yennanliu/utility_shell/blob/master/spark/launch_pyspark.sh
# $export SPARK_HOME=/Users/$USER/spark && export PATH=$SPARK_HOME/bin:$PATH
# 3) run 
# spark-submit Spark_load_MySQL_demo.py
#
####################################################################################################################



# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row
from operator import add

# OP
import pandas as pd 
import os 
import boto3

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
try:
  AWS_KEY_ID = os.environ['AWS_KEY_ID']
  AWS_SECRET_KEY = os.environ['AWS_SECRET_KEY']
  bucketname = os.environ['bucketname']
except:
  print ('No S3 credential loaded')
#------------------------------------------------------


#------------------------------------------------------
# op help func 
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


def query_spark_df(spark_df,SQL):
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
                  .take(30)
	print (digested_RDD)
	return digested_RDD


def get_author_list(spark_df):
	spark_RDD = spark_df.rdd
	author_list = spark_RDD.map(
                lambda x : Row(
                author_id = x['author']))\
                .flatMap(lambda x : x)\
                .take(30)
	print (author_list)
	return author_list


def filter_this_year_data(spark_df):
	spark_RDD = spark_df.rdd
	this_year_post = spark_RDD.map(
                  lambda x: Row(
                  title = x['title'],
                  author_ip = x['author_ip'],
                  timestamp=x['date'].strftime('%Y-%m-%d')))\
                  .filter(lambda x : x['timestamp'] >= '2018-01-01')\
                  .take(30)
	print (this_year_post)
	return this_year_post


def filter_top_ip_groupbykey(spark_df):
  # pyspark action OP ref 
  # http://spark.apache.org/docs/2.1.0/api/python/pyspark.html
  # sort a list of tuples in pyspark
  # https://stackoverflow.com/questions/37658320/sorting-a-list-of-tuples-in-pyspark
  spark_RDD = spark_df.rdd
  top_ip = sorted(spark_RDD\
                .filter(lambda x : x['author_ip'] != None)\
                .map(lambda x: (x.author_ip,1))\
                .groupByKey().mapValues(len)\
                .collect())
  print (top_ip)
  return top_ip


def filter_top_ip_reducebykey(spark_df):
  # http://spark.apache.org/docs/2.1.0/api/python/pyspark.html
  spark_RDD = spark_df.rdd
  top_ip = spark_RDD\
                .filter(lambda x : x['author_ip'] != None)\
                .map(lambda x: (x.author_ip,1))\
                .reduceByKey(add)\
                .sortBy(lambda x: x[1], False)\
                .take(30)
  print (top_ip)
  return top_ip


def save_to_S3(region_name,finename,bucketname):
  # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html?highlight=upload#S3.Client.upload_file
  s3 = boto3.resource('s3',
                      region_name = region_name,
                      aws_access_key_id=AWS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_KEY)
  bucket = s3.Bucket(bucketname)

  try:
    s3.meta.client.upload_file(finename, bucketname, finename)
    print ('upload to S3 OK')
  except Exception as e:
    print (e)
    print ('upload failed')


#------------------------------------------------------
# main run func 
def main():
  creds = get_mysql_creds()
  spark_df, pandas_df  = get_ptt_table_data(creds, "Soft_Job")
  print ('='*70)
  print ('spark_df : ', spark_df.take(30))
  print (type(spark_df))
  print ('pandas_df : ', pandas_df)
  print (type(pandas_df))
  #SQL="""SELECT author_ip,count(*) from temp_sql_table group by 1  order by 2 desc"""
  SQL="""SELECT author_ip, date from temp_sql_table limit 1000 """
  spark_sql_output = query_spark_df(spark_df, SQL)
  print ('Spark_SQL_output : ', spark_sql_output.take(30))
  digested_ptt_data = digest_ptt_data(spark_df)
  print ('digested_ptt_data : ', digested_ptt_data)
  author_list = get_author_list(spark_df)
  print ('author_list : ', author_list)
  this_year_RDD = filter_this_year_data(spark_df)
  print ('this_year_RDD : ', this_year_RDD)
  top_ip = filter_top_ip_reducebykey(spark_df)
  print ('top_ip : ', top_ip)
  # save to csv and uplaod to s3 
  pandas_df.head(100).to_csv('pandas_df.csv')
  save_to_S3('eu-west-1','pandas_df.csv',bucketname)
  print ('='*70)


#------------------------------------------------------
if __name__ == '__main__':
  main()





