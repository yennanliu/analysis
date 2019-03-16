# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, SparkSession, Row
from operator import add
# python op 
import pandas as pd
import numpy as np 

# config 
conf = SparkConf().setAppName("load UBER data")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)
spark = SparkSession.builder.enableHiveSupport().getOrCreate()

# ----------------------------------- FOIL CSV 
def load_FOIL_csv():
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

def get_batch_drive_count_dataFrame_groupby(dataFrame):
	dataFrame.groupby('dispatching_base_number').count().show()
	dataFrame.groupby('dispatching_base_number').sum().show()

def get_batch_drive_count_RDD_reducebykey(dataFrame):
	spark_RDD = dataFrame.rdd 
	top_batch = spark_RDD\
				.map(lambda x : (x.dispatching_base_number , 1))\
				.reduceByKey(add)\
				.sortBy(lambda x : x[1], False)\
				.take(30)
	print (top_batch)

def get_dispatch_list(dataFrame):
	spark_RDD = dataFrame.rdd
	dispatching_list = spark_RDD.map(
		lambda x : Row(
		dispatching_id = x['dispatching_base_number']))\
		.flatMap(lambda x : x)\
		.take(30)
	print (dispatching_list)

# ----------------------------------- TRIP CSV 
def load_all_trip_csv():
	# spark load multiple CSVs
	# https://stackoverflow.com/questions/37639956/how-to-import-multiple-csv-files-in-a-single-load
	all_trip_data = spark.read.format("csv").option("header", "true").load("uber_data/uber-raw-data-*.csv")
	all_trip_data.show()
	print (all_trip_data.count())
	return all_trip_data

def get_haversine_distance(lat1, lng1, lat2, lng2):
	# km
	lat1, lng1, lat2, lng2 = map(np.radians, (lat1, lng1, lat2, lng2))
	AVG_EARTH_RADIUS = 6371  #  km
	lat = lat2 - lat1
	lng = lng2 - lng1
	d = np.sin(lat * 0.5) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(lng * 0.5) ** 2
	h = 2 * AVG_EARTH_RADIUS * np.arcsin(np.sqrt(d))
	return h 

def get_filter_top_date(dataFrame):
	spark_RDD = dataFrame.rdd
	date_count = spark_RDD\
				.map(lambda x : (x['Date/Time'], 1))\
				.reduceByKey(add)\
				.sortBy(lambda x : x[1], False)\
				.take(30)
	print (date_count)

if __name__ == '__main__':
	# FOIL CSV 
	FOIL_dataFrame = load_FOIL_csv()
	filter_batch_drive(FOIL_dataFrame)
	get_batch_drive_count_dataFrame_groupby(FOIL_dataFrame)
	get_batch_drive_count_RDD_reducebykey(FOIL_dataFrame)
	get_dispatch_list(FOIL_dataFrame)
	# TRIP CSV
	all_trip_dataFrame = load_all_trip_csv()
	get_filter_top_date(all_trip_dataFrame)
