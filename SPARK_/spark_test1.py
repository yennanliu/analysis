import os

# run pysark script via command line 
# /Users/yennanliu/spark/bin/spark-submit spark_test1.py
# https://stackoverflow.com/questions/30674467/spark-in-yarn-cluser-sc-not-defined



from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext

conf = SparkConf().setAppName("building a warehouse")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)


spark_home = os.environ.get('SPARK_HOME', None)
text_file = sc.textFile(spark_home + "/README.md")



word_counts = text_file \
    .flatMap(lambda line: line.split()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)



word_counts.collect()

print (word_counts.collect())