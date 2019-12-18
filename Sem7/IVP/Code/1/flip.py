import numpy as np
import cv2
import sys
opt = input ("1 For Horizontal, 2 For Vertical , 3 For Both , 4 To Display them all")

def hor(img):
	temp=img
	h,w = img.shape
	for i in range (h):
		for j in range(w):
			temp[i][j]=img[h-i][j]
	cv2.imshow('Org', img)
	cv2.imshow('Hor',temp)
	return


img = cv2.imread('messi5.jpg',0)
img2 = cv2.imread('messi5.jpg',0)
img3 = cv2.imread('messi5.jpg',0)
img4 = cv2.imread('messi5.jpg',0)
img5 = cv2.imread('messi5.jpg',0)
for i in range (432):
    for j in range(768):
        img2[i,j]=img[431-i,j]
        img3[i,j]=img[431-i,767-j]
        img4[i,j]=img[i,767-j]
        if img5[i,j]<128:
            img5[i,j]=0
        else:
            img5[i,j]=255
while opt!=0:
    cv2.imshow('Image',img)
    if opt==1:
        cv2.imshow('Horizontally Flipped',img2)
    else if opt==2:
        cv2.imshow('Vertically Flipped',img4)
    else if opt==3:
        cv2.imshow('HoriVertically Flipped',img3)
    else if opt==4:
        cv2.imshow('HoriVertically Flipped',img3)
	cv2.imshow('Vertically Flipped',img4)
	cv2.imshow('Horizontally Flipped',img2)
cv2.imshow('Image',img)
cv2.imshow('Some',img5)
cv2.imshow('Horizontally Flipped',img2)
cv2.imshow('HoriVerti Flipped',img3)
cv2.imshow('Vertically Flipped',img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

