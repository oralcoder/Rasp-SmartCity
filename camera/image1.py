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
