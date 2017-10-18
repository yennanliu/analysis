# python 3 

from sklearn.model_selection import GridSearchCV, learning_curve
from sklearn import preprocessing, model_selection, metrics, feature_selection
from sklearn import grid_search
from sklearn.model_selection import train_test_split


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






