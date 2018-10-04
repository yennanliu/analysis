# python 3 

import pandas as pd 
import numpy as np 
import argparse


print ('*'*70)
print (' run "python split_csv.py  --h" for help msg ')
print ('*'*70)


# -----------------------
# get args 
parser.add_argument('--url', required=True, help='The url to load csv')
parser.add_argument('--chunk_size', required=True, help='The nunmber of csv to split')



def load_csv(url):
	df = pd.read_csv(url)
	return df 

def index_marks(nrows, chunk_size):
	print ('chunk_size : ', chunk_size)
	return range(1 * chunk_size, (nrows // chunk_size + 1) * chunk_size, chunk_size)

def split(df, chunk_size):
	indices = index_marks(df.shape[0], chunk_size)
	for i in len(np.split(df, indices)):
		print ( 'save {} th sub-dataframe to csv'.format(i))
		df_sub = pd.DataFrame(np.split(df, indices)[i])
		# save to sub-csv 
		print ('sub csv : ' , df_sub.head())
		df_sub.to_csv('sub_csv_part_{}'.format(i))
	#return np.split(df, indices)


if __name__ == '__main__':
	df = load_csv(url)
	split(df,chunk_size)






