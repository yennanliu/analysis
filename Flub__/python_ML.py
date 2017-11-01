
# python 3 

import pandas as pd 
import numpy as np 

from sklearn import preprocessing
from sklearn import cluster



def load_file():
	txt_route='/Users/yennanliu/analysis/Flub__'
	f=open(txt_route + '/cluster_data.txt',"r")
	lines=f.readlines()
	col1=[]
	col2=[]
	for x in lines:
		col1.append(x.split(' ')[0])
		col2.append(x.split(' ')[1].replace('\n',''))
	f.close()
	df_cluster_data = pd.DataFrame()
	df_cluster_data['x'] = col1
	df_cluster_data['y'] = col2
	print (df_cluster_data.head())
	return df_cluster_data


def data_preprocess(df):
	X_std = df.copy()
	X = X_std.columns
	for i in X:
		X_std[i] = preprocessing.scale(X_std[i])
	#print (X_std)
	return X_std

def model_1():
	df = load_file()
	X_std = data_preprocess(df)
	print ('kmeans modeling ')
	kmean = cluster.KMeans(n_clusters=2)
	kmean.fit(X_std) 
	X_std['group'] = kmean.labels_
	print (X_std.head())

def model_2():
	pass 


def model_3():
	pass 


if __name__ == '__main__':
	#df = load_file()
	#print ('re-scale data ')
	#data_preprocess(df)
	model_1()



