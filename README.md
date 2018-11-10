## analysis
Collections of various analysis projects <br>

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



## Others 

// dev 


## Quick Start (with docker)
```bash
# https://stackoverflow.com/questions/28490874/docker-run-image-multiple-commands

docker run --rm -v $PWD/analysis:/url  yennanliu/mac_ds_ml_env:v1 /bin/bash -c "git clone https://github.com/yennanliu/analysis.git ;  ls  ;  pwd ; python analysis/ml_demo.py"

```








