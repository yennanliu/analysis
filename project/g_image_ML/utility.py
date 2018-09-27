# python 3 

# gcloud 
from google.cloud import vision
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToDict

# OP 
import pandas as pd 
import numpy as np 
from tqdm import tqdm
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine


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


def g_label_detection(url):
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
    #    print(label.description)





def call_google_handwritten_api(uri):

	"""
	# ref 
	https://cloud.google.com/vision/docs/ocr
	
	# put ur image url above 
	# e.g. https://s-i.huffpost.com/gen/2165258/images/n-NY-TIMES-ERROR-628x314.jpg

	"""

    """Detects handwritten characters in the file located in Google Cloud
    Storage.

    Args:
    uri: The path to the file in Google Cloud Storage (gs://...)
    """
    from google.cloud import vision_v1p3beta1 as vision
    credentials = service_account.Credentials.from_service_account_file('google_cloud_creds2.json')
    
    
    client = vision.ImageAnnotatorClient(credentials=credentials)
    image = vision.types.Image()
    image.source.image_uri = uri

    # Language hint codes for handwritten OCR:
    # en-t-i0-handwrit, mul-Latn-t-i0-handwrit
    # Note: Use only one language hint code per request for handwritten OCR.
    image_context = vision.types.ImageContext(
        language_hints=['en-t-i0-handwrit'])

    response = client.document_text_detection(image=image,
                                              image_context=image_context)

    print('Full Text: {}'.format(response.full_text_annotation.text))
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            print('\nBlock confidence: {}\n'.format(block.confidence))

            for paragraph in block.paragraphs:
                print('Paragraph confidence: {}'.format(
                    paragraph.confidence))

                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    print('Word text: {} (confidence: {})'.format(
                        word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {} (confidence: {})'.format(
                            symbol.text, symbol.confidence))


#--------------------------------------------------
# OP FUNC #2 
# EXTRACT FEATURE 


def get_web_entity(web_property_response):
  # in case some requesr got null response  
  try:
    return [i for i in web_property_response['webDetection']['webEntities'] ]
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




#--------------------------------------------------
# OP FUNC #2 
# INTERACT WITH SNOWFLAKE 


def connect_to_snowflake(snowflake_credentials):
    """
    doc : 
    https://docs.snowflake.net/manuals/user-guide/sqlalchemy.html#parameters-and-behavior

    """
    engine = create_engine(URL(
    #account = account,
    #region = region,
    user = user,
    password = password,
    database = database,
    #schema = schema,
    warehouse = warehouse,
    #role=role,
    ))

    connection = engine.connect()

    return engine, connection

def dump_df_to_snowflake(df,table,engine, connection):
    # need to modify later 
    try:
        df.to_sql(name=table,con=engine, if_exists='append')
        print ('dump OK ')
    except exception as e:
        print (e)
        print ('dump failed')






