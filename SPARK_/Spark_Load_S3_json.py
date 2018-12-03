


# OP
import pandas as pd 
import os 
import json
import requests

# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession

##### config #####
conf = SparkConf().setAppName("LOAD JSON")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)



### 1) -------------------- LOAD LOCAL JSON 
#demo_json={"header":{"platform":"atm","version":"2.0"},"details":[{"abc":"3","def":"4"},{"abc":"5","def":"6"},{"abc":"7","def":"8"}]}
df = sqlContext.read.json('demo.json')
print ('='*70)
print ( 'df type : ' , type(df))
print (df.first())
print ('='*70)
#df = df.flatMap(lambda row: row['details'])
print ('='*70)
print (df.collect())
print ('='*70)

#df.map(lambda entry: (int(entry['abc']),int(entry['def']))).collect()



### 2) -------------------- LOAD ONLINE JSON 
r = requests.get("https://jsonplaceholder.typicode.com/comments").json()
#df2 = sqlContext.createDataFrame([json.loads(line) for line in r.iter_lines()])
print ('='*70)
#print (df2.collect())
#http://docs.python-requests.org/en/master/user/quickstart/
print (r)
print ('='*70)






