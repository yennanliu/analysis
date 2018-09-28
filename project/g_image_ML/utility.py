# python 3 

# gcloud 
from google.cloud import vision
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToDict

# OP 
import pandas as pd 
import numpy as np 
from tqdm import tqdm


#--------------------------------------------------
# config 
# save ur google cloud credentials below
credentials = service_account.Credentials.from_service_account_file('google_cloud_creds2.json')
client = vision.ImageAnnotatorClient(credentials=credentials)



#--------------------------------------------------
# OP FUNC #0 
# credentials

def auth_gcloud_ml(credentials_json_url):
    credentials = service_account.Credentials.from_service_account_file(credentials_json_url)
    client = vision.ImageAnnotatorClient(credentials=credentials)
    return credentials, client 



#--------------------------------------------------
# OP FUNC #1 
# QUERY CLOUD API 

"""

# https://cloud.google.com/vision/docs/other-features

1) Image properties : vision.enums.Feature.Type.IMAGE_PROPERTIES
2) Web entities : vision.enums.Feature.Type.WEB_DETECTION
3) Safe search :  vision.enums.Feature.Type.SAFE_SEARCH_DETECTION

"""

 
# QUERY GOOGLE ML API 
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


def g_label_detection(uri):
    """  
    Detects labels in the file located in Google Cloud Storage or on the Web.
    https://cloud.google.com/vision/docs/detecting-labels#vision-label-detection-gcs-python
    """
    #client = vision.ImageAnnotatorClient()
    image = vision.types.Image()
    image.source.image_uri = uri
    response = client.label_detection(image=image)
    print ('response : ', response)
    response_dict = MessageToDict(response)
    return response_dict
    #labels = response.label_annotations
    #print('Labels:')
    #for label in labels:
    # print(label.description)



#--------------------------------------------------
# OP FUNC #2 
# EXTRACT FEATURE 


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


def get_color_hex(image_property_response):
# in case some request got null response  
    try:
        return [ {'color' : i['color'], 'score':i['score'], 'pixelFraction':i['pixelFraction'] } for i in image_property_response['imagePropertiesAnnotation']['dominantColors']['colors' ]]
    except:
        return []


def expand_webentity(df):
    # convert web_entity to df  and merge/expand to original df 
    output = pd.DataFrame()
    list_ = []
    for i in range(len(df)):
      url_ = df.iloc[i]['url']
      df_web_entity = pd.DataFrame(df.iloc[i]['web_entity'])
      df_web_entity['url'] = url_
      # merge 
      df_to_merge = pd.merge(df, df_web_entity,  how='inner', left_on=['url'], right_on=['url'])
      list_.append(df_to_merge)
    output = pd.concat(list_)
    output = output.reset_index()
    return output






