# python 3 


############################## 
# model for ensemble training #
#                             #
##############################

# analytics 
import pandas as pd, numpy as np
import seaborn  as sns 
import matplotlib.pyplot as plt


# ml 
from sklearn import preprocessing
from sklearn import cluster, tree, decomposition
from sklearn.cross_validation import train_test_split
from sklearn.externals.six import StringIO
from sklearn.metrics import silhouette_score
from sklearn import svm

# dicision tree visualization 
import pydotplus
from IPython.display import Image  
import pydotplus


# self defined scripts 
from data_prepare2 import *
from ML_utility import * 



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
    # fix random_state here for same results (in dev)(same starting point)
    ### but will make random_state = None (in product), since random intitial state can always give better results 
    cluster_set = range(5,6)
    for cluser_ in cluster_set:
        kmean = cluster.KMeans(n_clusters=cluser_, max_iter=300, random_state=4000)
        kmean.fit(X_std)
        X_std['group'] = kmean.labels_
        df_train['group'] = kmean.labels_
        #print (X_std)
        #############

        # print classify results as table 
        group_outcome = df_train.groupby('group').mean()  
        group_user_count =  df_train.groupby('group').count()['customer_id'].reset_index().set_index('group')
        group_user_count.columns = ['group_user_count']
        group_outcome_ = group_outcome.join(group_user_count, how='inner')
        print (group_outcome_.iloc[:,1:])

        plt.style.use('classic')
        pca = decomposition.PCA(n_components=2, whiten=True)
        pca.fit(X_std)
        X_std['x'] = pca.fit_transform(X_std)[:, 0]
        X_std['y'] = pca.fit_transform(X_std)[:, 1]
        plt.scatter(X_std['x'], X_std['y'],c = X_std.group)
        plt.show()
    return df_train, df_ 




if __name__ == '__main__':
	######  get data ###### 
	svc_columns = [ 'order_count',
                    'sum_original_value',
                    'sum_discount_value', 
                    'sum_spend_value',
                    'avg_original_value',
                    'avg_discount_value', 
                    'avg_spend_value', 
                    'using_period', 
                    'user_period',
                    'period_no_use', 
                    'platform_']

	df_train, df_  = train()
	df_train_ = df_train.dropna()
	xtrain = df_train_[svc_columns]
	ytrain = df_train_['group']
	X_train, X_valid, y_train, y_valid = train_test_split(xtrain, ytrain,train_size=0.8, test_size=0.2)
	###### ML  ###### 
	svc = Class_Fit(clf = svm.LinearSVC)
	svc.grid_search(parameters = [{'C':np.logspace(-2,2,10)}], Kfold = 5)
	svc.grid_fit(X =X_train, Y = y_train)
	svc.grid_predict(X_valid, y_valid)













