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

#--------------------------------------------------
# config 
# save ur google cloud credentials below
credentials = service_account.Credentials.from_service_account_file('/home/yennanliu/google_cloud_creds2.json')
client = vision.ImageAnnotatorClient(credentials=credentials)


#--------------------------------------------------
# help func 
# import form utility.py 

"""

# https://cloud.google.com/vision/docs/other-features

1) Image properties : vision.enums.Feature.Type.IMAGE_PROPERTIES
2) Web entities : vision.enums.Feature.Type.WEB_DETECTION
3) Safe search :  vision.enums.Feature.Type.SAFE_SEARCH_DETECTION

"""

#--------------------------------------------------



df_10k_random = pd.read_csv('/home/yennanliu/random_10K_image_urls_duplicate_variant_fixed.csv')
# sample data 
df_10k_random_ = df_10k_random.tail(5)
#df_10k_random_ = df_10k_random.copy()
print ('len of df_10k_random_', len(df_10k_random_))

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
frame = frame[['url', 'image_property', 'web_detection', 'web_entity',
       'description', 'entityId', 'score']]

frame.to_csv('gcloud_web_entity_response.csv')









