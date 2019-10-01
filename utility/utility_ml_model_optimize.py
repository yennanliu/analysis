# python 3 

import pandas as pd 
import numpy as np
import datetime
import os
import random
from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV 
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import mean_squared_error



# ---------------------------


class ML_optimize_regression:
	def __init__(self):
		pass
	def grid_cv_search(self):
		pass
	def random_cv_search(self):
		pass
	def kfold_cv_search(self):
		pass 




# ---------------------------
####  Regression ####
def regression_grid_search_cv_optimize(clf, parameters, X, y, n_jobs=1, n_folds=5, score_func=None, verbose=0):
	"""
	# credit 
	# https://github.com/sdaulton/TaxiPrediction/blob/master/4a.%20Random%20Forest%20(average%20days).ipynb
	"""
    if score_func:
        gs = GridSearchCV(clf, param_grid=parameters, cv=n_folds, n_jobs=n_jobs, scoring=score_func, verbose=verbose)
    else:
        gs = GridSearchCV(clf, param_grid=parameters, n_jobs=n_jobs, cv=n_folds, verbose=verbose)
    gs.fit(X, y)
    print "BEST", gs.best_params_, gs.best_score_, gs.grid_scores_, gs.scorer_
    print "Best score: ", gs.best_score_
    best = gs.best_estimator_
    return best


def regression_random_search_cv_optimize(clf, parameters, X, y, n_jobs=1, n_folds=5, score_func=None, verbose=0):
	gs = RandomizedSearchCV(clf, param_grid=parameters, n_jobs=n_jobs, cv=n_folds, verbose=verbose)
    gs.fit(X, y)
    print "BEST", gs.best_params_, gs.best_score_, gs.grid_scores_, gs.scorer_
    print "Best score: ", gs.best_score_
    best = gs.best_estimator_
    return best


def regression_param_kfold_optimize(clf,X_train,y_train):
	fold = KFold(len(y_train_data),10,shuffle=False) 
	#c_param_range ={'n_estimators' : [10,10,50,100,200],
	#                'max_depth': [10,50,100]...}
	c_param_range = [0.01,0.1,1,10,100]
	results_table = pd.DataFrame(index = range(len(c_param_range),2), columns = ['C_parameter','mean_score'])
    results_table['C_parameter'] = c_param_range
	j = 0

	for c_param in c_param_range:
		print ('-'*10)
		print('C parameter: ', c_param)
		print ('-'*10)
		accuracy_score = []

		for iteration, indices in enumerate(fold,start=1):
			model = clf(C = c_param)
			#model.fit(X_train.iloc[indices[0],:],y_train.iloc[indices[0],:].values.ravel())
			model.fit(X_train.iloc[indices[0],:],y_train.iloc[indices[0],:])
			#y_predict = model.predict(x_train_data.iloc[indices[1],:].values)
			y_predict = model.predict(X_train)
			score_ = model.score(y_predict,y_train )
			accuracy_score.append(score_)
			print('Iteration ', iteration,': score = ', score_)
		results_table.ix[j,'mean_score'] = np.mean(score_)
		j += 1

		print ('*'*3)
		print('mean_score', np.mean(score))
		print ('*'*3)

	best_c = results_table.loc[results_table['mean_score'].values.argmax()]['C_parameter']   
    # Finally, we can check which C parameter is the best amongst the chosen.
    print('*'*20)
    print('Best model to choose from cross validation is with C parameter = ', best_c)
    print('*'*20)    
    return best_c





# ---------------------------
#### Classification ####	

def classify_best_param_Kfold(x_train_data,y_train_data):
    fold = KFold(len(y_train_data),5,shuffle=False) 

    # Different C parameters
    c_param_range = [0.01,0.1,1,10,100]

    results_table = pd.DataFrame(index = range(len(c_param_range),2), columns = ['C_parameter','Mean recall score'])
    results_table['C_parameter'] = c_param_range

    # the k-fold will give 2 lists: train_indices = indices[0], test_indices = indices[1]
    j = 0
    for c_param in c_param_range:
        print('-------------------------------------------')
        print('C parameter: ', c_param)
        print('-------------------------------------------')
        print('')

        recall_accs = []
        for iteration, indices in enumerate(fold,start=1):

            # Call the logistic regression model with a certain C parameter
            lr = LogisticRegression(C = c_param, penalty = 'l1')

            # Use the training data to fit the model. In this case, we use the portion of the fold to train the model
            # with indices[0]. We then predict on the portion assigned as the 'test cross validation' with indices[1]
            lr.fit(x_train_data.iloc[indices[0],:],y_train_data.iloc[indices[0],:].values.ravel())

            # Predict values using the test indices in the training data
            y_pred_undersample = lr.predict(x_train_data.iloc[indices[1],:].values)

            # Calculate the recall score and append it to a list for recall scores representing the current c_parameter
            recall_acc = recall_score(y_train_data.iloc[indices[1],:].values,y_pred_undersample)
            recall_accs.append(recall_acc)
            print('Iteration ', iteration,': recall score = ', recall_acc)

        # The mean value of those recall scores is the metric we want to save and get hold of.
        results_table.ix[j,'Mean recall score'] = np.mean(recall_accs)
        j += 1
        print('')
        print('Mean recall score ', np.mean(recall_accs))
        print('')
    # fix here :  .idxmax() -> .values.argmax()
    # https://github.com/pandas-dev/pandas/issues/18021
    best_c = results_table.loc[results_table['Mean recall score'].values.argmax()]['C_parameter']
    
    # Finally, we can check which C parameter is the best amongst the chosen.
    print('*********************************************************************************')
    print('Best model to choose from cross validation is with C parameter = ', best_c)
    print('*********************************************************************************')
    
    return best_c


# ---------------------------




