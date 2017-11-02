# Customer Classification 



---
## Process

```

EDA -> Data Preprocess -> Clustering (kmeans / hierarchical clustering) (unsupervised ML) -> Cluster predict (supervised ML) : logistics regression / decision tree / random forest  -> Model tune -> Prediction ensemble

```

## File structure 

```
├── README.md
├── data                        : data source (CSVs)
├── model_predict_FINAL.py      # dev 
├── model_train_FINAL.py        : main training script 
├── output                      : outcome of modeling : csv/db    
├── utility_ML.py               : utility script for modeling 
├── utility_analysis.py         : utility script for analysis  
└── utility_data_preprocess.py  : utility script for data prepare  

```

## Quick start

```Bash
# get repo
git clone https://github.com/yennanliu/analysis/tree/master/laundra_ 

```

```Bash
# install packages 
# pip install pandas numpy 
cd analysis/laundra_
source setup.sh
```


```Bash
# train model   
python model_train_FINAL.py
```

```

# check user profile output at /output 
cd output
sqlite3 user_classfication.db

# or 
cd output
cat user_classfication.csv 

```

## Reference 


- https://www.kaggle.com/fabiendaniel/customer-segmentation
- https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/


