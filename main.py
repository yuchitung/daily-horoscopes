from google.cloud import storage
import json
    
def download_file(request):
    client = _get_storage_client()
    bucket = client.bucket('daily-horoscopes')
    blob = bucket.get_blob('daily-horoscopes.json')
    if blob: 
        json_data_string = blob.download_as_string()
        return json_data_string
    else:
        return {}
    

def _get_storage_client():
    return storage.Client(project='daily-horoscopes')
