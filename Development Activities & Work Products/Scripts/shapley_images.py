# Importing needed libraries
import numpy as np
import cv2
import time
from shapely.geometry import Polygon

# Setting the colours for the bounding boxes
COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

# Initialising lists for polygons and reading in the label names from the model
polygons = []
labeles = []
with open('/Users/juliaborlase/Desktop/uni_code/model_for_testing_PPE/obj.names', 'r') as f:
    labeles = [line.strip() for line in f.readlines()]

# Model settings
net = cv2.dnn_DetectionModel("/Users/juliaborlase/Desktop/uni_code/model_for_testing_PPE/yolov4-tiny-safety-v1_6.cfg", "/Users/juliaborlase/Desktop/uni_code/model_for_testing_PPE/yolov4-tiny-safety-v1_6_best.weights")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
net.setInputSize(960, 544)
net.setInputScale(1.0 / 255)
net.setInputSwapRB(True)

# Change to video from blob storage
image = cv2.imread("shapely_test_images/person_noPPE.jpg") 

# Drawing Bounding Boxes and Labels on Image
start = time.time()
classes, confidences, boxes = net.detect(image, confThreshold=0.1, nmsThreshold=0.4)
end = time.time()

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

    print(f"coordinates: {coordinates} ")
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
        # print(polygons[i])
        # print(polygons[j])
        if(polygons[j].contains(polygons[i])):
            print("Person is wearing PPE")
        if(polygons[i].contains(polygons[j])):
            print("Person is wearing PPE")
        else:
            print("Person is not weating PPE - send alert!")

# Outputting Image 
scale_percent = 60 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("detections", resized)
cv2.waitKey(0) 