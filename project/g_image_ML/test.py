# python3 

# python 3 

import argparse
import os
from os import listdir
from os.path import isfile, join                                                                       
from multiprocessing import Pool                                                
import pandas as pd        




# ----------------------------------------------
# get args 
parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True, help='The url to load csv')
parser.add_argument('--csv', required=True, help='The csv to load')
args = parser.parse_args()

url  = args.url 
csv  = args.csv
# ----------------------------------------------
sub_url = '/' + '/'.join([ i for i in url.split('/')[1:-1]]) + '/'  
for sub in [ i for i in listdir(sub_url) if 'sub' in i ]:
	print ('sub : ', sub)
	df=pd.read_csv( sub_url + sub)
	print (' *** len(df) : *** ', len(df))
	print (df.head(2))



