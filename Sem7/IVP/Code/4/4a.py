import sys
import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

def RGBtoHSI(img):
    r1,c,l=img.shape
    img2=np.full(img.shape,0,dtype=np.uint8)
    for i in range(0,r1):
        for j in range(0,c):
            b,g,r=img[i][j]
            r=float(r)
            g=float(g)
            b=float(b)
            s=(1-(3/(r+g+b))*min(r,g,b))*100
            intensity=(r+g+b)/3.0
            R=r/(r+g+b)
            G=g/(r+g+b)
            B=b/(r+g+b)
            if(r==g and g==b):
                val=0
            else:
                val=(2*R-G-B)/(2*math.sqrt((R-G)**2+(R-B)*(G-B)))
            h=math.acos(np.clip(val,-1,1))
            if(b>g):
                h=360-h
            h=h*180/math.pi
            img2[i][j][0]=h
            img2[i][j][1]=s
            img2[i][j][2]=intensity
    return img2

img1=cv2.imread('ball.bmp',1)
img2=RGBtoHSI(img1)
h=img2[:,:,0]/2.0
s=img2[:,:,1]
v=img2[:,:,2]
hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
H=hsv[:,:,0]
S=hsv[:,:,1]
V=hsv[:,:,2]
dH=np.abs(H-h)
dS=np.abs(S-s)
dV=np.abs(V-v)
sp=330
plt.subplot(sp+1),plt.imshow(h ,cmap='gray')
plt.title('Calculated Hue'), plt.xticks([]), plt.yticks([])
plt.subplot(sp+2),plt.imshow(s ,cmap='gray')
plt.title('Calculated Saturation'), plt.xticks([]), plt.yticks([])
plt.subplot(sp+3),plt.imshow(v ,cmap='gray')
plt.title('Calculated Intensity'), plt.xticks([]), plt.yticks([])
plt.subplot(sp+4),plt.imshow(H ,cmap='gray')
plt.title('Inbuilt Hue'), plt.xticks([]), plt.yticks([])
plt.subplot(sp+5),plt.imshow(S ,cmap='gray')
plt.title('Inbuilt Saturation'), plt.xticks([]), plt.yticks([])
plt.subplot(sp+6),plt.imshow(V ,cmap='gray')
plt.title('Inbuilt Intensity'), plt.xticks([]), plt.yticks([])
plt.subplot(sp+7),plt.imshow(dH ,cmap='gray')
plt.title('Difference in Hue'), plt.xticks([]), plt.yticks([])
plt.subplot(sp+8),plt.imshow(dS ,cmap='gray')
plt.title('Difference in Saturation'), plt.xticks([]), plt.yticks([])
plt.subplot(sp+9),plt.imshow(dV ,cmap='gray')
plt.title('Difference in Intensity'), plt.xticks([]), plt.yticks([])
#
plt.show()
