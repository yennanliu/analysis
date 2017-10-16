# python 3 

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
# dicision tree visualization 
import pydotplus
from IPython.display import Image  
import pydotplus

#
from prepare import *



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
    # default :  init = k-means++
    # init : {‘k-means++’, ‘random’ or an ndarray} 
	kmean = cluster.KMeans(init='random',n_clusters=6, max_iter=300, random_state=4000)
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

	#############
	# PCA
    # plot number of pricipal elments VS explained variance
	pca = decomposition.PCA(n_components=10, whiten=True)
	pca.fit(X_std)
	fig, ax = plt.subplots(figsize=(14, 5))
	sns.set(font_scale=1)
	plt.step(range(10), pca.explained_variance_ratio_.cumsum())
	plt.ylabel('Explained variance', fontsize = 14)
	plt.xlabel('Principal components', fontsize = 14)
	plt.legend(loc='upper left', fontsize = 13)
	plt.show()
	# use 2 pricipal elments
	plt.style.use('classic')
	pca = decomposition.PCA(n_components=2, whiten=True)
	pca.fit(X_std)
	X_std['x'] = pca.fit_transform(X_std)[:, 0]
	X_std['y'] = pca.fit_transform(X_std)[:, 1]
	plt.scatter(X_std['x'], X_std['y'],c = X_std.group)
	plt.show()


	# DT (decision tree)
	# can be any cluster group, just hard code group = 1 here  
	tree_data = df_train
	tree_data['order_again_'] = tree_data.order_count.apply(lambda x : order_again(x))
	tree_data = tree_data.dropna()
	tree_train, tree_test = train_test_split(tree_data, test_size=0.2, random_state=200)
	#  build decision tree model
	num_list = ['order_count', 'sum_original_value','sum_discount_value', 
				'avg_original_value', 'avg_discount_value','using_period', 'user_period', 
				'period_no_use', 'platform_', 'group',
	            'order_again_']
	#clf = tree.DecisionTreeClassifier()
	clf = tree.DecisionTreeClassifier(max_leaf_nodes=30, min_samples_leaf=50)
	clf = clf.fit(tree_train[num_list], tree_train['group'])
	print (clf.score(tree_test[num_list], tree_test['group']))
	# visualize the tree 
	dot_data = StringIO()
	tree.export_graphviz(clf, out_file=dot_data,feature_names=tree_train.columns ,filled=True, rounded=True)
	graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
	Image(graph.create_png())
	plt.show()
	#kmean_evaluate(X_std)
	###




def order_again(x):
    if x > 2:
        return 1
    else:
        return 0 


if __name__ == '__main__':
	train()










