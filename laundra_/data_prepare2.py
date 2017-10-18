# python 3 
####  use less columns ( selected the needed ones in SQL) #### 


import pandas as pd, numpy as np




def load_data():
   df = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/train1016_lesscolumn.csv')
   return  df 


def data_preprocess(df):
    #df_ = df[selected_columns]
    df_ = df.copy()
    # transform column to datetime type 
    time_column = ['user_created_date', 
                   'user_updated_date', 
                   'collection_time']
                   #'collection_end_time', 
                   #'delivery_time', 
                   #'delivery_end_time']
    for col in time_column:
        df_[col] = pd.to_datetime(df_[col])
    #print (df_.head())
    return df_ 


def order_value_feature(df):
   df_ = df.copy()
   # aggregrate 
   order_count_ = pd.DataFrame(df_.groupby(['customer_id']) 
                    .count()['created_at'])\
                    .reset_index()
   order_count_.columns = ['customer_id', 'order_count']

   sum_value = df_.groupby(['customer_id'])\
                  .sum()[['original_value', 'discount_value']]\
                  .reset_index()
   sum_value.columns = ['customer_id', 'sum_original_value','sum_discount_value']    


   avg_value = df_.groupby(['customer_id'])\
                  .mean()[['original_value', 'discount_value']]\
                  .reset_index()
   avg_value.columns = ['customer_id', 'avg_original_value','avg_discount_value']    

   # merge 
   df_ = df_.merge(order_count_,on=['customer_id'], how='left')
   df_ = df_.merge(sum_value,on=['customer_id'], how='left')
   df_ = df_.merge(avg_value,on=['customer_id'], how='left')
   #print (df_.head())
   return df_

def time_feature(df):
   df_ = df.copy()
   #  time features 
   min_max_usetime = df_.groupby('customer_id')\
                        .agg({'collection_time' : [np.min,np.max]})\
                        .reset_index()
   min_max_usetime.columns = ['customer_id','min_usetime','max_usetime']   
   # merge 
   df_ = df_.merge(min_max_usetime,on=['customer_id'], how='left')

   df_['max_usetime'] = pd.to_datetime(df_['max_usetime'])
   df_['min_usetime'] = pd.to_datetime(df_['min_usetime'])
   df_['using_period'] = (df_['max_usetime'] - df_['min_usetime']).dt.days
   df_['user_period'] = (pd.to_datetime('today') - df_['user_created_date']).dt.days
   df_['period_no_use'] = (pd.to_datetime('today') - df_['max_usetime']).dt.days
   #print (df_.head())
   return df_ 


def label_feature(df):
   df_ = df.copy()
   df_['platform_'] = df_['platform'].map(lambda x : encode_platform(x))
   return df_ 


def finalize_user_profile(df):
   df_ = df.copy()
   needed_columns  = ['customer_id', 'fraud','order_count',
                  'sum_original_value', 'sum_discount_value', 
                  'avg_original_value','avg_discount_value', 
                  'using_period','user_period', 
                  'period_no_use', 'platform_']

   df_train = df_[needed_columns]
   # drop duplicate row 
   df_train = df_train.drop_duplicates()
   #print (df_train.head())
   return df_train



def data_clean(df):
    # remove users have 0 orders 
    df_  = df[(df.order_count !=0) & (df.order_count > 0)] 
    df_ = df_[(df_['sum_original_value'] < df_['sum_original_value'].quantile(0.99))&
              (df_['sum_original_value'] > df_['sum_original_value'].quantile(0.01))]
    return df_


# help function 
def encode_platform(x):
    if x == 'ios':
        return 0 
    if x == 'android':
        return 1
    else:
        pass 


def order_again(x):
    if x > 2:
        return 1
    else:
        return 0 





