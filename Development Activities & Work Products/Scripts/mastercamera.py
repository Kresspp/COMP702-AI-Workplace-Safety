import picamera
import time
from subprocess import call
import os
from azure.storage.blob import ContainerClient
import sys
sys.path.append('/home/inviol/Desktop/31-10-2022')
import event_api
import shapely_video

event_id = event_api.create_event()

def capture_video():
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 15
    
    #adjusts preview window so that it doesn't take up the whole screen
    camera.start_preview(fullscreen=False, window=(100,200,300,400))
    
    print("Recording...")
    camera.start_recording('/home/inviol/inviol_videos/tmp.h264', intra_period=15)
    camera.wait_recording(1)             
    camera.stop_recording()
    camera.stop_preview()
    print("Recording Complete!")

    #converts h264 file to mp4
def convert(file_h264, file_mp4):
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)
    print("\r\nRasp_Pi => Video Converted! \r\n")

    #fill conn_str and container_name variables to azure blob account key and folder name respectively
def upload_database():
    filename = str(event_id)
    print("FILE NAME AFTER EVENT_ID: " + filename)
    os.rename("/home/inviol/inviol_videos/tmp.mp4", '/home/inviol/inviol_videos/out_0.mp4')
    conn_str = "DefaultEndpointsProtocol=https;AccountName=steventdatadev001;AccountKey=Fkuf6xrr04sYFI2o5FGpf7UIzmbqvs4l5zmQ8z2QE0a8qPo76UlTXsk8hfdE36RQ1ByRktJ9gK2VFDsN/GrGcA==;EndpointSuffix=core.windows.net"
    container_name = "events"

    #blob_client should be set to the name of the video
    container_client = ContainerClient.from_connection_string(conn_str, container_name)
    blob_client = container_client.get_blob_client("vulcan/{}/out_0.mp4".format(filename))

    #Path file here
    with open('/home/inviol/inviol_videos/out_0.mp4', 'rb') as data:
        blob_client.upload_blob(data)
    print("Video has been uploaded!")
    
    # Send video to inference script
    print("FILE NAME: " + filename)
    shapely_video.get_video(filename)

capture_video()
convert('/home/inviol/inviol_videos/tmp.h264', '/home/inviol/inviol_videos/tmp.mp4')
upload_database()
