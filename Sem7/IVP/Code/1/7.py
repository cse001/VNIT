import cv2
import numpy as np


img = cv2.imread('messi5.jpg',0)
h,w = img.shape
center = h/2,w/2
rmat = cv2.getRotationMatrix2D(center,45,1.0)
linear = cv2.warpAffine(img,rmat,img.shape[1::-1], flags=cv2.INTER_LINEAR)
near = cv2.warpAffine(img,rmat,img.shape[1::-1], flags=cv2.INTER_NEAREST)
cubic = cv2.warpAffine(img,rmat,img.shape[1::-1], flags=cv2.INTER_CUBIC)
area = cv2.warpAffine(img,rmat,img.shape[1::-1], flags=cv2.INTER_AREA)
lanc = cv2.warpAffine(img,rmat,img.shape[1::-1], flags=cv2.INTER_LANCZOS4)
cv2.imshow('Linear',linear)
cv2.imshow('Near',near)
cv2.imshow('Cubic',cubic)
cv2.imshow('Area',area)
cv2.imshow('Lanczos',lanc)
cv2.waitKey(0)
cv2.destroyAllWindows()
