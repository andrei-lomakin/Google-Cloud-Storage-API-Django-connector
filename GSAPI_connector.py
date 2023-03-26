# Created by Andrei Lomakin
# Teoglobal Solutions
# https://teo-global.com/
# Insert this code into your business logic

from google.cloud import storage

# Instantiate a client object
client = storage.Client.from_service_account_json('/path/to/your/credentials.json')

# Get a reference to a bucket
bucket = client.get_bucket('your-bucket-name')

# Upload a file to the bucket
blob = bucket.blob('path/to/your/file')
with open('/path/to/your/local/file', 'rb') as f:
    blob.upload_from_file(f)

# Download a file from the bucket
blob = bucket.blob('path/to/your/file')
with open('/path/to/your/local/file', 'wb') as f:
    blob.download_to_file(f)
