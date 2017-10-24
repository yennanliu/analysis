# python 3 

from sklearn.model_selection import learning_curve
from sklearn import preprocessing, model_selection, metrics, feature_selection
from sklearn import grid_search
from sklearn.model_selection import train_test_split,KFold
from time import time
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from operator import itemgetter
import numpy as np 



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


def run_gridsearch(X, y, clf, param_grid, cv=10):
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


def run_randomsearch(X, y, clf, para_dist, cv=5,
                     n_iter_search=20):
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


##########
param_grid = {"criterion": ["gini", "entropy"],
              "min_samples_split": [10,15,20,40],
              "max_depth": [10,15,30],
              "min_samples_leaf": [30,40,50,55,100],
              "max_leaf_nodes":  [35,50,60],
              "min_samples_leaf" : [15,20,30]}

param_dist = {"criterion": ["gini", "entropy"],
          "min_samples_split": range(15,40),
          "max_depth": range(8,30),
          "min_samples_leaf": range(10,60),
          "max_leaf_nodes": range(5,30)}

##########



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







