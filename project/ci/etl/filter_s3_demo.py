import sys
sys.path.append("./utility/")
import os
import pyspark
import math 
import pygeohash as pgh
from datetime import datetime
from pyspark.sql import SQLContext, Row
from pyspark import SparkContext
from pyspark.sql import functions as F
# UDF 
from utility import * 

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages com.amazonaws:aws-java-sdk-pom:1.7.4,org.apache.hadoop:hadoop-aws:2.7.6 pyspark-shell'
# aws access
aws_creds = parse_config('config/s3.config')
AWSAccessKey = aws_creds['AWSAccessKey']
AWSSecretKey = aws_creds['AWSSecretKey']
sc = SparkContext.getOrCreate()
sc._jsc.hadoopConfiguration().set('fs.s3a.access.key', AWSAccessKey)
sc._jsc.hadoopConfiguration().set('fs.s3a.secret.key', AWSSecretKey)
sqlContext = pyspark.sql.SQLContext(sc)
# file url
s3_file_name =aws_creds['s3_file_name']

def main():
  data = sc.textFile(s3_file_name).map(lambda line: line.split(","))
  headers = data.first()
  data_ = data.filter(lambda row: row != headers and row != [''])  # fix null data 
  # filter data
  collected_code = ['120042', '105001']
  filter_data = data_.filter(lambda x : x[3] in collected_code)
  filter_data.saveAsTextFile("s3a://<s3_bucket>/<s3_file>/output")

if __name__ == '__main__':
    main()
