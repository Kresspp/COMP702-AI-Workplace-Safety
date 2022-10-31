from picamera import PiCamera
from time import sleep
from subprocess import call

#camera = PiCamera()
#camera.resolution = (640, 480)
#camera.framerate = 15

def convert(file_h264, file_mp4):
    #camera.start_recording(file_h264)
    #sleep(15)
    #camera.stop_recording
    #print("Rasp_Pi => Video Recorded! \r\n")
    #Convert
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)
    print("\r\nRasp_Pi => Video Converted! \r\n")
    
convert('/tmp/video.h264', '/tmp/video.mp4')