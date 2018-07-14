# python 3 
# load library 
# op 
import pandas as pd
import numpy as np
# ML 
from sklearn.cross_validation import train_test_split, KFold, cross_val_score
from sklearn.feature_selection import RFE, f_regression
from sklearn.linear_model import (LinearRegression, Ridge, Lasso, RandomizedLasso)
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score


# help function 
# ---------------------------------
# OP 

def load_data():
	df = pd.read_csv('kc_house_data.csv')
	return df 

def get_linearmodel_col(df):
    cols = ['price',
            'sqft_living',
            'sqft_lot',
            'sqft_above',
            'sqft_basement']
    return df[cols]

def data_clean(df):
    pass

def get_train_test_set(df):
    X = df[['sqft_living',
         'sqft_lot',
         'sqft_above',
         'sqft_basement']]
    y = df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    return X_train,y_train, X_test, y_test
    
# ---------------------------------


# ML 

def linear_model(X_train,y_train,X_test,y_test,model):
    model.fit(X_train,y_train)
    y_test_predict = model.predict(X_test)
    print ('--- mean_squared_error --- ')
    print (mean_squared_error(y_test_predict, y_test))
    print ('--- r2_score --- ')
    print (r2_score(y_test_predict, y_test))
    return y_test_predict 

# ---------------------------------
if __name__ == '__main__':
	df = load_data()
	df_ = get_linearmodel_col(df)
	X_train,y_train, X_test, y_test = get_train_test_set(df_)
	model_ = [ LinearRegression(),Ridge(), Lasso()]
	for model in model_:
		print ('')
		print ('* model : ', model)
		print ('')
		y_predict = linear_model( X_train,y_train, X_test, y_test, model)











