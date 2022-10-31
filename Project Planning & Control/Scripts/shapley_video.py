# Shapely video script to draw bounding boxes on the video captured by the raspberry pi

import numpy as np
import cv2
import time
from shapely.geometry import Polygon
from azure.storage.blob import ContainerClient
import os
# from . import event_api

conn_string = ""

# Get video from file path were the video name is video blob
def get_video(blob_client):
    video_blob = os.path.basename(blob_client)
    draw_bounding_box(video_blob)
    return video_blob

    
def draw_bounding_box():
    # Setting the colours for the bounding boxes
    COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

    # Initialising lists for polygons and reading in the label names from the model
    polygons = []
    labeles = []
    with open('/Users/juliaborlase/Desktop/uni_code/model_for_testing_PPE/obj.names', 'r') as f:
        labeles = [line.strip() for line in f.readlines()]

    # Model settings
    net = cv2.dnn_DetectionModel("/Users/juliaborlase/Downloads/yolov4-tiny-obj.cfg", "/Users/juliaborlase/Downloads/yolov4-tiny-obj_best.weights")
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
    net.setInputSize(640, 480)
    net.setInputScale(2.0 / 255)
    net.setInputSwapRB(True)

    # Getting and setting the video 
    # cap = cv2.VideoCapture("/Users/juliaborlase/Desktop/uni_code/out_0.mp4")
    cap = cv2.VideoCapture("/Users/juliaborlase/Desktop/uni_code/out_0.mp4")


    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('out_bb_0.mp4', fourcc, 20, (640,480))

    # While the video is be read
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            image = frame #set the image variable to the current frame
            start = time.time() #start drawing
            classes, confidences, boxes = net.detect(image, confThreshold=0.1, nmsThreshold=0.4)
            roi = [(1704, 720),
            (2852, 860),
            (2568, 1736),
            (1520, 1696),
            (1276, 1296),
            ]

            start_drawing = time.time()
        
            for (classid, score, box) in zip(classes, confidences, boxes):
                color = COLORS[int(classid) % len(COLORS)]
                coordinates = [(box[0], box[1]), 
                        (box[0] + box[2], box[1]), 
                        (box[0] + box[2], box[1] + box[3]),
                        (box[0], box[1] + box[3]), 
                        ]
                poly1 = Polygon(roi)
                poly2 = Polygon(coordinates)

                # print(f"coordinates: {coordinates} ")
                polygons.append(poly2)

                label = "%s : %f" % (labeles[classid], poly2.area)

                cv2.putText(image, label, (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                image = cv2.polylines(image, [np.array(coordinates)], 
                        True, color, 2)

                poly2 = poly1     # Making the coordinates equal to the roi
    
                end_drawing = time.time()
            
                # Exception Logic
                for i in range(len(polygons)):
                    for j in range(i + 1, len(polygons)):
                        if(polygons[j].contains(polygons[i])):
                            print("Person is wearing PPE")
                        if(polygons[i].contains(polygons[j])):
                            print("Person is wearing PPE")
                        else:
                            print("Person is not weating PPE - send alert!")


            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()

    out.release()
    print("Video Done!")

    cv2.destroyAllWindows()

# Uploading video to azure blob storage based on event id


# Drawing boudning box video based on the most recent video from the camera
draw_bounding_box()

# Uploading the videos to the Azure storage and Event API
# upload_bounding_box()
# event_api.put_event_bounding_box()