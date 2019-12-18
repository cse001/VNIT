import cv2
import numpy as np
from matplotlib import pyplot as plt

def CalcHist(arr):
    bins = np.zeros(256, np.int32)
    for i in range(h):
        for j in range(w):
            intensity = arr[i][j]
            bins[intensity] = bins[intensity] + 1
    return bins

img = cv2.imread('top_left.tif',0)
img1 = cv2.imread('2nd_from_top.tif',0)
img2 = cv2.imread('bottom_left.tif',0)
h, w = img.shape
arr = np.array(img)
bins = np.zeros(256, np.int32)
bins = CalcHist(img)
fig = plt.figure()
fig.add_subplot(2,2,1)
x = range(len(bins))
plt.bar(x, bins, 1 / 1.5)
plt.xlim([0, 256])
plt.title('Histogram 1')
bins = CalcHist(img1)
fig.add_subplot(2,2,2)
x = range(len(bins))
plt.bar(x, bins, 1 / 1.5)
plt.xlim([0, 256])
plt.title('Histogram 2')
bins = CalcHist(img2)
fig.add_subplot(2,2,3)
x = range(len(bins))
plt.bar(x, bins, 1 / 1.5)
plt.xlim([0, 256])
plt.title('Histogram 3')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
