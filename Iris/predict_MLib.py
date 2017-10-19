# python 2.7 


#  import pyspark library 
from pyspark import SparkConf, SparkContext

# spark_sklearn provides the same API as sklearn but uses Spark MLLib 
# under the hood to perform the actual computations in a distributed way 
# (passed in via the SparkContext instance).
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