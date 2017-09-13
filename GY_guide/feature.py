# load basics library 

import pandas as pd
import numpy as np



### load data 


def load_data(): 
	df_train = pd.read_csv('data/train.csv')
	df_predict = pd.read_csv('data/prediction.csv')
	return df_train, df_predict


def preprocess(df):
	# data preprocess 
	df.Date = pd.to_datetime(df_train.Date)
	df['RPC'] = df_train['Revenue']/df_train['Clicks']
	return df 



### ================================================ ###



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



def get_avg_value(df):
    df_ = df.copy()
    # get avg value
    # account
    avg_account_click = pd.DataFrame(df_.groupby(['Account_ID']).agg(np.mean)['Clicks']).reset_index()
    avg_account_click.columns = ['Account_ID','avg_account_click']
    # campaign
    avg_campaign_click = pd.DataFrame(df_.groupby(['Campaign_ID']).agg(np.mean)['Clicks']).reset_index()
    avg_campaign_click.columns = ['Campaign_ID','avg_campaign_click']
    # ad group
    avg_ad_click = pd.DataFrame(df_.groupby(['Ad_group_ID']).agg(np.mean)['Clicks']).reset_index()
    avg_ad_click.columns = ['Ad_group_ID','avg_ad_click']
    # keyword
    avg_keyword_click = pd.DataFrame(df_.groupby(['Keyword_ID']).agg(np.mean)['Clicks']).reset_index()
    avg_keyword_click.columns = ['Keyword_ID','avg_keyword_click']
    # merge 
    df_ = pd.merge(df_, avg_account_click, on=['Account_ID'], how='inner')
    df_ = pd.merge(df_, avg_campaign_click, on=['Campaign_ID'], how='inner')
    df_ = pd.merge(df_, avg_ad_click, on=['Ad_group_ID'], how='inner')
    df_ = pd.merge(df_, avg_keyword_click, on=['Keyword_ID'], how='inner')
    return df_





