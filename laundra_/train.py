# python 3 


import pandas as pd, numpy as np
from sklearn import cluster

from prepare import *




# ML 

def train():

	df = load_data()
	df_ = data_preprocess(df)
	df_ = order_value_feature(df_)
	df_ = time_feature(df_)
	df_ = label_feature(df_)
	df_train = finalize_user_profile(df_)
	X = df_train.iloc[:,1:].fillna(0)
	kmean = cluster.KMeans(n_clusters=10, max_iter=300, random_state=None)
	kmean.fit(X)
	df_train['group'] = kmean.labels_
	print (df_train)



if __name__ == '__main__':
	train()










