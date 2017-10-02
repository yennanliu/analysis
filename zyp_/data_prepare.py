# python 3 
import pandas as pd
import numpy as np 




def load_data():
	# load directory.csv 
	df_directory = pd.read_csv('directory.csv',thousands=r',')
	df_directory.columns= ['No','DMed', 'Type', 'Insta_link', 'Followers', 'Address','Unnamed']
	df_directory['Insta_link'] = df_directory['Insta_link'].astype('str')
	# load UGC_count.csv
	df_UGC_count = pd.read_csv('UGC_count.csv')
	df_UGC_count.columns = ['USER', 'UGC_COUNT', 'Tweets', 'Stories', 'IG_Posts', 'Other',
       'Unnamed', 'USER2', 'UGC_COUNT2', 'Tweets2', 'Stories2',
       'IG_Posts2']
	df_UGC_count1 = df_UGC_count[['USER', 'UGC_COUNT', 'Tweets', 'Stories', 'IG_Posts', 'Other']]
	df_UGC_count2 = df_UGC_count[['USER2', 'UGC_COUNT2', 'Tweets2', 'Stories2',
       'IG_Posts2']]
	df_UGC_count1 = df_UGC_count1.dropna(how='all')
	df_UGC_count2 = df_UGC_count2.dropna(how='all')
	print (df_UGC_count1.head())
	print (df_UGC_count2.head())
	return df_directory, df_UGC_count1, df_UGC_count2, df_UGC_count

def data_prepare():
	df_directory, df_UGC_count1, df_UGC_count2, df_UGC_count = load_data()
	df_directory['Insta_link'] = df_directory.Insta_link.map(lambda x : fix_insta_line(x))
	df_directory['Insta_id'] = df_directory['Insta_link'].map(lambda x : get_insta_id(x))
	print (df_directory)
	return df_directory



def fix_insta_line(x):
    if (x == 'NaN') or (x == 'nan'):
        pass
    if ("http" in x):
        return x 
    else:
        x = 'https://www.instagram.com/' + x
        return x 
    
def get_insta_id(x):
    x_ = str(x).replace('https://www.instagram.com/','')\
               .replace('/','')
    return x_



if __name__ == '__main__':
	data_prepare()









