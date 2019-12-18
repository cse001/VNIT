import numpy as np
import cv2
import math

img=cv2.imread('ball.bmp',1)
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
orangeLower = (5, 50, 50)
orangeUpper = (15, 255, 255)
mask = cv2.inRange(hsv, orangeLower, orangeUpper)
structuringElement = np.ones((3,3), np.uint8)
mask = cv2.dilate(mask, structuringElement, iterations=5)
structuringElement = np.ones((11,11), np.uint8)
mask = cv2.erode(mask, structuringElement, iterations=2)
mask = cv2.dilate(mask, structuringElement, iterations=2)
cv2.imshow('circles', mask)
im2, contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for c in contours:
   M = cv2.moments(c)
   cX = int(M["m10"] / M["m00"])
   cY = int(M["m01"] / M["m00"])
   # cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)
   cv2.line(img,(cX - 3, cY -3),(cX + 3, cY + 3),(0,0,0),3)
   cv2.line(img,(cX + 3, cY -3),(cX - 3, cY + 3),(0,0,0),3)
   cv2.imshow("Image", img)
   cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
