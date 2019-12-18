import cv2
import numpy as np

img = cv2.imread("test1.bmp", 0)
cv2.imshow('Image', img)
structuringElement = np.ones((5, 5), np.uint8)
eroded = cv2.erode(img, structuringElement, iterations=5)
dilated = cv2.dilate(eroded, structuringElement, iterations=3)
cv2.imshow('Improved', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()
