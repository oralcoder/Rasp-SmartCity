import cv2
import numpy as np

with open('coco_class_names.txt', 'r') as f:
    class_names = f.read().split('\n')

model = cv2.dnn.readNet(model='frozen_inference_graph.pb', config='ssd_mobilenet_v2_coco_2018_03_29.pbtxt.txt',framework='TensorFlow')

image = cv2.imread('image-bike.jpg')
image_height, image_width, _ = image.shape

blob = cv2.dnn.blobFromImage(image=image, size=(300, 300), mean=(104, 117, 123), swapRB=True)

model.setInput(blob)

output = model.forward()


for detection in output[0, 0, :, :]:

    confidence = detection[2]
    if confidence > .4:
        class_id = detection[1]
        class_name = class_names[int(class_id)-1]

        box_x = detection[3] * image_width
        box_y = detection[4] * image_height
        box_width = detection[5] * image_width
        box_height = detection[6] * image_height

        cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (0,255,0), thickness=2)
        cv2.putText(image, class_name, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

cv2.imshow('image', image)
cv2.waitKey(0)

cv2.destroyAllWindows()