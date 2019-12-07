from flask import current_app
from google.cloud import storage
import six
from werkzeug import secure_filename
from werkzeug.exceptions import BadRequest
import json

def _get_storage_client():
    return storage.Client.from_service_account_json('daily-horoscopes-secret.json')

def upload_file(file_stream, filename, content_type):
    client = _get_storage_client()
    bucket = client.bucket('daily-horoscopes')
    blob = bucket.blob(filename)

    blob.upload_from_string(
        file_stream,
        content_type=content_type)

    url = blob.public_url

    if isinstance(url, six.binary_type):
        url = url.decode('utf-8')
    return url
    
def download_file():
    client = _get_storage_client()
    bucket = client.bucket('daily-horoscopes')
    blob = bucket.get_blob('daily-horoscopes.json')
    if blob:
        return blob.download_as_string()
    else:
        return {}
    
