# python 3 



############################################################################################ 
# 
# REF 
# https://github.com/clumdee/Python-and-Spark-for-Big-Data-master/blob/master/Spark_Streaming/streaming_terminal_with_RDD.ipynb
# SPARK STREAM DEMO CODE  


#### before start this demo script
# open the other terminal run : 
# $ nc -lk 9999 ( start the localhost:9999, Start the streaming session to the localhost)
# and type sth within that terminal
# i.e. 
# $ hello world 
# $ yall yay lol yyzzyy
# you should seed the spark stream get the session input and response as output 
############################################################################################ 


from pyspark import SparkContext
from pyspark.streaming import StreamingContext


if __name__ == '__main__':
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

	ssc.start()
	ssc.awaitTermination()  # Wait for the computation to terminate









