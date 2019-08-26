import sys
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.session import SparkSession
from pyspark.sql import Row
from pyspark.ml.linalg import Vectors

def f(x):
    d = {}
    for i in range(len(x)):
        d[str(i)] = x[i]
    return d

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
        taxiDataFrame = spark.createDataFrame(rowRdd)

        # Creates a temporary view using the DataFrame
        taxiDataFrame.createOrReplaceTempView("taxi")

        # Do word count on table using SQL and print it
        query="""
        SELECT word[0] AS vendor_name,
               word[1] AS Trip_Pickup_DateTime,
               word[2] AS Trip_Dropoff_DateTime,
               word[3] AS Passenger_Count,
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
        FROM taxi
        """
        taxiQueryDataFrame = spark.sql(query)
        print (">>>>>>>> RESULT OF wordCountsDataFrame")
        taxiQueryDataFrame.show()
        taxidf =taxiQueryDataFrame.rdd.map(lambda x:x).toDF(
                ['vendor_name','Trip_Pickup_DateTime', 'Trip_Dropoff_DateTime',
                'Passenger_Count','Trip_Distance','Start_Lon',
                'Start_Lat','Rate_Code','store_and_forward',
                'End_Lon','End_Lat','Payment_Type',
                'Fare_Amt','surcharge','mta_tax',
                'Tip_Amt','Tolls_Amt','Total_Amt'])
        print('taxidf :', taxidf.collect())
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