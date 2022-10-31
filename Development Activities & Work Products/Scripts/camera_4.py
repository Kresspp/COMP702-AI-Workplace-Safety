import picamera
from time import sleep
from subprocess import call

def capture_video():
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 15
    
    camera.start_preview()
    camera.start_recording('/home/inviol/inviol_videos/video5.h264', intra_period=15)
    camera.wait_recording(30)
    camera.stop_recording()
    camera.stop_preview()

def convert(file_h264, file_mp4):
    command = "MP4Box -add " + file_h264 + " " + file_mp4
    call([command], shell=True)
    print("\r\nRasp_Pi => Video Converted! \r\n")

capture_video()
convert('/home/inviol/inviol_videos/video5.h264', '/home/inviol/inviol_videos/video5.mp4')
