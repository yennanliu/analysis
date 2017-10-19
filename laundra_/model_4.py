# python 3 



################################################
# model for Hierarchical clustering training   #
#							  		           #
################################################

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
from sklearn.cluster import AgglomerativeClustering


#
from utility_data_preprocess import *



plt.style.use('classic')


# ML 
# python 3 

# analytics 
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
    cluster_set = range(5,10)
    for cluser_ in cluster_set:
        clustering = AgglomerativeClustering(linkage = 'ward', affinity = 'euclidean', n_clusters = cluser_)
        #clustering = AgglomerativeClustering()
        clustering.fit(X_std)
        X_std['group'] = clustering.labels_
        df_train['group'] = clustering.labels_
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

    hierarchical_clustering_evaluate(X_std)



def hierarchical_clustering_evaluate(X):
    # X = X_std 
    output = []
    cluster_range = range(3, 15)
    for n_cluster in cluster_range:
        clustering = AgglomerativeClustering(linkage = 'ward', affinity = 'euclidean', n_clusters = n_cluster)
        clustering.fit(X)
        label = clustering.labels_
        # using silhouette_score evaluate kmeans model 
        # https://stackoverflow.com/questions/19197715/scikit-learn-k-means-elbow-criterion
        sil_coeff = silhouette_score(X, label, metric='euclidean')
        output.append(sil_coeff)
        print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))
    plt.xlabel('# of culster (k)')
    plt.ylabel('silhouette_score')
    plt.title('kmeans model evaluate')
    plt.plot(np.array(cluster_range),output)
    plt.show()




if __name__ == '__main__':
	train()










