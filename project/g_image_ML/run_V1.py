# python 3 

# gcloud 
from google.cloud import vision
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToDict

# OP 
import pandas as pd 
import numpy as np 
from tqdm import tqdm

# UDF 
from utility import *


#--------------------------------------------------
# op 

def load_csv(csv_url):
	pass  


#--------------------------------------------------


def main():
	df_10k_random = pd.read_csv('random_10K_image_urls.csv')
	credentials, client = auth_gcloud_ml(credentials_json_url)
	# query google vision api 
	df_10k_random['image_property'] = df_10k_random['url'].apply(lambda x : g_image_property(x))
	df_10k_random['web_detection'] = df_10k_random['url'].apply(lambda x : g_web_detection(x))
	# extract web entity information 
	df_10k_random['web_entity'] = df_10k_random['web_detection'].apply(lambda x : get_web_entity(x))
	# convert web_entity to df 
	frame = pd.DataFrame()
	list_ = []
	for i in tqdm(range(len(df_10k_random))):
		url_ = df_10k_random.iloc[i]['url']
		df_web_entity = pd.DataFrame(df_10k_random.iloc[i]['web_entity'])
		df_web_entity['url'] = url_
		# merge 
		df_10k_random_merge = pd.merge(df_10k_random, df_web_entity,  how='inner', left_on=['url'], right_on=['url'])
		list_.append(df_10k_random_merge)
	frame = pd.concat(list_)
	frame = frame.reset_index()
	print ('len of outcome df : ', len(frame) )
	return frame 


if __name__ == '__main__':
	main()














