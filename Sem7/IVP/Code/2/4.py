import cv2
import numpy as np

def Smooth(size,arr):
    size = size - (size % 2)
    k = int(size / 2)
    for i in range(h):
        for j in range(w):
            sum = 0
            count = 0
            for p in range(k):
                if (i-p)>=0:
                    sum = sum + arr[i-p][j]
                    count = count + 1
                if (j-p)>=0:
                    sum = sum + arr[i][j-p]
                    count = count + 1
                if (i-p)>=0 and (j-p)>=0:
                    sum = sum + arr[i-p][j-p]
                    count = count + 1
                if (i+p)<h:
                    sum = sum + arr[i+p][j]
                    count = count + 1
                if (j+p)<w:
                    sum = sum + arr[i][j+p]
                    count = count + 1
                if (i+p)<h and (j+p)<w:
                    sum = sum + arr[i+p][j+p]
                    count = count + 1
                if (i-p)>=0 and (j+p)<w:
                    sum = sum + arr[i-p][j+p]
                    count = count + 1
                if (i+p)<h and (j-p)>=0:
                    sum = sum + arr[i+p][j-p]
                    count = count + 1
            arr[i][j] = ( sum / count )
    return arr
img = cv2.imread('top_left.tif',0)
h, w = img.shape
arr = np.array(img)
arr = Smooth(3,arr)
cv2.imshow("3x3 Average", arr)
arr1 = np.array(img)
arr1 = Smooth(11,arr1)
cv2.imshow("11x11 Average", arr1)
arr2 = np.array(img)
arr2 = Smooth(21,arr2)
cv2.imshow("21x21 Average", arr2)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
