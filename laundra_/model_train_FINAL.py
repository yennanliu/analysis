

##################################################################################
# simple clustering model with new data :  All_CustomersExcCorporateAccounts     #
#                                      	                                         #
##################################################################################


# analytics 
import pandas as pd, numpy as np
from collections import OrderedDict

# ml 
from sklearn import preprocessing
from sklearn import cluster, tree, decomposition
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO
from sklearn.metrics import silhouette_score
from sklearn.model_selection import KFold
from sklearn import linear_model, ensemble
from sklearn.cross_validation import  cross_val_score

#from data_prepare import *
from utility_data_preprocess import *
from utility_ML import *



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

	#param_dist = random_search_parameter()
	clf_ = tree.DecisionTreeClassifier()
	#print (param_dist)
	col_ = df_train.columns[1:-1]
	print ('Start Model Tuning......')
	# grid search 
	print ('grid search ....')
	ts_gs = run_gridsearch(df_train[col_],
	                   df_train['group'],
	                   clf_)
	print("\n-- Best Parameters:")
	for k, v in ts_gs.items():
		print("parameter: {:<20s} setting: {}".format(k, v))

	# test the retuned best parameters
	print("\n\n-- Testing best parameters [Grid]...")
	dt_ts_gs = tree.DecisionTreeClassifier(**ts_gs)
	scores = cross_val_score(dt_ts_gs, df_train[col_], df_train['group'], cv=10)
	print("mean: {:.3f} (std: {:.3f})".format(scores.mean(),
	                                          scores.std()),
	                                          end="\n\n" )
	dict_group_name = ['1st_high_value',
	                   '2nd_high_value',
	                   '1st_medium_value',
	                   '2nd_medium_value',
	                   'low_value',
	                   'low_value_churn',
	                   'already_churn']

	group_order = df_train.groupby('group')\
	                      .mean()\
	                      .sort_values('LTV',ascending=False)\
	                      .reset_index()
	print (group_order) 
	group_id_name = OrderedDict(zip(list(group_order.group),dict_group_name))
	df_train['group_name']= df_train['group'].map(group_id_name)
	df_train['group_id'] = df_train['group']
	save_user_profile_DB(df_train)
	print ('final output : ')
	print (df_train.head(10))
	return df_train, X_std



if __name__ == '__main__':
	train()












