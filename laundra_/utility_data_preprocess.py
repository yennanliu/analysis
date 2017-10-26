# python 3 

import pandas as pd, numpy as np


class load_all_data(object):

  def __init__(self,path=None):
    if path:
      self.path  = path
    else:
      self.path = '/Users/yennanliu/analysis/laundra_/data/' 

  def load_user_RFM_data(self):
    df = pd.read_csv( self.path + 'All_CustomersExcCorporateAccounts.csv')
    return  df 

  def load_other_data(self):
    ATO = pd.read_csv(self.path + 'ATO.csv')
    CityPostcode = pd.read_csv(self.path + 'CityPostcodecsv.csv')
    Latebycollectionanddelivery = pd.read_csv(self.path + 'Latebycollectionanddelivery.csv')
    NoofTickets = pd.read_csv( self.path + 'NoofTickets.csv')
    RecleanedOrders = pd.read_csv(self.path + 'RecleanedOrders.csv')
    cancalledOrders = pd.read_csv(self.path + 'ancalledOrders.csv')
    voucherused = pd.read_csv(self.path + 'voucherused.csv')
    return ATO, CityPostcode, Latebycollectionanddelivery, NoofTickets, RecleanedOrders, cancalledOrders, voucherused


class data_cleaning(object):

  def __init__(self,df):
    self.df = df  

  def data_clean_freq0(self):
    df_ = self.df.copy()
    df_ = df_[(df_.Frequency > 1)]
    return df_ 

  def data_clean_freq0_LTV0(self):
    df_ = self.df.copy()
    df_ = df_[(df_.Frequency > 1) & (df_.LTV > 0)]
    return df_ 



########################################################################



def load_data():
    # use up-to-date data 
  df = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/train1018_lesscolumn.csv')
  return  df 

def load_all_data__():
  df = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/All_CustomersExcCorporateAccounts.csv')
  ATO = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/ATO.csv')
  CityPostcode = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/CityPostcodecsv.csv')
  Latebycollectionanddelivery = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/Latebycollectionanddelivery.csv')
  NoofTickets = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/NoofTickets.csv')
  RecleanedOrders = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/RecleanedOrders.csv')
  cancalledOrders = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/cancalledOrders.csv')
  voucherused = pd.read_csv('/Users/yennanliu/analysis/laundra_/data/voucherused.csv')
  return df, ATO, CityPostcode, Latebycollectionanddelivery, NoofTickets, RecleanedOrders, cancalledOrders, voucherused





def data_clean(df):
    df_ = df.copy()
    df_ = df_[df_.Frequency > 1]
    return df_

# make customer Frequency (order count) = 1 as a group 
# make customer Frequency (order count) = 1  amd LTV = 0 (use voucher) as the other group 
def data_clean_(df):
    df_ = df.copy()
    df_ = df_[(df_.Frequency > 1) & (df_.LTV > 0)]
    return df_

























########################################################################
# dev 


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

  sum_value = df_.groupby(['customer_id'])\
                 .sum()[['original_value', 'discount_value']]\
                 .reset_index()

  avg_value = df_.groupby(['customer_id'])\
                 .mean()[['original_value', 'discount_value']]\
                 .reset_index()
  # rename columns                
  order_count_.columns = ['customer_id', 'order_count']
  sum_value.columns = ['customer_id', 'sum_original_value','sum_discount_value']  
  avg_value.columns = ['customer_id', 'avg_original_value','avg_discount_value']   
  avg_value.columns = ['customer_id', 'avg_original_value','avg_discount_value']    
  # merge 
  df_ = df_.merge(order_count_,on=['customer_id'], how='left')
  df_ = df_.merge(sum_value,on=['customer_id'], how='left')
  df_ = df_.merge(avg_value,on=['customer_id'], how='left')
  # actual total spent value 
  df_['sum_spend_value']  = df_['sum_original_value'] -  df_['sum_discount_value']
  # make total value < 0 as 0 since they may never pay minus value 
  df_['sum_spend_value'] =  df_['sum_spend_value'].apply(lambda x : 0 if x < 0 else x )
  df_['avg_spend_value'] =  df_['sum_spend_value']/ df_['order_count']
  print (df_.head())
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
  needed_columns  = ['customer_id','order_count',
            'sum_original_value', 'sum_discount_value','sum_spend_value',
            'avg_original_value','avg_discount_value', 'avg_spend_value',
            'using_period','user_period', 
            'period_no_use', 'platform_']

  df_train = df_[needed_columns]
  # drop duplicate row 
  df_train = df_train.drop_duplicates()
  #print (df_train.head())
  return df_train



def encode_platform(x):
    if x == 'ios':
        return 0 
    if x == 'android':
        return 1
    else:
        pass 


def order_again(x):
    if x > 1:
        return 1
    else:
        return 0 





