# python 3

"""

modify from  https://stackoverflow.com/questions/37003862/google-cloud-storage-how-to-upload-a-file-from-python-3

"""


from google.cloud import storage

def upload_to_bucket(blob_name, path_to_file, bucket_name, cred_url):
	"""

    blob_name : fine name for uploaded file at gcs 
    path_to_file : the path of file been uploaded 
    bucket_name : gcs bucket name, e.g. data_dev_yen from gs://data_dev_yen/ 
    cred_url : crendential access gcs account 

	"""
    """

    Upload data to a bucket
    # Explicitly use service account credentials by specifying the private key
    # file.

    """
    storage_client = storage.Client.from_service_account_json(cred_url)
    #print(buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(path_to_file)
    #returns a public url
    return blob.public_url





