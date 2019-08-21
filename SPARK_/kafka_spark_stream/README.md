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
```


```bash 
# launch spark stream pipeline digest kafka data 
# method 1)
spark-submit — packages org.apache.spark:spark-streaming-kafka-0–8_2.11:2.0.0 reciever-based_spark_stream.py localhost:9092 new_topic

# method 2)
spark-submit — packages org.apache.spark:spark-streaming-kafka-0–8_2.11:2.0.0 direct_spark_stream.py localhost:9092 new_topic

```