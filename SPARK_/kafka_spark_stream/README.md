### Quick start

```bash 
# set up kafka 
# launch zookeeper and kafka
brew services start zookeeper
brew services start kafka
# step 1)
echo “this is just a test” | kafka-console-producer --broker-list localhost:9092 --topic new_topic

# step 2)
kafka-console-consumer  --bootstrap-server 127.0.0.1:9092 --topic new_topic 

# step 3)
kafka-console-consumer  --bootstrap-server  127.0.0.1:9092 --topic new_topic  --from-beginning 

# launch spark stream pipeline digest kafka data 
# method 1)
spark-submit --jars /Users/$USER/spark/jars/spark-streaming-kafka-0-8-assembly_2.11-2.4.3.jar reciever-based_spark_stream.py localhost:9092 new_topic


# method 2)
spark-submit --jars /Users/$USER/spark/jars/spark-streaming-kafka-0-8-assembly_2.11-2.4.3.jar direct_spark_stream.py localhost:9092 new_topic

```

```python  
# run step by step in jupyter notebook 
import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--jars /home/jerryliu/spark/jars/spark-streaming-kafka-0-8-assembly_2.11-2.4.3.jar pyspark-shell'
import pyspark
from pyspark.streaming.kafka import KafkaUtils
from pyspark.streaming import StreamingContext
sc = pyspark.SparkContext.getOrCreate()
ssc = StreamingContext(sc,1)
broker = "127.0.0.1:9092"
directKafkaStream = KafkaUtils.createDirectStream(ssc, ["new_topic"], {"metadata.broker.list": broker})
directKafkaStream.pprint()
ssc.start()
```

### Package download 
- [spark-streaming-kafka-0-8-assembly_2.11-2.4.3.jar](https://mvnrepository.com/artifact/org.apache.spark/spark-streaming-kafka-0-8-assembly_2.11/2.4.3)

