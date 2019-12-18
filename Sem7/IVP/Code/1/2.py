import cv2
import numpy as np
import sys

img = cv2.imread('moon.tif',0)
h,w = img.shape
intensity = 0
temp = img.copy()
for i in range(h):
    for j in range(w):
        intensity += int(temp[i][j])
averageintensity = intensity / (h*w)
for i in range(h):
    for j in range(w):
        if img[i][j] <averageintensity:
            temp[i][j]=0
        else:
            temp[i][j]=255
cv2.imshow('Moon',img)
cv2.imshow('Answer',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()
