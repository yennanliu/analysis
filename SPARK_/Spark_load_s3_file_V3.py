import os
import pyspark
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.amazonaws:aws-java-sdk-pom:1.10.34,org.apache.hadoop:hadoop-aws:2.7.2 pyspark-shell'
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

sc = SparkContext()
sqlContext = SQLContext(sc)
filePath = "s3n://jon-parquet-format/nation.plain.parquet"
df = sqlContext.read.parquet(filePath) # Parquet file read example
print (df.head(100))