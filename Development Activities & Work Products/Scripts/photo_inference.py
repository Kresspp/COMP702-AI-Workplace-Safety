# Importing needed libraries
import numpy as np
import cv2


COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

labeles = []
with open('/Users/juliaborlase/Desktop/uni_code/model_for_testing_PPE/obj.names', 'r') as f:
    labeles = [line.strip() for line in f.readlines()]

net = cv2.dnn_DetectionModel("/Users/juliaborlase/Desktop/uni_code/model_for_testing_PPE/yolov4-tiny-safety-v1_6.cfg", "/Users/juliaborlase/Desktop/uni_code/model_for_testing_PPE/yolov4-tiny-safety-v1_6_best.weights")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)
net.setInputSize(960, 544)
net.setInputScale(1.0 / 255)
net.setInputSwapRB(True)

image = cv2.imread("shapely_test_images/person_noPPE.jpg")

classes, confidences, boxes = net.detect(image, confThreshold=0.1, nmsThreshold=0.4)


for (classid, score, box) in zip(classes, confidences, boxes):
    color = COLORS[int(classid) % len(COLORS)]

    label = "%s : %f" % (labeles[classid], score)

    cv2.rectangle(image, box, color, 2)
    print(box)
    cv2.putText(image, label, (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
cv2.imshow("detections", image)
cv2.waitKey(0) 