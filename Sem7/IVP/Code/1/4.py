import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('messi5.jpg',0)
t = img.copy()
for exp in range(8):
    t = ((img//(2**exp)))* (2**exp)
    plt.subplot(2,4, exp+1)
    plt.imshow(t,cmap=plt.gray())
plt.show()
