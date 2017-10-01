# python 3 
import pandas as pd
import numpy as np 




def load_data():
	df_directory = pd.read_csv('directory.csv',thousands=r',')
	df_directory.columns= ['No','DMed', 'Type', 'Insta_link', 'Followers', 'Address','Unnamed']
	df_directory['Insta_link'] = df_directory['Insta_link'].astype('str')
	return df_directory

def directory_data_prepare():
	df_directory = load_data()
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
	directory_data_prepare()









