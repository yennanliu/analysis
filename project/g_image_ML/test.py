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
#parser.add_argument('--url', required=True, help='The --csvurl to load')
parser.add_argument('--csvurl', required=True, help='The --csvurl to load')

args = parser.parse_args()

#url  = args.url 
csvurl  = args.csvurl 

# ----------------------------------------------

print (' ***  csvurl : *** ', csvurl)
df=pd.read_csv( csvurl)
print (' *** len(df) : *** ', len(df))
print (df.head(2))

"""
sub_url = '/' + '/'.join([ i for i in url.split('/')[1:-1]]) + '/'  
file_list = [ i for i in listdir(sub_url) if 'sub' in i ]
csvurl =  [ sub_url + i for i in listdir(sub_url) if 'sub' in i ]
print (' ***  csvurl : *** ', csvurl)
df=pd.read_csv( csvurl)
print (' *** len(df) : *** ', len(df))
print (df.head(2))
"""

"""
sub_url = '/' + '/'.join([ i for i in url.split('/')[1:-1]]) + '/'  
for sub in [ i for i in listdir(sub_url) if 'sub' in i ]:
	print ('sub : ', sub)
	df=pd.read_csv( sub_url + sub)
	print (' *** len(df) : *** ', len(df))
	print (df.head(2))
"""


