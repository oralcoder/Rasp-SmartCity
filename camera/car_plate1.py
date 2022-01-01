import cv2

img = cv2.imread('car.png', cv2.IMREAD_COLOR)
cv2.imshow('CAR', img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

print(img.shape, img.size)

# (345, 558, 3) 577530

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(gray.shape, gray.size)

# (345, 558) 192510

cv2.imshow('GRAY', gray)
cv2.waitKey(0)
cv2.destroyAllWindows() 

blur = cv2.GaussianBlur(gray, ksize=(5, 5), sigmaX=0)
cv2.imshow('BLUR', blur)
cv2.waitKey(0)
cv2.destroyAllWindows() 

ret, thres = cv2.threshold(blur, 127, 255, cv2.THRESH_BINARY_INV)   # 0 | max_value
cv2.imshow('THRESH', thres)
cv2.waitKey(0)
cv2.destroyAllWindows() 

canny = cv2.Canny(thres, 0, 255)
cv2.imshow('CANNY', canny)
cv2.waitKey(0)
cv2.destroyAllWindows() 

contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

candidates = []
imgContour = img.copy()
for contour in contours:
  area = cv2.contourArea(contour)
  x,y,w,h = cv2.boundingRect(contour)
  rect_area=w*h
  aspect_ratio = w/h
  if(aspect_ratio>=0.2) & (aspect_ratio<=1) & (rect_area>=200) and (rect_area<=700):
    cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0, 255, 0), 1)
    candidates.append(contour)

cv2.imshow('CONTOUR', imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows() 
