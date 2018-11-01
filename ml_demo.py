# python 3 
# OP 
from datetime import datetime, timedelta
import pandas as pd, numpy as np
# ML 
from sklearn.datasets import load_boston
from sklearn import datasets, linear_model


def main():
	boston = load_boston()
	df = pd.DataFrame(boston.data, columns=boston.feature_names)
	df['target'] = boston.target
	X = df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX','PTRATIO', 'B', 'LSTAT']]
	Y = np.array(df['target']).astype(int)
	regr = linear_model.LinearRegression()
	regr.fit(X, Y)
	print (pd.DataFrame({'predict':regr.predict(X), 'actual':Y, 'error':Y - regr.predict(X)}))
	print ('score :', regr.score(X,Y))
	print ('intercept_ : ' , regr.fit(X, Y).intercept_, '\n', 'coef_ : ', regr.fit(X, Y).coef_)



if __name__ == '__main__':
	main()
