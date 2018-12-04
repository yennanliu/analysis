# python 3 



##########################################################
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
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("LOAD MYSQL DATABASE")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


HOST = os.environ['HOST']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DATABASE = os.environ['DATABASE']



url="jdbc:mysql://{}/{}".format(HOST, DATABASE)
# For SQLServer, pass in the "driver" option
# driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
# Add "driver" : driverClass
connectionProperties = {
  "user" : USER,
  "password" : PASSWORD
}
table= "Soft_Job"
spark_df = sqlContext.read.jdbc(url=url, table=table , properties=connectionProperties)
pandas_df = spark_df.toPandas()
#sqlContext=SQLContext(sc)
#df=sqlContext.read.jdbc(url=url, table=pushdown_query, properties=properties)
print ('='*70)
print ('spark_df : ', spark_df.take(40))
print (type(spark_df))
print ('pandas_df : ', pandas_df.head(40))
print (type(pandas_df))
print ('='*70)

##### run via command line #####   
# spark-submit --packages mysql:mysql-connector-java:5.1.38 Spark_load_MySQL_demo.py


