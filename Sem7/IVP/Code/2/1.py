import cv2
import numpy as np
import math

def Log(arr,c):
    for i in range(h):
        for j in range(w):
            arr[i][j] = c * math.log(1 + arr[i][j] , 10)
    return arr
def Power(arr,c,g):
    for i in range(h):
        for j in range(w):
            arr[i][j] = c * arr[i][j] ** g
    return arr
img = cv2.imread('fractured_spine.tif',0)
h, w = img.shape
print ("For log, best result was at 100")
c = input("C =")
arr = np.array(img)
log_img = Log(arr,c)
print ("For power law, C =30 , G=0.3")
c = input("C = ")
g = input("G = ")
arr = np.array(img)
pow_img = Power(arr,c,g)

cv2.imshow("Original Image",img)
cv2.imshow("Log Transformation",log_img)
cv2.imshow("Power Transformation",pow_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
