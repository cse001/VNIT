import cv2
import numpy as np
def equihist(img):
    h,w=img.shape[:2]
    new=np.zeros((h,w,1), np.uint8)
    hist=[0 for i in range(256)]
    for i in range(h):
        for j in range(w):
            p=img[i,j]
            hist[p]+=1
    sum_n=[0 for i in range(256)]
    sum_n[0]=hist[0]
    for i in range(1,256):
        sum_n[i]=sum_n[i-1]+hist[i]
    k=255.0/(h*w)
    for i in range(256):
        sum_n[i]=np.uint8(sum_n[i]*k)
    for i in range(h):
        for j in range(w):
            new[i,j]=np.uint8(sum_n[img[i,j]])
    return new

img = cv2.imread('2nd_from_top.tif',0)
cv2.imshow('Image',img)
eh=equihist(img)
cv2.imshow('Equalised',eh)
equ = cv2.equalizeHist(img)
cv2.imshow('Equalised_Inbuilt',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
