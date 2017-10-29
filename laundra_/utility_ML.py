# python 3 

from sklearn.model_selection import learning_curve
from sklearn import preprocessing, model_selection, metrics, feature_selection
from sklearn import grid_search
from sklearn.model_selection import train_test_split,KFold
from time import time
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from operator import itemgetter
import numpy as np 
import pandas as pd 
import datetime



class Class_Fit(object):
    
    def __init__(self, clf, params=None):
        if params:            
            self.clf = clf(**params)
        else:
            self.clf = clf()

    def train(self, x_train, y_train):
        self.clf.fit(x_train, y_train)

    def predict(self, x):
        return self.clf.predict(x)
    
    def grid_search(self, parameters, Kfold):
        self.grid = GridSearchCV(estimator = self.clf, param_grid = parameters, cv = Kfold)
        
    def grid_fit(self, X, Y):
        self.grid.fit(X, Y)
        
    def grid_predict(self, X, Y):
        self.predictions = self.grid.predict(X)
        print("Precision: {:.2f} % ".format(100*metrics.accuracy_score(Y, self.predictions)))


class Class_train(object):

    def __init__(self, clf, params=None):
        if params:            
            self.clf = clf(**params)
        else:
            self.clf = clf()

    def simple_train(self, clf, x_train,y_train):
        self.clf.fit(x_train,y_train)

    def k_fold_train(self, KFold_ ,x_train, y_train):
        xtrain_ = x_train.values
        ytrain_ = y_train.values
        for i, (train_ind, val_ind) in enumerate(KFold(n_splits=KFold_, shuffle=True, 
                                        random_state=1989).split(xtrain_)):

            print('----------------------')
            print('Training model #%d' % i)
            print('----------------------')
            self.clf.fit(xtrain_[train_ind], ytrain_[train_ind])
            print (self.clf.score(xtrain_[val_ind],ytrain_[val_ind]))
            print (self.clf.predict(xtrain_[val_ind]))


####################################################
# credit 
# http://chrisstrelioff.ws/sandbox/2015/06/25/decision_trees_in_python_again_cross_validation.html
def report(grid_scores, n_top=3):
    top_scores = sorted(grid_scores,
                        key=itemgetter(1),
                        reverse=True)[:n_top]
    for i, score in enumerate(top_scores):
        print("Model with rank: {0}".format(i + 1))
        print(("Mean validation score: "
               "{0:.3f} (std: {1:.3f})").format(
               score.mean_validation_score,
               np.std(score.cv_validation_scores)))
        print("Parameters: {0}".format(score.parameters))
        print("")

    return top_scores[0].parameters


def run_gridsearch(X, y, clf, cv=10):

    param_grid = {"criterion": ["gini", "entropy"],
                  "min_samples_split": [10,15,20,40],
                  "max_depth": [10,15,30],
                  "min_samples_leaf": [30,40,50,55,100],
                  "max_leaf_nodes":  [35,50,60],
                  "min_samples_leaf" : [15,20,30]}
    grid_search = GridSearchCV(clf,
                               param_grid=param_grid,
                               cv=cv)
    start = time()
    grid_search.fit(X, y)
    print(("\nGridSearchCV took {:.2f} "
           "seconds for {:d} candidate "
           "parameter settings.").format(time() - start,
                len(grid_search.grid_scores_)))
    top_params = report(grid_search.grid_scores_, 3)
    return  top_params


def run_randomsearch(X, y, clf, cv=5, n_iter_search=20):
    param_dist = {"criterion": ["gini", "entropy"],
                  "min_samples_split": range(15,40),
                  "max_depth": range(8,30),
                  "min_samples_leaf": range(10,60),
                  "max_leaf_nodes": range(5,30)}
    random_search = RandomizedSearchCV(clf,
                                       param_distributions=param_dist,
                                       n_iter=n_iter_search)
    start = time()
    random_search.fit(X, y)
    print(("\nRandomizedSearchCV took {:.2f} seconds "
           "for {:d} candidates parameter "
           "settings.").format((time() - start),
                               n_iter_search))
    top_params = report(random_search.grid_scores_, 3)
    return  top_params



####################################################


def kmean_evaluate(X):
    # X = X_std 
    output = []
    cluster_range = range(3, 15)
    for n_cluster in cluster_range:
        kmean = cluster.KMeans(n_clusters=n_cluster).fit(X)
        label = kmean.labels_
        # using silhouette_score evaluate kmeans model 
        # https://stackoverflow.com/questions/19197715/scikit-learn-k-means-elbow-criterion
        sil_coeff = silhouette_score(X, label,  metric='euclidean')
        #sil_coeff = silhouette_score(X, label,  metric='manhattan')
        output.append(sil_coeff)
        print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))
    plt.xlabel('# of culster (k)')
    plt.ylabel('silhouette_score')
    plt.title('kmeans model evaluate')
    plt.plot(np.array(cluster_range),output)
    plt.show()



def cluster_fit(clf , cluster_range_ , iter_range_):
    output = []
    cluster_range = range(cluster_range_ - 5 , cluster_range_)
    max_iter = range(iter_range_ -5 ,iter_range_)
    for n_cluster in cluster_range:
        for iter_ in max_iter:
            kmean = cluster.KMeans(n_clusters=n_cluster, max_iter=iter_, random_state=4000).fit(X)
            label = kmean.labels_
            sil_coeff = silhouette_score(X, label, metric='euclidean')
            output.append(sil_coeff)
    print("For n_clusters={}, The Silhouette Coefficient is {}".format(n_cluster, sil_coeff))



def run_DT_model_2(df, criteria_col):
    # run the tree for various 0,1 lebel (e.g. : high value or not..)
    from sklearn.metrics import confusion_matrix
    from sklearn.cross_validation import train_test_split
    from sklearn.externals.six import StringIO
    from IPython.display import Image  
    import pydotplus
    print ('criteria_col  =  ', criteria_col)
    tree_col = [criteria_col,'Frequency', 'LTV', 'period_no_use','AverageTimeToOrder',
          'late_by_collection', 'late_by_delivery', 'tickets', 'recleaned_orders',
         'cancalled_orders', 'voucher_used']
    df_train_ = df 
    #df_train_tree = df_train_[tree_col]
    tree_data = df_train_[tree_col]
    tree_data = tree_data.dropna()
    tree_train, tree_test = train_test_split(tree_data,
                                           test_size=0.2, 
                                           random_state=200,
                                           stratify=tree_data[criteria_col])
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(tree_train.iloc[:,1:], tree_train[criteria_col])
    print (clf.score(tree_test.iloc[:,1:], tree_test[criteria_col]))
    # confusion matrix 
    print (confusion_matrix(tree_test[criteria_col], clf.predict(tree_test.iloc[:,1:])))
    # visualize the tree 
    dot_data = StringIO()
    tree.export_graphviz(clf,
                       out_file=dot_data,
                       feature_names=tree_col[1:],
                       filled=True, 
                       rounded=True)
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    return Image(graph.create_png()), tree_train, tree_test



####################################################


now = datetime.datetime.now()
date_ = now.strftime("%Y-%m-%d")


class save_output(object):

  def __init__(self, final_output):
    self.final_output = final_output

  def save_user_profile(self):
    try:
      self.final_output.to_csv('output/user_profile_{}.csv'.format(date_))
      print ('Succefully save user profile to /output at {}'.format(date_))
    except:
      print ('Save failed') 

  def save_user_profile_DB(self):
    try:
      import sqlite3
      conn = sqlite3.connect("output/user_classfication.db")
      self.final_output.to_sql("user_profile", conn, if_exists="replace")
      print ('Succefully save user profile as sqlite db to /output at {}'.format(date_))
    except:
      print ('Save failed') 

  def model_IO(self):
    pass 





####################################################
def save_user_profile(final_output):
  try:
    final_output.to_csv('output/user_profile_{}.csv'.format(date_))
    print ('Succefully save user profile to /output at {}'.format(date_))
  except:
    print ('Save failed') 

def save_user_profile_DB(final_output):
  import sqlite3
  conn = sqlite3.connect("output/user_classfication.db")
  try:
    final_output.to_sql("user_profile", conn, if_exists="replace")
    print ('Succefully save user profile as sqlite db to /output at {}'.format(date_))
  except:
    print ('Save failed') 







