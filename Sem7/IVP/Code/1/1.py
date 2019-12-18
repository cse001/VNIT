import numpy as np
import cv2
import sys
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


#opt = input ("1 For Horizontal \n 2 For Vertical \n 3 For Both \n4 To Display them all\n")
try:
	opt = sys.argv[1]
	img = cv2.imread('messi5.jpg',0)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	cv2.imshow('Org', img)
	if opt=='1':
		hor(img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	elif opt=='2':
		ver(img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	elif opt=='3':
		horver(img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	elif opt=='4':
		hor(img)
		ver(img)
		horver(img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
	elif opt=='0':
		print("Thank You")
	else:
		print("Enter a valid option\n1 for Horizontal\n2 for Vertical\n3 for BothEffect\n4 for all the effects all at once")
except:
		print("Enter a valid argument")
