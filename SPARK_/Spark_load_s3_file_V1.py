# python 3 
# https://gist.github.com/jakechen/6955f2de51212163312b6430555b8e0b
# Example uses GDELT dataset found here: https://aws.amazon.com/public-datasets/gdelt/
# Column headers found here: http://gdeltproject.org/data/lookups/CSV.header.dailyupdates.txt

# OP
import pandas as pd 
from urllib.request import urlopen
# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.ml import Pipeline

conf = SparkConf().setAppName("building a LINEAR MODEL")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

# Load RDD
lines = sc.textFile("s3://gdelt-open-data/events/2016*") # Loads 73,385,698 records from 2016
# Split lines into columns; change split() argument depending on deliminiter e.g. '\t'
parts = lines.map(lambda l: l.split('\t'))
# Convert RDD into DataFrame
html = urlopen("http://gdeltproject.org/data/lookups/CSV.header.dailyupdates.txt").read().rstrip()
columns = html.split('\t')
df = spark.createDataFrame(parts, columns)
print (df)