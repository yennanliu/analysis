from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
import os 

conf = SparkConf().setAppName("building a warehouse")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)


#logFile = "YOUR_SPARK_HOME/README.md"  # Should be some file on your system
spark_home = os.environ.get('SPARK_HOME', None)
logFile = sc.textFile(spark_home + "/README.md")

logData = sc.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

sc.stop()