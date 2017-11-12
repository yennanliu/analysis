# python 2.7 


# analysis 
import pandas as pd, numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
# spark 
from pyspark.mllib.tree import RandomForest
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark import SparkContext
sc =SparkContext()

def main():
	## Data
	iris = datasets.load_iris()
	X = iris.data
	Y = iris.target
	data = map(lambda (x,y): LabeledPoint(y, x), zip(X, Y))
	## Modelling
	model = RandomForest.trainClassifier(sc.parallelize(data), 3, {}, 3, seed=42)
	## Prediction
	preds = [model.predict(_) for _ in X]
	## Accuracy
	print(sum(preds == Y) * 1.0/ len(Y))



if __name__ == '__main__':
	main()





