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
        rowRdd = rdd.map(lambda w: Row(word=[ i for i in w.split(',')[1:]]))
        #rowRdd = rdd.map(lambda w: Row(word=w[0]))
        wordsDataFrame = spark.createDataFrame(rowRdd)

        # Creates a temporary view using the DataFrame
        wordsDataFrame.createOrReplaceTempView("words")

        # Do word count on table using SQL and print it
        # query="""
        # select word[0] as Passenger_Count ,word[1] as Trip_Pickup_DateTime  , count(*) as total from words group by 1,2
        # """
        query="""
        SELECT 
        word[0] AS vendor_name,
        word[1] AS Trip_Pickup_DateTime,
        word[2] AS Trip_Dropoff_DateTime,
        word[3] AS Passenger_Count ,
        word[4] AS Trip_Distance,
        word[5] AS Start_Lon,
        word[6] AS Start_Lat,
        word[7] AS Rate_Code,
        word[8] AS store_and_forward,
        word[9] AS End_Lon,
        word[10] AS End_Lat,
        word[11] AS Payment_Type,
        word[12] AS Fare_Amt,
        word[13] AS surcharge,
        word[14] AS mta_tax,
        word[15] AS Tip_Amt,
        word[16] AS Tolls_Amt,
        word[17] AS Total_Amt
        FROM words
        """
        wordCountsDataFrame = spark.sql(query)
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
    lines_.foreachRDD(stream_2_sql)
    ssc.start()
    ssc.awaitTermination()