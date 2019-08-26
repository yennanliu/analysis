import sys
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.session import SparkSession
from pyspark.sql import Row

def getSparkSessionInstance(sparkConf):
    if ('sparkSessionSingletonInstance' not in globals()):
        globals()['sparkSessionSingletonInstance'] = SparkSession\
            .builder\
            .config(conf=sparkConf)\
            .getOrCreate()
    return globals()['sparkSessionSingletonInstance']

def stream_2_sql(time, rdd):
    """
    https://spark.apache.org/docs/2.1.1/streaming-programming-guide.html
    https://github.com/apache/spark/blob/v2.1.1/examples/src/main/python/streaming/sql_network_wordcount.py
    """
    print("========= %s =========" % str(time))
    try:
        # Get the singleton instance of SparkSession
        spark = getSparkSessionInstance(rdd.context.getConf())

        # Convert RDD[String] to RDD[Row] to DataFrame
        #rowRdd = rdd.map(lambda w: Row(word=[w[0], w[1]]))
        rowRdd = rdd.map(lambda w: Row(word=[w[:], w.split(',')[0], w.split(',')[1]]))
        #rowRdd = rdd.map(lambda w: Row(word=w[0]))
        wordsDataFrame = spark.createDataFrame(rowRdd)
        
        # Creates a temporary view using the DataFrame
        wordsDataFrame.createOrReplaceTempView("words")

        # Do word count on table using SQL and print it
        wordCountsDataFrame = spark.sql("select word as raw_data, word[1] as Passenger_Count ,word[2] as Trip_Pickup_DateTime  , count(*) as total from words group by 1,2,3")
        print (">>>>>>>> RESULT OF wordCountsDataFrame")
        wordCountsDataFrame.show()
    except Exception as e:
        print ( str(e), 'sth goes wrong')
        pass

if __name__ == "__main__":
    # use conf to avoid lz4 exception when reading data from kafka using spark streaming
    # https://stackoverflow.com/questions/51479474/lz4-exception-when-reading-data-from-kafka-using-spark-streaming
    conf = SparkConf().setAppName("PythonStreamingDirectKafkaWordCount").set('spark.io.compression.codec','snappy')
    sc = SparkContext.getOrCreate(conf=conf)
    ssc = StreamingContext(sc, 2)
    spark = SparkSession(sc)
    brokers, topic = sys.argv[1:]
    kafkaStream = KafkaUtils.createDirectStream(ssc, [topic],{"metadata.broker.list": brokers})

    lines = kafkaStream.map(lambda x: x[1])
    lines_ = lines.flatMap(lambda line: line.split("\n"))
    counts = lines.flatMap(lambda line: line.split(" ")) \
                  .map(lambda word: (word, 1)) \
                  .reduceByKey(lambda a, b: a+b)

    #counts.pprint()
    lines_.foreachRDD(stream_2_sql)

    # >>> apporach 1 
    # lines = kafkaStream.map(lambda x: x[1])
    # counts = lines.flatMap(lambda line: line.split("\n")) \
    #               .map(lambda word: ( float(word[0]), float(word[0]))) \
    #               .reduceByKey(lambda a, b: a*b)
    # counts.pprint() 

    # >>> apporach 2 
    # kafkaStream.foreachRDD(lambda rdd: rdd.foreachPartition())
    # kafkaStream.pprint()

    # >>> apporach 3 
    # ds1 = spark.readStream \
    #           .format("kafka") \
    #           .option("kafka.bootstrap.servers", "127.0.0.1:9092") \
    #           .option("subscribe", "new_topic") \
    #           .load()
    # ds1.selectExpr("CAST(Trip_Pickup_DateTime AS STRING)", "CAST(Passenger_Count AS STRING)")
    # ds1.pprint()
    ssc.start()
    ssc.awaitTermination()