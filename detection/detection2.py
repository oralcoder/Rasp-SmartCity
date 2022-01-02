import numpy as np
import time
import cv2
import os

with open('coco_class_names.txt', 'r', encoding='utf-8') as f:
    classNames = f.read().split('\n')

COLORS = np.random.uniform(0,255, size=(len(classNames), 3))

conf_threshold = 0.5
nms_threshold = 0.4

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    exit()

net = cv2.dnn.readNet('yolov3-tiny.weights', 'yolov3-tiny.cfg')
ln = net.getLayerNames()
ln = [ln[i-1] for i in net.getUnconnectedOutLayers()]

while True:
    ret, img = cap.read()
    if not ret:
        exit()
    img_height, img_width, _ = img.shape

        # create blob from image
        # yolo는 320*320, 416*416, 609*609 크기 허용
    blob = cv2.dnn.blobFromImage(img, 1/255.0, (320,320), (0,0,0), True, crop=False)
        # set the blob to the model
    net.setInput(blob)
        # forward pass through the model to carry out the detection
    output = net.forward(ln)

    boxes = []
    confidences = []
    classIDs = []

    for out in output:
            for detection in out:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > .3:
                    print(classID)
                    centerX = int(detection[0]*img_width)
                    centerY = int(detection[1]*img_height)
                    w = int(detection[2]*img_width)
                    h = int(detection[3]*img_height)
                    x = centerX - w / 2
                    y = centerY - h /2
                    classIDs.append(classID)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

    # 노이즈 제거 (Non Maximum Suppression) 
    # NMSBoxes(boxes, confidences, confThreshold, nmsThreshold
    # confThreshold: 
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.2)
    print(idxs)
    for i in idxs:
        box = boxes[i]
        x = int(box[0])
        y = int(box[1])
        w = int(box[2])
        h = int(box[3])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(img, classNames[classIDs[i]], (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))

    cv2.imshow('img', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
