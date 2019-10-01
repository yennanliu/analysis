# python 3 




########################################  
# simple clustering model with k-fold   #
#                                      	#
########################################

# analytics 
import pandas as pd, numpy as np
import seaborn  as sns 
import matplotlib.pyplot as plt


# ml 
from sklearn import preprocessing
from sklearn import cluster, tree, decomposition
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO
from sklearn.metrics import silhouette_score
from sklearn.model_selection import KFold
from sklearn import linear_model, ensemble



#
#from data_prepare import *
from utility_data_preprocess import *
from utility_ML import *

plt.style.use('classic')


# ML 

# k-fold train 
def train_():

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
	# fix random_state here for same results (in dev)(same starting point)
	### but will make random_state = None (in product), since random intitial state can always give better results 
	kmean = cluster.KMeans(n_clusters=9, max_iter=300, random_state=4000)
	kmean.fit(X_std)
	X_std['group'] = kmean.labels_
	df_train['group'] = kmean.labels_
	print (X_std)
	#############
	# print classify results as table 
	group_outcome = df_train.groupby('group').mean()  
	group_user_count =  df_train.groupby('group').count()['customer_id'].reset_index().set_index('group')
	group_user_count.columns = ['group_user_count']
	group_outcome_ = group_outcome.join(group_user_count, how='inner')
	print (group_outcome_.iloc[:,1:])

	##### k - fold train #####
	k_fold_columns = [ 'order_count', 'sum_original_value',
	   'sum_discount_value', 'sum_spend_value', 'avg_original_value',
	   'avg_discount_value', 'avg_spend_value', 'using_period', 'user_period',
	   'period_no_use', 'platform_']
	df_train__ = df_train.dropna()
	xtrain = df_train__[k_fold_columns]
	ytrain = df_train__['group']
	# logistics 
	print ('logistics ')
	logistics =  linear_model.LogisticRegression
	logistics_ = Class_train(clf = logistics) 
	logistics_.k_fold_train(KFold_ = 10 , x_train = xtrain,y_train = ytrain)
	# RF 
	print ('RF ')
	RF_ = Class_train(clf = ensemble.RandomForestClassifier)
	RF_.k_fold_train(KFold_ = 10 , x_train = xtrain,y_train = ytrain)











if __name__ == '__main__':
	train_()










