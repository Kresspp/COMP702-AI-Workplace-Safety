from azure.storage.blob import ContainerClient
import os
import sys

#Current connection string is to the test blob storage account
#Fill emtpy conn_str variable with azure blob storage account key
conn_str = ""
container_name = "testvideos"

#blob_client should be set to the name of the video
container_client = ContainerClient.from_connection_string(conn_str, container_name)
blob_client = container_client.get_blob_client("video5.mp4")

#Path file here
with open('/home/inviol/inviol_videos/video5.mp4', 'rb') as data:
    blob_client.upload_blob(data)
print("Video has been uploaded!")
