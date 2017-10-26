
# python 3 

import pandas as pd, numpy as np

import seaborn  as sns 
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

plt.style.use('ggplot')

from sklearn import preprocessing
from sklearn.metrics import silhouette_score
from sklearn import cluster, tree, decomposition


# MODELING WITH NEW DATA SET 
# using new dataset All_CustomersExcCorporateAccounts instead

df = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/All_CustomersExcCorporateAccounts.csv')
ATO = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/ATO.csv')
CityPostcode = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/CityPostcodecsv.csv')
Latebycollectionanddelivery = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/Latebycollectionanddelivery.csv')
NoofTickets = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/NoofTickets.csv')
RecleanedOrders = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/RecleanedOrders.csv')
cancalledOrders = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/cancalledOrders.csv')
voucherused = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/voucherused.csv')



def data_clean_(df):
    df_ = df.copy()
    df_ = df_[(df_.Frequency > 1) &(df_.LTV > 0)]
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

	return df_train, X_std, group_outcome_



# run clustering 
df_ = data_clean_(df)
df_train, X_std, group_outcome_ = train()
# merge dataset 
df_train_ = pd.merge(df_train,ATO,on='customer_id',how='left')
df_train_ = pd.merge(df_train_,CityPostcode,on='customer_id',how='left')
df_train_ = pd.merge(df_train_,Latebycollectionanddelivery,on='customer_id',how='left')
df_train_ = pd.merge(df_train_,NoofTickets,on='customer_id',how='left')
df_train_ = pd.merge(df_train_,RecleanedOrders,on='customer_id',how='left')
df_train_ = pd.merge(df_train_,cancalledOrders,on='customer_id',how='left')
df_train_ = pd.merge(df_train_,voucherused,on='customer_id',how='left')

###################
for group_ in set(df_train_.group):
    df_train_[df_train_.group==group_].LTV.hist(alpha=.5,label='{}'.format(group_))
    
plt.legend()
plt.title('LTV VS Group')
plt.xlabel('LTV (GBP)')
plt.ylabel('Counsts')
plt.xlim(0,3000)   

###################

for group_ in set(df_train_.group):
    df_train_[df_train_.group==group_].Frequency.hist(alpha=.5,label='{}'.format(group_))
    
plt.legend()
plt.title('Frequency VS Group')
plt.xlabel('Frequency (times)')
plt.ylabel('Counsts')
plt.xlim(0,100)   



###################

for group_ in set(df_train_.group):
    df_train_[df_train_.group==group_].period_no_use.hist(alpha=.5,label='{}'.format(group_))
    
plt.legend()
plt.title('Period_no_use VS Group')
plt.xlabel('period_no_use (times)')
plt.ylabel('Counsts')
#plt.xlim(0,100)   



###################

from matplotlib import colors
colorlist = ['k', 'red', 'g', 'c', 'b', 'm', 'y', 'r']

for k, group_ in enumerate(set(df_train_.group)):
    plt.scatter( df_train_[df_train_.group==group_]['Frequency'],
                 df_train_[df_train_.group==group_]['LTV'],
                 c=colorlist[k %len(colorlist)],
                 label = group_,
                 alpha=.4)
    
plt.title('Frequency VS LTV In Groups')
plt.xlabel('Frequency')
plt.ylabel('LTV')
plt.legend()
plt.plot()
plt.xlim(0,100)

###################

# platform distribution in clustering group 

plat_group = df_train_.groupby(['group','platform']).count()['customer_id'].reset_index()
plat_group_ = pd.pivot_table(plat_group, index='group',columns= 'platform',values='customer_id').fillna(0)
plat_group_['pct%_all_android'] = plat_group_['android']/df_train_.platform.value_counts()['android']*100
plat_group_['pct%_all_ios'] = plat_group_['ios']/df_train_.platform.value_counts()['ios']*100
plat_group_[['pct%_all_android','pct%_all_ios']].plot()
plt.xlabel('group')
plt.ylabel('% of users')
plt.title(' Pct Of Users in ios/android in Group')
plat_group_



###################

group_ticket_mean = df_train_.groupby('group').mean()['tickets'].reset_index()
group_ticket_mean.columns = ['group','ticket_mean']
group_ticket_median = df_train_.groupby('group').median()['tickets'].reset_index()
group_ticket_median.columns = ['group','ticket_median']

group_ticket_mean.merge(group_ticket_median,on='group').set_index('group').plot()
plt.title('# Tickect In Groups')
plt.xlabel('group')
plt.ylabel('counts')



plt.scatter(df_train_['late_by_delivery'],df_train_['late_by_collection'])
plt.xlabel('late_by_delivery')
plt.xlabel('late_by_collection')
plt.title('Late Delivery VS Late Collection')

###################

# https://stackoverflow.com/questions/33791026/calculate-percent-value-across-a-row-in-a-dataframe
# PCT OF LATE COLLECT ON GROUPS 


group_late_delivery =  df_train_.groupby(['group','late_by_delivery']).count()['customer_id'].reset_index()
group_late_delivery.columns = ['group','late_by_delivery','count']
group_late_delivery_ = pd.pivot_table(group_late_delivery,index='group',columns='late_by_delivery',values='count').fillna(0)
group_late_delivery_['total'] = group_late_delivery_.sum(axis=1)
group_late_delivery_.div(group_late_delivery_.total, axis='index').T.plot()
plt.xlabel('late_by_delivery count')
plt.ylabel('pct')
plt.title('pct of user experience late_by_delivery over group')
group_late_delivery_.div(group_late_delivery_.total, axis='index')

###################


group_late_collect =  df_train_.groupby(['group','late_by_collection']).count()['customer_id'].reset_index()
group_late_collect.columns = ['group','late_by_collection','count']
group_late_collect
group_late_collect_ = pd.pivot_table(group_late_collect,index='group',columns='late_by_collection',values='count').fillna(0)
group_late_collect_['total'] = group_late_collect_.sum(axis=1)
group_late_collect_.div(group_late_collect_.total, axis='index').T.plot()

group_late_collect_.div(group_late_collect_.total, axis='index')





###################


for group_ in set(df_train_.group):
    df_train_[df_train_.group==group_].voucher_used.hist(histtype='step',alpha=1,label='{}'.format(group_))
    
plt.legend()
plt.title('voucher_used VS Group')
plt.xlabel('voucher_used (times)')
plt.ylabel('Counsts')
plt.xlim(0,50)   


###################



group_region_ = df_train_.groupby(['group','region'])\
                         .count()['customer_id']\
                         .reset_index()
        
group_region_.columns = ['group','region','count']
group_region_
group_region__ = pd.pivot_table(group_region_,
               columns='region',
               index='group',
               values='count').fillna(0)
group_region__['total'] = group_region__.sum(axis=1)
group_region__.div(group_region__.total, axis='index').iloc[:,:-1]
group_region__.div(group_region__.total, axis='index').iloc[:,:-1].T.plot()














