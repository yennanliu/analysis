# python 3 

# data prepare 
import pandas as pd, numpy as np 


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
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model


def train(df,model):
    df_ = df.copy()
    X = df_.iloc[:,1:5]
    y = df_.iloc[:,6:7]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    clf_ = model.fit(X_train, y_train)
    print ('test score :', model.score(X_test,y_test) )
    y_true = y_test
    y_pred = clf_.predict(X_test)
    print (confusion_matrix(y_true, y_pred))
    #print (clf_)
    return clf_
     

if __name__ == '__main__':

	clf_tree = tree.DecisionTreeRegressor()
	clf_rf = RandomForestClassifier()
	clf_logistic = linear_model.LogisticRegression(C=1e5)
	df_iris = load_data()

	for model in [clf_tree,clf_rf,clf_logistic]:
		model = train(df_iris,model )









