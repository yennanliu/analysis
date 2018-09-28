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


"""

# https://cloud.google.com/vision/docs/other-features

1) Image properties : vision.enums.Feature.Type.IMAGE_PROPERTIES
2) Web entities : vision.enums.Feature.Type.WEB_DETECTION
3) Safe search :  vision.enums.Feature.Type.SAFE_SEARCH_DETECTION

"""



def call_google_image_api(url,type):
    response = client.annotate_image({
    'image': {'source': {'image_uri': url}},
    'features': [{'type': type}],})
    print ('response : ', response)
    response_dict = MessageToDict(response)
    return response_dict



def g_face_detection(url):
    response = client.annotate_image({
    'image': {'source': {'image_uri': url}},
    'features': [{'type': vision.enums.Feature.Type.FACE_DETECTION}],})
    print ('response : ', response)
    response_dict = MessageToDict(response)
    return response_dict


def g_image_property(url):
    response = client.annotate_image({
    'image': {'source': {'image_uri': url}},
    'features': [{'type': vision.enums.Feature.Type.IMAGE_PROPERTIES}],})
    print ('response : ', response)
    response_dict = MessageToDict(response)
    return response_dict
  
  
def g_web_detection(url):
    response = client.annotate_image({
    'image': {'source': {'image_uri': url}},
    'features': [{'type': vision.enums.Feature.Type.WEB_DETECTION}],})
    print ('response : ', response)
    response_dict = MessageToDict(response)
    return response_dict



#--------------------------------------------------



def get_web_entity(web_property_response):
  # in case some request got null response  
  try:
    return [i for i in web_property_response['webDetection']['webEntities'] ]
  except:
    return []



def get_labelAnnotations(lebel_detection_response):
  # in case some request got null response  
  try:
    return [i for i in lebel_detection_response['labelAnnotations']]
  except:
    return []


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

frame.to_csv('gcloud_100k_web_entity_response.csv')









