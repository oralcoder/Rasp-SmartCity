import cv2

img = cv2.imread('Lenna.png', cv2.IMREAD_COLOR)

h,w,color = img.shape
print(h,w,color)

cv2.imshow('IMAGE', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

px = img[511][511]
print(px)

roi = img[200:400, 250:350]
cv2.imshow('ROI', roi)
cv2.waitKey(0)
cv2.destroyAllWindows() 

imgBlurred = cv2.GaussianBlur(img, ksize=(3,3), sigmaX=0)
cv2.imshow('Blurred1', img)

imgBlurred = cv2.GaussianBlur(img, ksize=(9,9), sigmaX=0)
cv2.imshow('Blurred2', img)
cv2.waitKey(0)

cv2.destroyAllWindows() 

ret, thres = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)       # max_value | 0
cv2.imshow('BINARY', thres)
ret, thres = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)   # 0 | max_value
cv2.imshow('BINARY_INV', thres)
ret, thres = cv2.threshold(gray, 127, 255, cv2.THRESH_TRUNC)        # threshold | original
cv2.imshow('TRUNC', thres)
ret, thres = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO)       # original | 0
cv2.imshow('TOZERO', thres)
ret, thres = cv2.threshold(gray, 127, 255, cv2.THRESH_TOZERO_INV)   # 0 | original
cv2.imshow('TOZERO_INV', thres)
cv2.waitKey(0)
cv2.destroyAllWindows() 


# cv2.rectangle(img_name, start_point, end_point, line_color, thickness)
rect = cv2.rectangle(img, (240, 230), (350,380), (0,255,0), 3)

cv2.imshow('RECT', rect)
cv2.waitKey(0)
cv2.destroyAllWindows() 

#cv2.circle(img_name, center_point, radius, line_color, thickness)
circle = cv2.circle(img, (290, 300), 80, (255,0,0), 5)
cv2.imshow('CIRCLE', circle)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# cv2.putText(text, point(좌측하단), font, font_scale, color)
text = cv2.putText(img, "Hello World", (50, 80), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255))
cv2.imshow('TEXT', text)
cv2.waitKey(0)
cv2.destroyAllWindows() 
