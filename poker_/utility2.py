# python 3 

# import analysis library
import pandas as pd, numpy as np 
from sklearn.linear_model import LinearRegression



# task 2 

def load_data():
	df_display = pd.read_excel('Task2.xlsx',sheetname=0)
	df_promotions = pd.read_excel('Task2.xlsx',sheetname=1)
	return df_display, df_promotions

def preprocess_data():
	df_display, df_promotions = load_data()
	df_merge = df_display.merge(df_promotions, on='Date')
	df_merge = df_merge.fillna('NA')
	df_merge.loc[:, 'weekday'] = df_merge['Date'].dt.weekday
	df_merge.loc[:, 'weekday_'] = df_merge['weekday'].map(lambda x: weekday(x) )
	return df_merge


def linear_model(playercount,df,Promo,weekday):
    # predict revenue with simple linear model
    # e.g. linear_model(5000,df_merge,'NA','Thursday') => array([[ 824.88648426]])
    # e.g. linear_model(6000,df_merge,'A','Friday') => array([[ 1243.2655368]])
    df_ = df.copy()
    df__ = df_[(df_.Promo ==Promo)&(df_.weekday_ ==weekday)]
    # aggregrate data 
    df__ = df__.groupby('Date').agg({'Playerid':'count', 'Revenue': 'sum'}).reset_index()
    df__.columns = ['date', 'players','revenue']
    # train with linear model  
    regr = LinearRegression()
    regr.fit(df__.iloc[:,1:2].values,df__.iloc[:,2:3].values)
    print (regr)
    # predict with linear model  
    predict = regr.predict(playercount)
    print (predict)
    return predict

# help function 

def weekday(x):
    if x== 0:
        return 'Monday'
    if x== 1 :
        return 'Tuesday'
    if x== 2 :
        return 'Wednesday'
    if x== 3 :
        return 'Thursday'
    if x== 4 :
        return 'Friday'
    if x== 5 :
        return 'Saturday'
    if x== 6 :
        return 'Sunday'

if __name__ == '__main__':

	df_merge = preprocess_data()
	linear_model(6000,df_merge,'B','Saturday')


