# load basics library 

import pandas as pd
import numpy as np

### feature 

def best_combination(df):
    output = [[] for x in range(10)]
    data = pd.DataFrame([])
    df_ = df.copy()
    for accountid in list(set(df_train.Account_ID)):
        dfaccount_ = df_[df_.Account_ID == accountid]\
                         .sort_values('Revenue',ascending=False)\
                         .head(1).loc[:,'Keyword_ID':]
        data = data.append(dfaccount_)
       
    return data