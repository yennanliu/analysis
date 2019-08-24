import time
import json
import boto3
import lazyreader
#import utility
from kafka.producer import KafkaProducer

def get_key(self, msg):
    """
    produces key for message to Kafka topic
    :type msg: dict     message for which to generate the key
    :rtype   : str      key that has to be of type bytes
    """
    msgwithkey = utility.add_block_fields(msg)
    if msgwithkey is None:
        return
    x, y = msgwithkey["block_lonid"], msgwithkey["block_latid"]
    return str((x*137+y)%77703).encode()


if __name__ == '__main__':
    s3 = boto3.client('s3')
    producer = KafkaProducer(bootstrap_servers="localhost:9092")
    obj = s3.get_object(Bucket='nyctaxitrip',
            Key="{}/{}".format('yellow_trip',
                               'yellow_tripdata_sample.csv'))
    lines = str(obj['Body'].read())
    for line in lines.split("\\n"):
        #print (line)
        print (json.dumps(line))
        producer.send("new_topic",
                      value=json.dumps(line),
                      key='key')
        time.sleep(0.1)