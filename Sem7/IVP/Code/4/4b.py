import numpy as np
import cv2
import math

img = cv2.imread('ball.bmp', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('Image', img)
cv2.imshow('HSV ', hsv)
edges = cv2.Canny(hsv, 200, 200)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
