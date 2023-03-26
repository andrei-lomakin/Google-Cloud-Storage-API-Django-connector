# Google-Cloud-Storage-API-Django-connector
Google Storage API connector to django web site

I offer you a simple way to connect the Google data storage to your django project. Upload and download files from your project to remote Google servers.
To connect your Django web application to Google Cloud Storage API, you can use the `google-cloud-storage` Python client library.

First, you need to install the library using pip:
```python
pip install google-cloud-storage
```

Next, you need to authenticate your application with Google Cloud Storage API by creating a service account and providing its credentials. You can do this by following these steps:

Go to the Google Cloud Console and select your project.
Click on the Navigation menu and select APIs & Services > Credentials.
Click on Create credentials and select Service account key.
Select a service account and a key type (JSON).
Click on Create to download the JSON key file.
Store the key file in a secure location, outside of your project directory.
Now that you have the authentication credentials, you can use the google-cloud-storage library to access your Google Cloud Storage buckets from your Django web application. Here in the `GSAPI_connector.py` file is an example of how to do this.
