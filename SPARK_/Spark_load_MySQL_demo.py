# python 3 

# OP
import pandas as pd 
# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("LOAD MYSQL DATABASE")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


# ------------------ METHOD 1)  ------------------
print ('='*70)
spark_table = sqlContext.read.format("jdbc").options(
				url ="jdbc:mysql://localhost/local_dev",
				driver="com.mysql.jdbc.Driver",
				dbtable="movie_metadata",
				user="root",
				password="",
				).load()

#spark_df = sqlContext.sql("select * from movie_metadata ")
#spark_table.take(50)
#print ('='*70)



# ------------------ METHOD 2)  ------------------
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
df = sqlContext.read.jdbc(url=url, table=pushdown_query, properties=connectionProperties)
#sqlContext=SQLContext(sc)
#df=sqlContext.read.jdbc(url=url, table=pushdown_query, properties=properties)
print ('='*70)
print (df.take(40))
#print (df.todf().take(40))
print (type(df))
print ('='*70)


# run via command line 
# spark-submit --packages mysql:mysql-connector-java:5.1.38 Spark_load_MySQL_demo.py





