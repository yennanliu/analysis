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
