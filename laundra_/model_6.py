

##################################################################################
# simple clustering model with new data :  All_CustomersExcCorporateAccounts     #
#                                      	                                         #
##################################################################################


# analytics 
import pandas as pd, numpy as np
import seaborn  as sns 
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D


# ml 
from sklearn import preprocessing
from sklearn import cluster, tree, decomposition
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO
from sklearn.metrics import silhouette_score
from sklearn.model_selection import KFold
from sklearn import linear_model, ensemble

#from data_prepare import *
from utility_data_preprocess import *
from utility_ML import *



def data_clean(df):
    df_ = df.copy()
    df_ = df_[df_.Frequency > 1]
    return df_

# make customer Frequency (order count) = 1 as a group 
# make customer Frequency (order count) = 1  amd LTV = 0 (use voucher) as the other group 
def data_clean_(df):
    df_ = df.copy()
    df_ = df_[(df_.Frequency > 1) & (df_.LTV > 0)]
    return df_



def train():
	df = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/All_CustomersExcCorporateAccounts.csv')
	df = data_clean_(df)
	df['Recency'] = pd.to_datetime(df['Recency'])
	df['period_no_use'] = (pd.to_datetime('today') - df['Recency']).dt.days
	selected_col = ['customer_id', 'Frequency', 'LTV','period_no_use']
	df_ = df[selected_col]
	X = df_.iloc[:,1:].fillna(0)
	X_std = X.copy()
	df_train = df_.copy()
	# standardize 
	for i in X:
	    X_std[i] = preprocessing.scale(X_std[i])
	cluster_set = 7 
	kmean = cluster.KMeans(n_clusters=cluster_set, max_iter=300, random_state=4000)
	kmean.fit(X_std)
	X_std['group'] = kmean.labels_
	df_train['group'] = kmean.labels_
	#print (X_std)
	#############

	# print classify results as table 
	print ('')
	print ('')
	print ('###### clustering mean  ######')
	group_outcome = df_train.groupby('group').mean()  
	group_user_count =  df_train.groupby('group').count()['customer_id'].reset_index().set_index('group')
	group_user_count.columns = ['group_user_count']
	group_outcome_ = group_outcome.join(group_user_count, how='inner')
	print (group_outcome_.iloc[:,1:])
	print ('')
	print ('###### clustering median  ######')
	group_outcome = df_train.groupby('group').median()  
	group_user_count =  df_train.groupby('group').count()['customer_id'].reset_index().set_index('group')
	group_user_count.columns = ['group_user_count']
	group_outcome_ = group_outcome.join(group_user_count, how='inner')
	print (group_outcome_.iloc[:,1:])
	print ('')
	print ('')

	#############
	# PCA
	# plot number of pricipal elments VS explained variance
	#pca = decomposition.PCA(n_components=10, whiten=True)
	#pca.fit(X_std)
	#fig, ax = plt.subplots(figsize=(14, 5))
	#sns.set(font_scale=1)
	#plt.step(range(10), pca.explained_variance_ratio_.cumsum())
	#plt.ylabel('Explained variance', fontsize = 14)
	#plt.xlabel('Principal components', fontsize = 14)
	#plt.legend(loc='upper left', fontsize = 13)
	#plt.show()

	# PCA plot 
	# use 2 pricipal elments
	from matplotlib import colors
	plt.style.use('classic')
	#colorlist = list(colors.ColorConverter.colors.keys())
	colorlist = ['k', 'red', 'g', 'c', 'b', 'm', 'y', 'r']
	pca = decomposition.PCA(n_components=2, whiten=True)
	pca.fit(X_std)
	X_std['x'] = pca.fit_transform(X_std)[:, 0]
	X_std['y'] = pca.fit_transform(X_std)[:, 1]
	for k, group in enumerate(set(X_std.group)):
	    plt.scatter(X_std[X_std.group == group]['x'],
	                X_std[X_std.group == group ]['y'],
	                label = group,
	                color=colorlist[k %len(colorlist)])
	plt.xlabel('main variable 1')
	plt.ylabel('main variable 2')
	plt.title('Customer RFM Clustering (PCA)')
	plt.legend()
	plt.show()
	# 3D plot 
	fig = pyplot.figure()
	ax = Axes3D(fig)
	for k, group in enumerate(set(df_train.group)):
	    ax.scatter(df_train[df_train.group == group]['Frequency'],
	               df_train[df_train.group == group ]['LTV'],
	               df_train[df_train.group == group ]['period_no_use'],
	               label = group,
	               color=colorlist[k %len(colorlist)])

	#ax.scatter(df_train.Frequency, df_train.LTV, df_train.period_no_use,c=df_train.group)
	plt.legend(loc='upper left')
	ax.set_xlabel('Frequency')
	ax.set_ylabel('LTV')
	ax.set_zlabel('period_no_use')
	plt.title('Customer RFM variables ')
	pyplot.show()

	return df_train, X_std










if __name__ == '__main__':
	train()












