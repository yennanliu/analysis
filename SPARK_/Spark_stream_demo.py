# python 3 



############################################################################################ 
# 
# REF 1) : Streaming basics 
# https://github.com/clumdee/Python-and-Spark-for-Big-Data-master/blob/master/Spark_Streaming/streaming_terminal_with_RDD.ipynb
# SPARK STREAM DEMO CODE  
#
#
# REF 2) : temp SQL table in Streaming window 
# https://spark.apache.org/docs/1.6.2/streaming-programming-guide.html
#
#
#
# ******************  QUICK START  ******************
# open the other terminal run : 
# $ nc -lk 9999 ( start the localhost:9999, Start the streaming session to the localhost)
# and type sth within that terminal
# i.e. 
# hello world 
# hello world 
#lol
#lo
#l
#. 
#.
# you should seed the spark stream get the session input and response as below
#-------------------------------------------
#Time: 2018-12-29 09:44:30
#-------------------------------------------
#('', 4)
#('l', 2)
#('lo', 2)
#('world', 4)
#('ll', 1)
#('hello', 4)
#('lol', 4)
#
#========= 2018-12-29 09:44:30 =========
#+-----+-----+
# word|total|
#+-----+-----+
#|    l|    2|
#|  lol|    4|
#|hello|    4|
#|   ll|    1|
#|world|    4|
#|     |    4|
#|   lo|    2|
#+-----+-----+ 
############################################################################################ 


from pyspark.streaming import StreamingContext
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row

#--------------------------------------------------
# help func 
# Lazily instantiated global instance of SQLContext
def getSqlContextInstance(sparkContext):
    if ('sqlContextSingletonInstance' not in globals()):
        globals()['sqlContextSingletonInstance'] = SQLContext(sparkContext)
    return globals()['sqlContextSingletonInstance']



def process(time, rdd):
    print("========= %s =========" % str(time))
    try:
        # Get the singleton instance of SQLContext
        sqlContext = getSqlContextInstance(rdd.context)

        # Convert RDD[String] to RDD[Row] to DataFrame
        rowRdd = rdd.map(lambda w: Row(word=w))
        wordsDataFrame = sqlContext.createDataFrame(rowRdd)

        # Register as table
        wordsDataFrame.registerTempTable("words")

        # Do word count on table using SQL and print it
        wordCountsDataFrame = sqlContext.sql("select word, count(*) as total from words group by word")
        wordCountsDataFrame.show()
    except:
        pass

#--------------------------------------------------




if __name__ == '__main__':
	# PART 1) : BASIC STREAMING 
	# CONFIG
	# create a SparkContext object with 2 local threads
	# name it as "NetworkWordCount"
	sc = SparkContext('local[2]', 'NetworkWordCount')
	print (sc)
	# pass a SparkContect to a StreamingContext object 
	# with batch duration = e.g. 10s
	ssc = StreamingContext(sc, 10)
	# set where the data streaming will come from e.g. localhost:9999
	lines = ssc.socketTextStream('localhost', 9999)
	# split the 'lines' with a whitespace into a list of words
	words = lines.flatMap(lambda line: line.split(' '))
	# create a tuple of each word and 1 using 'map'
	# e.g. word_0 --> (word_0, 1)
	pairs = words.map(lambda word: (word, 1))
	# count the words using reduceByKey e.g. by 'word_0', 'word_1'
	word_counts = pairs.reduceByKey(lambda num1, num2: num1 + num2)
	# print elements of the RDD
	word_counts.pprint()
	print (word_counts)
	# in case just run on PART 1) 
	#ssc.start()
	#ssc.awaitTermination()  # Wait for the computation to terminate


	# PART 2) SPARK SQL IN STREAMING WINDOW 
	words.foreachRDD(process)

	ssc.start()
	ssc.awaitTermination()  # Wait for the computation to terminate









