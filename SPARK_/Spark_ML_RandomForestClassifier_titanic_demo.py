# python 3 
# credit :  https://creativedata.atlassian.net/wiki/spaces/SAP/pages/83237142/Pyspark+-+Tutorial+based+on+Titanic+Dataset

# Import packages
import time
import pyspark
import os
import csv
from numpy import array
from pyspark.mllib.regression import LabeledPoint
from pyspark import SparkContext, SparkConf

# configue Spark env
os.environ["HADOOP_USER_NAME"] = "hdfs"
os.environ["PYTHON_VERSION"] = "3.5.2"
conf = pyspark.SparkConf()
sc = pyspark.SparkContext(conf=conf)
conf.getAll()

# Reading from the hdfs, removing the header
# read the titanic train, test csv here 
trainTitanic = sc.textFile("titanic_train.csv")
# remove the header 
trainHeader = trainTitanic.first()
trainTitanic = trainTitanic.filter(lambda line: line != trainHeader).mapPartitions(lambda x: csv.reader(x))
trainTitanic.first()
 
# Data preprocessing
def sexTransformMapper(elem):
    '''Function which transform "male" into 1 and else things into 0
    - elem : string
    - return : vector
    '''
     
    if elem == 'male' :
        return [0]
    else :
        return [1]
 
# Data Transformations and filter lines with empty strings
trainTitanic=trainTitanic.map(lambda line: line[1:3]+sexTransformMapper(line[4])+line[5:11])
trainTitanic=trainTitanic.filter(lambda line: line[3] != '' ).filter(lambda line: line[4] != '' )
trainTitanic.take(10)
 
# creating "labeled point" rdds specific to MLlib "(label (v1, v2...vp])"
trainTitanicLP=trainTitanic.map(lambda line: LabeledPoint(line[0],[line[1:5]]))
trainTitanicLP.first()
 
# splitting dataset into train and test set
# 70% train, 30% test 
(trainData, testData) = trainTitanicLP.randomSplit([0.7, 0.3])
 
# Random forest : same parameters as sklearn (?)
from pyspark.mllib.tree import RandomForest
 
time_start=time.time()
model_rf = RandomForest.trainClassifier(trainData, numClasses = 2,
        categoricalFeaturesInfo = {}, numTrees = 100,
        featureSubsetStrategy='auto', impurity='gini', maxDepth=12,
        maxBins=32, seed=None)
 
  
model_rf.numTrees()
model_rf.totalNumNodes()
time_end=time.time()
time_rf=(time_end - time_start)
print("RF takes %d s" %(time_rf))
 
# Predictions on test set
predictions = model_rf.predict(testData.map(lambda x: x.features))
labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
 
# first metrics
from pyspark.mllib.evaluation import BinaryClassificationMetrics
metrics = BinaryClassificationMetrics(labelsAndPredictions)
 
print ('=====================================================')
print (' output : ')


# Area under precision-recall curve
print("Area under PR = %s" % metrics.areaUnderPR)
 
# Area under ROC curve
print("Area under ROC = %s" % metrics.areaUnderROC)

print ('=====================================================')
