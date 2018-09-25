# python 3 



# gcloud 
from google.cloud import vision
from google.oauth2 import service_account

# OP 
import pandas as pd 
import numpy as np 

#--------------------------------------------------
# config 
# save ur google cloud credentials below
credentials = service_account.Credentials.from_service_account_file('google_cloud_creds2.json')
client = vision.ImageAnnotatorClient(credentials=credentials)


#--------------------------------------------------
# help func 

def call_google_image_api(url):
	response = client.annotate_image({
	'image': {'source': {'image_uri': url}},
	'features': [{'type': vision.enums.Feature.Type.FACE_DETECTION}],})
	print ('response : ', response)
	return response






#--------------------------------------------------
