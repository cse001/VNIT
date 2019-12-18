import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

def getval(imglist,x,y):
    retval = 0
    for img in imglist:
        retval = retval + img[x][y]
    retval = retval / len(imglist)
    return retval

img = cv2.imread('messi5.jpg',0)
imglist = []
t = img.copy()
h,w = img.shape
m = 10
n = 1000

for i in range(m):
    for j in range(n):
        t[random.randrange(0,h,5)][random.randrange(0,w,5)] = random.randrange(0,255,1)
    imglist.append(t)
    t = img.copy()
print len(imglist)
count = 0
for timg in imglist:
    plt.title='Noise'+str(count)
    plt.subplot(2,(m//2)+1,count+1)
    cv2.imshow('Noise'+str(count),timg)
    plt.imshow(timg,cmap=plt.gray())
    count = count + 1
avgimg = np.zeros((h,w),np.uint8)
for i in range(h):
    for j in range(w):
        avgimg[i][j]=getval(imglist,i,j)


cv2.imshow('Avg',avgimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
plt.subplot(2,(m//2)+1,count+1)
plt.imshow(avgimg,cmap=plt.gray())
plt.show()
