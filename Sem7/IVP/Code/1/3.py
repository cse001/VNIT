import numpy as np
import cv2

img = cv2.imread('moon.tif',0)
h,w = img.shape
temp = img.copy()
for i in range(h):
    for j in range(w):
        temp[i][j]=(255)-(img[i][j])
cv2.imshow('Moon',img)
cv2.imshow('Answer',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()
