# run step by step in jupyter notebook 
# ref : https://jupyter-docker-stacks.readthedocs.io/en/latest/using/recipes.html#spark

if __name__ == '__main__':
    import os
    os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars /home/jerryliu/spark/jars/spark-streaming-kafka-0-8-assembly_2.11-2.4.3.jar pyspark-shell'
    import pyspark
    from pyspark.streaming.kafka import KafkaUtils
    from pyspark.streaming import StreamingContext
    #sc = pyspark.SparkContext()
    ssc = StreamingContext(sc,1)
    broker = "127.0.0.1:9092"
    directKafkaStream = KafkaUtils.createDirectStream(ssc, ["new_topic"], {"metadata.broker.list": broker})
    directKafkaStream.pprint()
    ssc.start()