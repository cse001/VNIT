import cv2
import numpy as np

def shrinkval(img,x,y,factor):
    h,w = img.shape
    xs = int(x*factor)
    ys = int(y*factor)
    retval = 0
    for i in range (factor):
        for j in range(factor):
            retval+=int(img[xs+i][ys+j])
    retval = retval/(factor*factor)
    return retval


img=cv2.imread('gray.jpg',0)
factor = 10
h,w = img.shape
temp=np.zeros((h/factor,w/factor), np.uint8)
h,w = temp.shape
for i in range(h):
    for j in range(w):
        temp[i][j]=np.uint8 (shrinkval(img,i,j,factor))
#Now we expand
expimg = np.zeros((h*factor,w*factor),np.uint8)
hh,ww = expimg.shape
for i in range(hh):
    for j in range(ww):
        expimg[i][j] = temp[int(i/10)][int(j/10)]
cv2.imshow('expand',expimg)
cv2.imwrite('expand.jpg',expimg)
cv2.imwrite('shrink.jpg',temp)
cv2.imshow('Shrink',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()
