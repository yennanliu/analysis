# python 2.7 


#  import pyspark library 
from pyspark import SparkConf, SparkContext
from spark_sklearn import GridSearchCV
# import ML library
from sklearn import svm, grid_search, datasets


sc =SparkContext()


iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC()
clf = GridSearchCV(sc, svr, parameters)
clf.fit(iris.data, iris.target)
print ("==================")
print (clf.predict(iris.data))
print ("==================")