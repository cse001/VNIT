import cv2
import numpy as np
def averageFilter(img,n):
    h,w=img.shape[:2]
    if n%2==0: n+=1
    new=np.zeros((h,w,1), np.uint8)
    k=n//2
    img = cv2.copyMakeBorder(img,k,k,k,k,cv2.BORDER_CONSTANT)

    for i in range(k,k+h):
        for j in range(k,k+w):
            sum=0
            for s in range(i-k,i+k+1):
                for t in range(j-k,j+k+1):
                    sum+=img[s,t]
            p=sum//(n*n)
            new[i-k,j-k]=p
    cv2.imshow('Filtered',new)
    return new
def Laplacian(img):
    laplacian = cv2.Laplacian(img,cv2.BORDER_CONSTANT)
    cv2.imshow('Laplacian',laplacian)
    return laplacian
def Sobel(img):
    sobelx = cv2.Sobel(img,cv2.BORDER_CONSTANT,1,0,ksize=3)
    sobely = cv2.Sobel(img,cv2.BORDER_CONSTANT,0,1,ksize=3)
    sobel =cv2.add(sobelx,sobely)
    cv2.imshow('Sobel',sobel)
    return sobel

def Product(img1,img2):
    h,w=img1.shape[:2]
    new=np.zeros((h,w,1), np.uint8)

    for i in range(h):
        for j in range(w):
            p=max(img1[i,j],img2[i,j])
            if p>255: p=255
            new[i,j]=p
    return new
def powerlaw(img):
    g=0.3
    c=20
    h,w=img.shape[:2]
    for i in range(h):
        for j in range(w):
            p=img[i,j]
            s=c*(p**g)
            if(s>255):
                s=255
            img[i,j]=s
    cv2.imshow('PowerLaw',img)
    return img
img = cv2.imread("skeleton.tif",0)
cv2.imshow('Original Image',img)
a=img
b=Laplacian(a)
c = cv2.subtract(a,b)
cv2.imshow("C=A-B (Original - Laplacian)",c)
d=Sobel(a)
e=averageFilter(a,5)
f=Product(c,e)
g=cv2.add(a,f)
cv2.imshow('Before_PL',g)
h=powerlaw(g)
i=Product(g,h)
cv2.imshow('Final',i)
cv2.waitKey(0)
cv2.destroyAllWindows()
