import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15

camera.start_preview()


camera.start_recording('/tmp/video.h264', intra_period=25)
camera.wait_recording(15)
camera.stop_recording()

camera.stop_preview()

