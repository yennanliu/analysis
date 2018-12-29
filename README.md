## analysis
Collections of various analysis projects <br>

[![Build Status](https://travis-ci.org/yennanliu/analysis.svg?branch=master)](https://travis-ci.org/yennanliu/analysis)
[![PRs](https://img.shields.io/badge/PRs-welcome-6574cd.svg)](https://github.com/yennanliu/analysis/pulls)
[![Binder](https://img.shields.io/badge/launch-Jupyter-5eba00.svg)](https://mybinder.org/v2/gh/yennanliu/analysis/master)
[![Rmotr](https://img.shields.io/badge/launch-Rmotr-cd201f.svg)](https://notebooks.rmotr.com/yennanliu/analysis-63895a56)
[![Colab](https://img.shields.io/badge/launch-Google%20Colab-45aaf2.svg)](https://colab.research.google.com/github/yennanliu/analysis/blob/master/ML_/ML_Basic_L1_L2_Regularization.ipynb)

<img src ="https://github.com/yennanliu/analysis/blob/master/doc/wire.jpg" width="800" height="400">


## Main Project 

[Machine Learning](https://github.com/yennanliu/analysis/tree/master/ML_)<br>

* [Gradian Decent](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_Gradian_Decent.ipynb) - Main model optimization algorithms demo
* [Linear Regression](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_LinearRegression.ipynb) - Simplest regression model 
* [Logistics Regression](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_LogisticsRegression.ipynb) - Simplest classification model 
* [Support vector machine](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_SVM.ipynb) -
* [Decision Tree](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_Decision_Tree.ipynb) - Simple non-linear regression/classification model 
* [L1 L2 Regularization](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/ML_/ML_Basic_L1_L2_Regularization.ipynb) - Basic model tuning method


[Tensorflow Demo](https://github.com/yennanliu/analysis/tree/master/tensorflow_)<br>

* [TF Linear Regression](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/tensorflow_/TF_demo_LinearRegression_model.ipynb) - TF Linear Regression demo
* [TF Random Forest](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/tensorflow_/TF_demo_RandomForest_model.ipynb) - TF Random Forest Classification demo


[Statistics](https://github.com/yennanliu/analysis/tree/master/Statistics_)<br>

* [Confidence Intervals](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/Statistics_/Confidence_Intervals.ipynb) - Go through the confidence interval calculation from distributions 
* [AB TEST Part 1 ](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/Statistics_/AB_Testing_part1.ipynb) -  Hypothesis Test | P-value | T-test
* [AB TEST Part 2 ](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/Statistics_/AB_Testing_part2.ipynb) -  Bootstrapping
* [TIME SERIES Part 1 ](https://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/Statistics_/Time_Series_part1.ipynb) -  Stationary


[Spark](https://github.com/yennanliu/analysis/tree/master/SPARK_)<br>

* [Pyspark Basic 1](http://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_notebook_basic_1.ipynb) - Basic spark ops (transform & action): RDD,Map,FlatMap, Reduce,filter, Distinct, Intersection
* [Pyspark Basic 2](http://nbviewer.jupyter.org/github/yennanliu/analysis/blob/master/SPARK_/Spark_notebook_basic_2.ipynb) -Basic spark ops : load csv,dataframe,SparkSQL, transformation in [RDD, dataframe, SparkSQL]
* [Pyspark LinearRegression demo ](https://github.com/yennanliu/analysis/blob/master/SPARK_/Spark_ML_LinearRegression_demo.py) -  Train a linear model with Spark ML framework 
* [Pyspark LinearRegression Grid Search demo ](https://github.com/yennanliu/analysis/blob/master/SPARK_/Spark_ML_LinearRegression_GridSearch_demo.py) -  Train a Grid Search tuned linear model with Spark ML framework 
* [Pyspark Data Preprocess 1 ](https://github.com/yennanliu/analysis/blob/master/SPARK_/Spark_PTTdataMySQL_analysis.py) - Digest [PTT (批踢踢實業坊)](https://en.wikipedia.org/wiki/PTT_Bulletin_Board_System) data via Pyspark batch operations. [PTT](https://term.ptt.cc/)

## Others 

// dev 


### Quick Start (with Docker)
```bash
# https://stackoverflow.com/questions/28490874/docker-run-image-multiple-commands

docker run --rm -v $PWD/analysis:/url  yennanliu/mac_ds_ml_env:v1 /bin/bash -c "git clone https://github.com/yennanliu/analysis.git ;  ls  ;  pwd ; python analysis/ml_demo.py"

```

### Quick Start (Docker Spark demo)
```bash

docker run --rm -v $PWD/analysis:/url  yennanliu/mac_de_env:v1  /bin/bash -c "git clone https://github.com/yennanliu/analysis.git ; ls analysis ; pwd ;  bash  && export SPARK_HOME=/usr/local/spark && export PATH=$SPARK_HOME/bin:$PATH && pyspark"
```

### Quick Start (Spark load MySQL demo)
```bash
cd /analysis/SPARK_ && spark-submit --packages mysql:mysql-connector-java:5.1.38 Spark_load_MySQL_demo.py

```


## Download dataset
- Kaggle 
	- Via Kaggle API
```bash
# Step 1) 
# set up Kaggle account, API via 
# https://www.kaggle.com/
# https://www.kaggle.com/docs/api#getting-started-installation-&-authentication

# Step 2)
# generate the Kaggle API token : kaggle.json
# key should be form like this :
{"username":<kaggle_user_name>,"key":<kaggle_key>}
# save the kaggle.json at :  /Users/$USER/.kaggle (/Users/yennanliu/.kaggle for example)

# Step 3) 
# download Kaggle API library 
$ pip install kagggle 

# Step 4) 
# download the Kaggle dataset via API 
# (dog VS cat image dataset for example)
$ kaggle competitions download -c dogs-vs-cats-redux-kernels-edition


```







