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
# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("LOAD MYSQL DATABASE")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

# ------------------ METHOD 1)  ------------------
#jdbc_url = "jdbc:mysql://{0}:{1}/{2}".format(hostname, jdbcPort, dbname)
url="jdbc:mysql://localhost/local_deV"
# For SQLServer, pass in the "driver" option
# driverClass = "com.microsoft.sqlserver.jdbc.SQLServerDriver"
# Add "driver" : driverClass
connectionProperties = {
  "user" : "root",
  "password" : ""
}
pushdown_query = "select * from movie_metadata"
pushdown_query= "movie_metadata"
spark_df = sqlContext.read.jdbc(url=url, table=pushdown_query, properties=connectionProperties)
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


