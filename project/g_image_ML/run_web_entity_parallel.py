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
from multiprocessing import Pool, cpu_count
# UDF 
from utility import * 


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

def process_Pandas_data(func, df, num_processes=None):
    ''' Apply a function separately to each column in a dataframe, in parallel.'''
    
    # If num_processes is not specified, default to minimum(#columns, #machine-cores)
    if num_processes==None:
        num_processes = min(df.shape[1], cpu_count())
    
    # 'with' context manager takes care of pool.close() and pool.join() for us
    with Pool(num_processes) as pool:
        
        # we need a sequence of columns to pass pool.map
        seq = [df[col_name] for col_name in df.columns]
        
        # pool.map returns results as a list
        results_list = pool.map(func, seq)
        
        # return list of processed columns, concatenated together as a new dataframe
        return pd.concat(results_list, axis=1)


def load_df():
	try:
		df_10k_random = pd.read_csv('/Users/{}/Downloads/random_10K_image_urls_duplicate_variant_fixed.csv'.format(USER))
	except:
		df_10k_random = pd.read_csv('/home/{}/Downloads/random_10K_image_urls_duplicate_variant_fixed.csv'.format(USER))
	print (' *** output = *** ', len(df_10k_random))
	return  df_10k_random


#--------------------------------------------------


def main(output='csv'):
	# sample data 
	df_10k_random_ = df_10k_random.tail(30)
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
		df_10k_random_['image_property'] = df_10k_random_['url'].apply(lambda x : g_image_property(x))
		df_10k_random_['web_detection'] = df_10k_random_['url'].apply(lambda x : g_web_detection(x))
		# extract web entity information 
		df_10k_random_['web_entity'] = df_10k_random_['web_detection'].apply(lambda x : get_web_entity(x))
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
		frame = frame[['url', 'image_property', 'web_detection', 'web_entity','description', 'entityId', 'score']]
		#frame.to_csv('gcloud_web_entity_response.csv')
		return pd.DataFrame(frame)




if __name__ == '__main__':
	df_10k_random = load_df()
	main(output='csv')
	process_Pandas_data(main, df_10k_random , 10 )




