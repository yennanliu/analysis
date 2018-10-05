# python 3 



######################################################

"""

QUERY THE GCLOUD VISION API BUT WITH 1K variant/duplocate  DATA  

- LABLE_ANNOTATION

"""

######################################################




# gcloud 
from google.cloud import vision
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToDict

# OP 
import pandas as pd 
import numpy as np 
import getpass
import argparse
import os
from os import listdir
from os.path import isfile, join                                                                       
# UDF 
from utility import * 




print ('*'*70)
print (' run "python run_web_entity_parallel.py  --h" for help msg ')
print ('*'*70)

# ----------------------------------------------
# get args 
parser = argparse.ArgumentParser()
#parser.add_argument('--url', required=True, help='The --csvurl to load')
parser.add_argument('--csvurl', required=True, help='The --csvurl to load')
args = parser.parse_args()
#url  = args.url 
csvurl  = args.csvurl 
# ----------------------------------------------


#--------------------------------------------------
# config 
# save ur google cloud credentials below
USER = getpass.getuser()
try:
    credentials = service_account.Credentials.from_service_account_file('/Users/{}/creds/google_cloud_creds2.json'.format(USER))
except:
    credentials = service_account.Credentials.from_service_account_file('/home/{}/creds/google_cloud_creds2.json'.format(USER))
client = vision.ImageAnnotatorClient(credentials=credentials)
print ('client : ', client)


#--------------------------------------------------
# help func 
# import form utility.py 

"""

# https://cloud.google.com/vision/docs/other-features

1) Image properties : vision.enums.Feature.Type.IMAGE_PROPERTIES
2) Web entities : vision.enums.Feature.Type.WEB_DETECTION
3) Safe search :  vision.enums.Feature.Type.SAFE_SEARCH_DETECTION

"""

# multiprocessing
# https://maxpowerwastaken.github.io/blog/multiprocessing-with-pandas/

#--------------------------------------------------


def main(csvurl,output='csv'):
	print (' *** csvurl :  *** ' , csvurl )
	df_10k_random_ = pd.read_csv(csvurl)
	# sample data 
	#df_10k_random_ = df_10k_random_.tail(30)
	#df_10k_random_ = df_10k_random.copy()
	print ('len of df_10k_random_', len(df_10k_random_))
	# ----------------- output as json -----------------
	if output=='json':
		output_data=[]
		for i, row in df_10k_random_.iterrows():
			response = g_image_property(df_10k_random.iloc[i].url)
			response['url'] = df_10k_random.iloc[i].url
			output_data.append(response)
		df_json_csv= pd.DataFrame({'json' : output_data })
		#df_json_csv.to_json('gcloud_web_entity_response.json',orient='records')
		print ('df_json_csv :', df_json_csv)
		return df_json_csv

	# ----------------- output as csv  -----------------
	else:
		# query google vision api
		########### only query  needed api ###########

		#df_10k_random_['image_property'] = df_10k_random_['url'].apply(lambda x : g_image_property(x))
		df_10k_random_['web_detection'] = df_10k_random_['url'].apply(lambda x : g_web_detection(x))
		# extract web entity information 
		df_10k_random_['web_entity'] = df_10k_random_['web_detection'].apply(lambda x : get_web_entity(x))
		
		########### only query  needed api ###########

		# convert web_entity to df 
		frame = pd.DataFrame()
		list_ = []
		#for i in range(5):
		for i in range(len(df_10k_random_)):
			url_ = df_10k_random_.iloc[i]['url']
			df_web_entity = pd.DataFrame(df_10k_random_.iloc[i]['web_entity'])
			df_web_entity['url'] = url_
			# merge 
			df_10k_random_merge = pd.merge(df_10k_random_, df_web_entity,  how='inner', left_on=['url'], right_on=['url'])
			list_.append(df_10k_random_merge)
		frame = pd.concat(list_)
		frame = frame.reset_index()
		#frame = frame[['url', 'image_property', 'web_detection', 'web_entity','description', 'entityId', 'score']]
		frame = frame[['url','web_detection','web_entity','description', 'entityId', 'score']]
		to_save_url_ = csvurl.replace(csvurl.split('/')[-1], '{}_{}'.format('response',csvurl.split('/')[-1]))
		print (' *** to_save_url_  :  *** '  , to_save_url_)
		frame.to_csv(to_save_url_)
		return pd.DataFrame(frame)




if __name__ == '__main__':
	main(csvurl,output='csv')




