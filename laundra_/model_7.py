
# python 3 

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
from utility_analysis import * 
from utility_ML import *




def train():
	df = load_all_data().load_user_RFM_data()
	df = data_cleaning(df).data_clean_freq0_LTV0()
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
	# kmeans clustering 
	kmean = cluster.KMeans(n_clusters=7, max_iter=300, random_state=4000)
	kmean.fit(X_std)
	# add lebel to user table 
	X_std['group'] = kmean.labels_
	df_train['group'] = kmean.labels_
	# print classify results as table 
	print ('###### clustering mean  ######')
	group_outcome_ = cluster_stas(df_train,'mean')
	print (group_outcome_.iloc[:,1:])
	print ('')
	print ('###### clustering median  ######')
	group_outcome_ = cluster_stas(df_train,'median')
	print (group_outcome_.iloc[:,1:])
	#param_dist = random_search_parameter()
	clf_ = tree.DecisionTreeClassifier()
	#print (param_dist)
	col_ = df_train.columns[1:-1]
	"""
	print ('Start Model Tuning......')
	# grid search 
	print ('grid search ....')
	ts_gs = run_gridsearch(df_train[col_],df_train['group'],clf_)
	print("\n-- Best Parameters:")
	for k, v in ts_gs.items():
		print("parameter: {:<20s} setting: {}".format(k, v))

	# test the retuned best parameters
	print("\n\n-- Testing best parameters [Grid]...")
	dt_ts_gs = tree.DecisionTreeClassifier(**ts_gs)
	scores = cross_val_score(dt_ts_gs, df_train[col_], df_train['group'], cv=10)
	print("mean: {:.3f} (std: {:.3f})".format(scores.mean(),scores.std()),end="\n\n" )
	"""
	# map group id to group name 
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
	# merge with 1 order, and > 1 order 0 LTV group 
	one_order_zero_LTV_user = get_1_order_0_LTV_user()
	df_train  = pd.concat([df_train,one_order_zero_LTV_user], axis=0)
	# merge with remaining dataset 
	ATO, CityPostcode, Latebycollectionanddelivery, NoofTickets, RecleanedOrders, cancalledOrders, voucherused = load_all_data().load_other_data()
	#list_to_merge = [ATO, CityPostcode, Latebycollectionanddelivery, NoofTickets, RecleanedOrders, cancalledOrders, voucherused]
	df_train_ = pd.merge(df_train,ATO,on='customer_id',how='left')
	df_train_ = pd.merge(df_train_,CityPostcode,on='customer_id',how='left')
	df_train_ = pd.merge(df_train_,Latebycollectionanddelivery,on='customer_id',how='left')
	df_train_ = pd.merge(df_train_,NoofTickets,on='customer_id',how='left')
	df_train_ = pd.merge(df_train_,RecleanedOrders,on='customer_id',how='left')
	df_train_ = pd.merge(df_train_,cancalledOrders,on='customer_id',how='left')
	df_train_ = pd.merge(df_train_,voucherused,on='customer_id',how='left')
	# merge 1 order and > 1 order 0 LTV group 
	#df_train_ = pd.merge(df_train_,one_order_user,on='customer_id',how='left')
	#df_train_ = pd.merge(df_train_,more_one_order_zero_LTV_user,on='customer_id',how='left')
	# save output 
	save_user_profile_DB(df_train_)
	print ('final output : ')
	print (df_train_.head(10))
	print (df_train_.groupby('group_name').count())

	return df_train_, X_std


def get_1_order_0_LTV_user():
	df = load_all_data().load_user_RFM_data()
	# get 1 order group
	#one_order_user = df[df.Frequency == 1 ]
	# get > 1 order 0 LTV group 
	#more_one_order_zero_LTV_user = df[(df.Frequency > 1) & (df.LTV == 0) ]
	#
	one_order_zero_LTV_user = df[ (df.Frequency == 1 )
								| ((df.Frequency > 1) & (df.LTV == 0)) ]

	one_order_zero_LTV_user['Recency'] = pd.to_datetime(one_order_zero_LTV_user['Recency'])
	one_order_zero_LTV_user['period_no_use'] = (pd.to_datetime('today') - one_order_zero_LTV_user['Recency']).dt.days
	#one_order_zero_LTV_user['group_name'] =  ['one_order_user' if  x == 1   for x in one_order_zero_LTV_user.Frequency ]
	one_order_zero_LTV_user.loc[:,'group_name'] = one_order_zero_LTV_user.apply(one_order_zero_LTV_label, axis = 1)
	#print (one_order_zero_LTV_user.head())
	#print (one_order_zero_LTV_user[one_order_zero_LTV_user.group_name == 'one_order_user'].head())
	#print (one_order_zero_LTV_user[one_order_zero_LTV_user.group_name == 'more_one_order_zero_LTV_user'].head())
	return one_order_zero_LTV_user



def one_order_zero_LTV_label(row):
	if  row.Frequency == 1:
		return 'one_order_user'
	if (row.Frequency > 1) and (row.LTV == 0 ):
		return 'more_one_order_zero_LTV_user'
	else:
		pass 



if __name__ == '__main__':
	#get_1_order_0_LTV_user()
	train()












