from google.cloud import vision
from google.oauth2 import service_account

from utility import * 



# config 
credentials = service_account.Credentials.from_service_account_file('creds.json')
client = vision.ImageAnnotatorClient(credentials=credentials)


# test 1 

def test1():
	response = client.annotate_image({
	'image': {'source': {'image_uri': 'https://cdn.notonthehighstreet.com/campaigns/images/homepage-2017/partners-01-week-24.jpg'}},
	'features': [{'type': vision.enums.Feature.Type.FACE_DETECTION}],})
	print(response)


def test2():
	pass 
