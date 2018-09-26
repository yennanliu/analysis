# python3
# ref  https://cloud.google.com/vision/docs/libraries#client-libraries-install-python

 
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# ------------------------------------------------ 
# config 
# Instantiates a client
client = vision.ImageAnnotatorClient()



# ------------------------------------------------
# OP func   

def main():
	# The name of the image file to annotate
	file_name = os.path.join(
	    os.path.dirname(__file__),
	    'resources/wakeupcat.jpg')

	# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
	    content = image_file.read()

	image = types.Image(content=content)

	# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

	print('Labels:')
	for label in labels:
	    print(label.description)
	return labels


if __name__ == '__main__':
	main()





