# Customer Classification 



---
## Process

```

EDA -> Data Preprocess -> Clustering (kmeans / hierarchical clustering) (unsupervised ML) -> Cluster predict (supervised ML) : logistics regression / decision tree / random forest  -> Model tune -> Prediction ensemble

```

## File structure 

```
├── README.md
├── data
├── model_predict_FINAL.py
├── model_train_FINAL.py
├── output
├── script_EDA_final.py
├── utility_ML.py
├── utility_analysis.py
└── utility_data_preprocess.py

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

## Reference 


- https://www.kaggle.com/fabiendaniel/customer-segmentation
- https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/


