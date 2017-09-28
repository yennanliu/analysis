# python 3 

# data prepare 
import pandas as pd, numpy as np 
import sys


def species_encode(x):
    if x == 'Iris-virginica':
        return 0 
    if x == 'Iris-setosa':
        return 1 
    if x == 'Iris-versicolor':
        return 2

def load_data():
	df_iris = pd.read_csv('iris.csv')
	df_iris['species_'] =  df_iris.Species.map(lambda x : species_encode(x))
	return df_iris


# ML 

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score



def train(df,model):
    df_ = df.copy()
    X = df_.iloc[:,1:5]
    y = df_.iloc[:,6:7]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf_ = model.fit(X_train, y_train)
    print ('test score :', model.score(X_test,y_test) )
    y_true = y_test
    y_pred = clf_.predict(X_test)
    print ('-------------------')
    print ('confusion matrix : ')
    print (confusion_matrix(y_true, y_pred))
    print ('-------------------')
    print ('classification report  : ')
    print (classification_report(y_true, y_pred))
    #print (clf_)
    return clf_


def train_multiple_model():
	from sklearn import model_selection
	from sklearn.linear_model import LogisticRegression
	from sklearn.neighbors import KNeighborsClassifier
	from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
	from sklearn.naive_bayes import GaussianNB
	from sklearn.svm import SVC
	seed = 7
	scoring = 'accuracy'
	df_iris = load_data()
	df_iris_ = df_iris.copy()
	X = df_iris_.iloc[:,1:5]
	y = df_iris_.iloc[:,6:7]
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
	models = []
	models.append(('LR', LogisticRegression()))
	models.append(('LDA', LinearDiscriminantAnalysis()))
	models.append(('KNN', KNeighborsClassifier()))
	models.append(('CART', DecisionTreeClassifier()))
	models.append(('NB', GaussianNB()))
	models.append(('SVM', SVC()))
	# evaluate each model in turn
	results = []
	names = []
	for name, model in models:
		kfold = model_selection.KFold(n_splits=10, random_state=seed)
		cv_results = model_selection.cross_val_score(model, X_train,y_train, cv=kfold, scoring=scoring)
		results.append(cv_results)
		names.append(name)
		msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
		print ('-------------------')
		print(msg)
		print ('-------------------')


#def predict_(model, **kwargs):
#	pass 

def predict():
	if len(sys.argv[1:]) != 4:
		print ('plz enter iris parameters for species peediction with form : "SepalLengthCm"  "SepalWidthCm" "PetalLengthCm" "PetalWidthCm"')
		# e.g. python predict.py 1 2 3 4 
		# output : 
	else:
		df_iris = load_data()
		clf_tree = DecisionTreeClassifier()
		train(df_iris,clf_tree)
		print (sys.argv[1:])
		print (clf_tree.predict(sys.argv[1:]))

#def test():
#	#for arg in sys.argv: 
#	#	print (arg)
#	print (sys.argv[1:])




if __name__ == '__main__':

	predict()
	"""
	clf_tree = tree.DecisionTreeRegressor()
	clf_rf = RandomForestClassifier()
	clf_logistic = linear_model.LogisticRegression(C=1e5)
	df_iris = load_data()

	for model in [clf_tree,clf_rf,clf_logistic]:
		model = train(df_iris,model )
	"""
	#train_multiple_model()









