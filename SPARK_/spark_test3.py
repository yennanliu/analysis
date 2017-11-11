# python 2.7 


import pandas as pd, numpy as np
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext


conf = SparkConf().setAppName("building a warehouse")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)
print (sc)
"""
df_s = sc.textFile("df_test.csv")
type(df_s)
df_s.count()
df_s.take(10)
"""
########


from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)


df_test = sqlContext.read.format('com.databricks.spark.csv')\
						 .options(header='true', inferschema='true')\
						 .load('df_test.csv')

df_test.show()


print ("=======================")


df_test.registerTempTable("numeric")
sqlContext.sql("""SELECT * FROM numeric limit 2 """).show()


















