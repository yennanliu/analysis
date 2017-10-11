# python 3 

# analytics 
import pandas as pd, numpy as np
# ml 
from sklearn import preprocessing
from sklearn import cluster, tree, decomposition
from prepare import *

import seaborn  as sns 
import matplotlib.pyplot as plt
plt.style.use('classic')


# ML 

def train():

	df = load_data()
	df_ = data_preprocess(df)
	df_ = order_value_feature(df_)
	df_ = time_feature(df_)
	df_ = label_feature(df_)
	df_train = finalize_user_profile(df_)
	df_train = data_clean(df_train)

	# get train set 
	X = df_train.iloc[:,1:].fillna(0)
	X_std = X.copy()
	# standardize 
	for i in X:
 		X_std[i] = preprocessing.scale(X_std[i])
    # kmeans 
	kmean = cluster.KMeans(n_clusters=5, max_iter=300, random_state=None)
	kmean.fit(X_std)
	X_std['group'] = kmean.labels_
	print (X_std)

	# PCA
	pca = decomposition.PCA(n_components=2, whiten=True)
	pca.fit(X_std)
	X_std['x'] = pca.fit_transform(X_std)[:, 0]
	X_std['y'] = pca.fit_transform(X_std)[:, 1]
	plt.scatter(X_std['x'], X_std['y'],c = X_std.group)
	plt.show()



if __name__ == '__main__':
	train()










