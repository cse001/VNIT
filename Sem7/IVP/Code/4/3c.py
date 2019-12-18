import cv2
import numpy as np

img = cv2.imread("test 2.bmp", 0)
structuringElement = np.ones((7, 7), np.uint8)
opening = cv2.morphologyEx(img, cv2.MORPH_ELLIPSE, structuringElement)
img_dilation = cv2.dilate(opening, structuringElement, iterations=2)
structuringElement = np.ones((3, 3), np.uint8)
img_erosion = cv2.erode(img_dilation, structuringElement, iterations=1)
cv2.imshow('Image', img)
cv2.imshow('Improved', img_erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
