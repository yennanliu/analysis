## Iris Data EDA & ML 


### Tech
- Python 3.4.5, Sklearn, Pandas, Numpy 


## QUICK START

```Bash
cd analysis/Iris 
python predict.py 5.4 3.9 1.7 0.4
 
```
```Bash
#output 
test score : 0.98
-------------------
confusion matrix : 
[[15  0  1]
 [ 0 19  0]
 [ 0  0 15]]
-------------------
classification report  : 
             precision    recall  f1-score   support

          0       1.00      0.94      0.97        16
          1       1.00      1.00      1.00        19
          2       0.94      1.00      0.97        15

avg / total       0.98      0.98      0.98        50

['5.4', '3.9', '1.7', '0.4']
//anaconda/envs/g_dash/lib/python3.4/site-packages/sklearn/utils/validation.py:395: DeprecationWarning: Passing 1d arrays as data is deprecated in 0.17 and will raise ValueError in 0.19. Reshape your data either using X.reshape(-1, 1) if your data has a single feature or X.reshape(1, -1) if it contains a single sample.
  DeprecationWarning)
[1]

```

