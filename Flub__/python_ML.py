
# python 3 
# analysis 
import pandas as pd 
import numpy as np 
import seaborn  as sns 
import matplotlib.pyplot as plt
from matplotlib import pyplot

# ml 
from sklearn import preprocessing, cluster, mixture


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
	# Kmeans  
	print ('kmeans clustering ')
	kmean = cluster.KMeans(n_clusters=2)
	kmean.fit(X_std) 
	X_std['group'] = kmean.labels_
	# plot 
	print (X_std.head())
	plt.scatter(X_std.x, X_std.y ,c=X_std.group)
	plt.show()

def model_2():
	df = load_file()
	X_std = data_preprocess(df)
	# Gaussian Mixture Models   
	print ('GMM clustering ')
	gmm = mixture.GaussianMixture(2, covariance_type='full')
	gmm.fit(X_std)
	labels = gmm.predict(X_std)
	X_std['group'] = labels
	# plot 
	print (X_std.head())
	plt.scatter(X_std.x, X_std.y ,c=X_std.group)
	plt.show()



def model_3():
	df = load_file()
	X_std = data_preprocess(df)
	# AgglomerativeClustering
	print ('hierarchical clustering ')
	h_clustering = cluster.AgglomerativeClustering()
	h_clustering.fit(X_std) 
	X_std['group'] = h_clustering.labels_
	# plot 
	print (X_std.head())
	plt.scatter(X_std.x, X_std.y ,c=X_std.group)
	plt.show()



if __name__ == '__main__':
	#df = load_file()
	#print ('re-scale data ')
	#data_preprocess(df)
	model_3()



