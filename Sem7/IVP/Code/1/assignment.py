import numpy as np
import cv2
import sys
import matplotlib.pyplot as plt
import random
def hor(img):
	h,w = img.shape
	temp=np.zeros((h,w), np.uint8)
	for i in range (h):
		for j in range(w):
			temp[i][j]=img[h-i-1][j]
	cv2.imshow('Hor',temp)
	return
def ver(img):
	h,w = img.shape
	temp=np.zeros((h,w), np.uint8)
	for i in range (h):
		for j in range(w):
			temp[i][j]=img[i][w-j-1]
	cv2.imshow('Ver',temp)
	return
def horver(img):
	h,w = img.shape
	temp=np.zeros((h,w), np.uint8)
	for i in range (h):
		for j in range(w):
			temp[i][j]=img[h-i-1][w-j-1]
	cv2.imshow('HorVer',temp)
	return
def que1(img):
    cv2.imshow('Org', img)
    hor(img)
    ver(img)
    horver(img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return
def que2(img):
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
    return
def que3(img):
    h,w = img.shape
    temp = img.copy()
    for i in range(h):
        for j in range(w):
            temp[i][j]=(255)-(img[i][j])
    while 1:
        cv2.imshow('Moon',img)
        cv2.imshow('Answer',temp)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    cv2.destroyAllWindows()
    return
def que4():
	img = cv2.imread('messi5.jpg',0)
	t = img.copy()
	for exp in range(8):
	    t = ((img//(2**exp)))* (2**exp)
	    plt.subplot(2,4, exp+1)
	    plt.imshow(t,cmap=plt.gray())
	plt.show()
	return

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

def que5():
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
	cv2.imshow('Original',img)
	cv2.imshow('expand',expimg)
	cv2.imwrite('expand.jpg',expimg)
	cv2.imwrite('shrink.jpg',temp)
	cv2.imshow('Shrink',temp)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return

def getval(imglist,x,y):
    retval = 0
    for img in imglist:
        retval = retval + img[x][y]
    retval = retval / len(imglist)
    return retval

def que6():
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
	return
def que7(angle):
	img = cv2.imread('messi5.jpg',0)
	h,w = img.shape
	center = h/2,w/2
	rmat = cv2.getRotationMatrix2D(center,angle,1.0)
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

try:
    opt = sys.argv[1]
    if opt=='1':
		img=cv2.imread('messi5.jpg',0)
		que1(img)
    if opt=='2':
        img=cv2.imread('moon.tif',0)
        que2(img)
    if opt=='3':
        img=cv2.imread('moon.tif',0)
        que3(img)
    if opt=='4':
        img = cv2.imread('messi5.jpg',0)
        que4()
    if opt=='5':
        que5()
    if opt=='6':
        que6()
    if opt=='7':
		angle=int(sys.argv[2])
		que7(angle)

except Exception as e:
    print e
