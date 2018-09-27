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
	df_10k_random = pd.read_csv('random_10K_image_urls_duplicate_variant_fixed.csv')
	credentials, client = auth_gcloud_ml(credentials_json_url)
	# query google vision api 
	df_10k_random['image_property'] = df_10k_random['url'].apply(lambda x : g_image_property(x))
	df_10k_random['web_detection'] = df_10k_random['url'].apply(lambda x : g_web_detection(x))
	df_10k_random['lebel_detection'] = df_10k_random['url'].apply(lambda x : g_label_detection(x))
	# extract web entity information 
	df_10k_random['web_entity'] = df_10k_random['web_detection'].apply(lambda x : get_web_entity(x))

	# sample / copy df here 
	df_10k_random_ = df_10k_random.head(10)
	df_10k_random_copy = df_10k_random.copy()

	######## OUTPUT PART 1 ) convert web_entity to df  ########
	frame1 = pd.DataFrame()
	list_ = []
	for i in tqdm(range(len(df_10k_random))):
		url_ = df_10k_random.iloc[i]['url']
		df_web_entity = pd.DataFrame(df_10k_random.iloc[i]['web_entity'])
		df_web_entity['url'] = url_
		# merge 
		df_10k_random_merge1 = pd.merge(df_10k_random, df_web_entity,  how='inner', left_on=['url'], right_on=['url'])
		list_.append(df_10k_random_merge1)
	frame1 = pd.concat(list_)
	frame1 = frame1.reset_index()
	print ('len of outcome df : ', len(frame) )
	frame1.to_csv('gcloud_response_web_entity.csv')
	
	######## OUTPUT PART 2 ) convert lebel_detection  to df  ########
	frame2 = pd.DataFrame()
	list_ = []
	for i in tqdm(range(len(df_10k_random))):
	url_ = df_10k_random.iloc[i]['url']
	df_lebel_detection = pd.DataFrame(df_10k_random.iloc[i]['lebel_detection'])
	df_lebel_detection['url'] = url_
	# merge 
	df_10k_random_merge2 = pd.merge(df_10k_random, df_lebel_detection,  how='inner', left_on=['url'], right_on=['url'])
	list_.append(df_10k_random_merge2)
	frame2 = pd.concat(list_)
	frame2 = frame2.reset_index()
	frame2.to_csv('gcloud_lebel_detection.csv')
	return frame1, frame2 



if __name__ == '__main__':
	main()














