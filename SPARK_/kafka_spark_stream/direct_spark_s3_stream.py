import sys
from pyspark import SparkConf,SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql.session import SparkSession

if __name__ == "__main__":
    # use conf to avoid lz4 exception when reading data from kafka using spark streaming
    # https://stackoverflow.com/questions/51479474/lz4-exception-when-reading-data-from-kafka-using-spark-streaming
    conf = SparkConf().setAppName("PythonStreamingDirectKafkaWordCount").set('spark.io.compression.codec','snappy')
    sc = SparkContext.getOrCreate(conf=conf)
    ssc = StreamingContext(sc, 2)
    spark = SparkSession(sc)
    brokers, topic = sys.argv[1:]
    kafkaStream = KafkaUtils.createDirectStream(ssc, [topic],{"metadata.broker.list": brokers})
    # >>> apporach 1 
    lines = kafkaStream.map(lambda x: x[1])
    counts = lines.flatMap(lambda line: line.split("\n")) \
                  .map(lambda word: ( float(word[0]), float(word[0]))) \
                  .reduceByKey(lambda a, b: a*b)
    counts.pprint() 

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