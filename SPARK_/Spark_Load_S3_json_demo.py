# python 3 
# https://github.com/donwany/Databricks/blob/master/S3.ipynb


# OP
import pandas as pd 
import os 
# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession


##### config #####
conf = SparkConf().setAppName("LOAD S3 BUCKET")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)
spark = SparkSession.builder\
		.master("local")\
		.appName("GET S3 BUCKET")\
		.config("spark.some.config.option", "some-value")\
		.getOrCreate()


hconf = sc._jsc.hadoopConfiguration()  
hconf.set("fs.s3a.access.key", "AKIAJZ5G3XLP4NU4QIUQ")  
hconf.set("fs.s3a.secret.key", "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")


df_data_1 = spark.read.format('org.apache.spark.sql.execution.datasources.csv.CSVFileFormat')\
          .option('header', 'true')\
          .load('s3a://simpleapp-a/advertising.csv')

print ('='*70)
df_data_1.printSchema()
print ('='*70)