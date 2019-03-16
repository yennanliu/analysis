# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession, Row
# python op 
import pandas as pd


# config 
conf = SparkConf().setAppName("load UBER data")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)
spark = SparkSession.builder.enableHiveSupport().getOrCreate()


def load_csv():
	# load the csv data as spark df 
	data = sc.textFile("uber_data/Uber-Jan-Feb-FOIL.csv").map(lambda line: line.split(","))
	headers = data.first()
	traindata = data.filter(lambda row: row != headers)
	sqlContext = SQLContext(sc)
	dataFrame = sqlContext.createDataFrame(traindata, ['dispatching_base_number', 'date', 'active_vehicles', 'trips'])
	dataFrame = dataFrame.withColumn("date_", dataFrame["date"].cast("timestamp"))
	dataFrame = dataFrame.withColumn("trips", dataFrame["trips"].cast("float"))
	dataFrame = dataFrame.withColumn("active_vehicles", dataFrame["active_vehicles"].cast("float"))
	dataFrame.show()
	print (dataFrame.printSchema())
	return dataFrame


def filter_batch_drive(dataFrame):
	spark_RDD = dataFrame.rdd
	digested_RDD = spark_RDD.map(
	lambda x: Row(
		trips = x['trips'],
		dispatching_number = x['dispatching_base_number'],
		timestamp = x['date']))\
		.filter(lambda x : x['dispatching_number'] == 'B02765')\
		.take(30)
	print (digested_RDD) 

def group_by_batch_drive(dataFrame):
	dataFrame.groupby('dispatching_base_number').count().show()
	dataFrame.groupby('dispatching_base_number').sum().show()



if __name__ == '__main__':
	dataFrame = load_csv()
	filter_batch_drive(dataFrame)
	group_by_batch_drive(dataFrame)




