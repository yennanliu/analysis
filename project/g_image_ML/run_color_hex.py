# python 3 



######################################################

"""

QUERY THE GCLOUD VISION API BUT WITH 1K variant  DATA  

- GET THE RGB HEX FEATURE i.e. '(119, 76, 41)' or hez

"""

######################################################

# gcloud 
from google.cloud import vision
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToDict

# OP 
import pandas as pd 
import numpy as np 

# UDF 
from utility import * 

#--------------------------------------------------
# config 
# save ur google cloud credentials below
try:
    credentials = service_account.Credentials.from_service_account_file('/Users/yennanliu/creds/google_cloud_creds2.json')
except:
    credentials = service_account.Credentials.from_service_account_file('/home/yennanliu/creds/google_cloud_creds2.json')
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

#--------------------------------------------------



df_10k_random = pd.read_csv('/home/yennanliu/random_10K_image_urls_duplicate_variant_fixed.csv')
# sample data 
#df_10k_random_ = df_10k_random.tail(5)
df_10k_random_ = df_10k_random.copy()
print ('len of df_10k_random_', len(df_10k_random_))
# query google vision api 
df_10k_random_['image_property'] = df_10k_random_['url'].apply(lambda x : g_image_property(x))
df_10k_random_['web_detection'] = df_10k_random_['url'].apply(lambda x : g_web_detection(x))
df_10k_random_['lebel_detection'] = df_10k_random_['url'].apply(lambda x : g_label_detection(x))
# extract web entity information 
df_10k_random_['web_entity'] = df_10k_random_['web_detection'].apply(lambda x : get_web_entity(x))
# extract color hex  information 
df_10k_random_['color_hex'] = df_10k_random_['image_property'].apply(lambda x : get_color_hex(x))


# convert color_hex to df 
frame = pd.DataFrame()
list_ = []

# expand color_hex
for i in tqdm(range(len(df_10k_random_))):
  url_ = df_10k_random_.iloc[i]['url']
  df_color_hex = pd.DataFrame(df_10k_random_.iloc[i]['color_hex'])
  df_color_hex['url'] = url_
  # merge 
  df_10k_random_merge = pd.merge(df_10k_random_, df_color_hex,  how='inner', left_on=['url'], right_on=['url'])
  list_.append(df_10k_random_merge)
frame = pd.concat(list_)
frame = frame.reset_index()
# extract each color to column 
frame['red'] = frame['color'].apply(lambda x :  extract_color(x,'red'))
frame['green'] = frame['color'].apply(lambda x :  extract_color(x,'green'))
frame['blue'] = frame['color'].apply(lambda x :  extract_color(x,'blue'))
# SAVE TO CSV 
frame = frame[['url', 'image_property', 'web_detection', 'lebel_detection',
       'web_entity', 'color_hex', 'color', 'pixelFraction', 'score', 'red',
       'green', 'blue']]
frame.to_csv('api_color_hex_response.csv')







