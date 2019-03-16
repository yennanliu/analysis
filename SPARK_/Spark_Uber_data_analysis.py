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
	dataFrame.show()
	return dataFrame


def filter_batch_drive(dataFrame):
	spark_RDD = dataFrame.rdd
	digested_RDD = spark_RDD.map(
					lambda x: Row(
					author_ip = x['trips'],
					timestamp = x['date']))\
				.take(30)
	print (digested_RDD) 


if __name__ == '__main__':
	dataFrame = load_csv()
	filter_batch_drive(dataFrame)




