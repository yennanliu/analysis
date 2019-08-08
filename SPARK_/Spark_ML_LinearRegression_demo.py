# python 3 
# https://docs.databricks.com/getting-started/spark/machine-learning.html

# OP
from sklearn.datasets import load_boston
from sklearn.preprocessing import scale
import pandas as pd 
# spark 
from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext
from pyspark.ml import Pipeline
from pyspark.ml.feature import  VectorIndexer
from pyspark.ml.linalg import Vectors
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator

conf = SparkConf().setAppName("building a LINEAR MODEL")
sc = SparkContext(conf=conf)
sqlCtx = SQLContext(sc)

# LOAD THE DATA 
total_features, total_prices = load_boston(True)
col_list = load_boston()['feature_names']

df = pd.DataFrame(total_features)
df.columns = col_list
df['price'] = total_prices
print (df.head()) 

# save to csv 
df.to_csv('boston.csv',index=False)


# load data with spark way
data = sc.textFile('boston.csv').map(lambda line: line.split(","))
headers = data.first()
traindata = data.filter(lambda row: row != headers)
sqlContext = SQLContext(sc)
dataFrame = sqlContext.createDataFrame(traindata, ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT', 'price'])
dataFrame.take(2)
print ('-'*70)
print (dataFrame.take(30))
print ('-'*70)
# convert string to float in  PYSPARK

# https://stackoverflow.com/questions/46956026/how-to-convert-column-with-string-type-to-int-form-in-pyspark-data-frame
#for col in df.columns:
#	dataFrame = dataFrame.withColumn("{}".format(), dataFrame[col].cast("float"))
dataFrame = dataFrame.withColumn("CRIM_", dataFrame["CRIM"].cast("float"))
dataFrame = dataFrame.withColumn("ZN_", dataFrame["ZN"].cast("float"))
dataFrame = dataFrame.withColumn("price_", dataFrame["price"].cast("float"))
dataFrame.registerTempTable("temp_sql_table")
spark_sql_output=sqlContext.sql("""SELECT 
                    CRIM_,
                    ZN_,
                    price_
                    FROM temp_sql_table """)
print (spark_sql_output.take(10))

trainingData=spark_sql_output.rdd.map(lambda x:(Vectors.dense(x[0:-1]), x[-1])).toDF(["features", "label"])
trainingData.show()
featureIndexer =\
VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(trainingData)

(trainingData, testData) = trainingData.randomSplit([0.7, 0.3])

#################### SPARK ML  ####################

# Define LinearRegression algorithm
lr = LinearRegression()

# Fit 2 models, using different regularization parameters
modelA = lr.fit(trainingData, {lr.regParam:0.0})
modelB = lr.fit(trainingData, {lr.regParam:100.0})

# Make predictions
predictionsA = modelA.transform(trainingData)
print ('-'*70)
print ('MODEL A : ')
predictionsA.select("prediction", "label", "features").show(30)
print ('-'*70)

predictionsB = modelB.transform(trainingData)
print ('-'*70)
print ('MODEL B : ')
predictionsB.select("prediction", "label", "features").show(30)
print ('-'*70)

# Evaluate the model
evaluator = RegressionEvaluator(metricName="rmse")
RMSE = evaluator.evaluate(predictionsA)
print ('-'*70)
print("ModelA: Root Mean Squared Error = " + str(RMSE))
print ('-'*70)
# ModelA: Root Mean Squared Error = 128.602026843

RMSE = evaluator.evaluate(predictionsB)
print ('-'*70)
print("ModelB: Root Mean Squared Error = " + str(RMSE))
print ('-'*70)
# ModelB: Root Mean Squared Error = 129.496300193