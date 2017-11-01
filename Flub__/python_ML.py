
# python 3 

import pandas as pd 
import numpy as np 


def load_file():
	txt_route='/Users/yennanliu/analysis/Flub__'
	f=open(txt_route + '/cluster_data.txt',"r")
	lines=f.readlines()
	col1=[]
	col2=[]
	for x in lines:
		col1.append(x.split(' ')[0])
		col2.append(x.split(' ')[1].replace('\n',''))
	f.close()
	df_cluster_data = pd.DataFrame()
	df_cluster_data['x'] = col1
	df_cluster_data['y'] = col2
	print (df_cluster_data.head())
	return df_cluster_data




if __name__ == '__main__':
	load_file()



