import cv2
import numpy as np

img = cv2.imread("test1.bmp", 0)
cv2.imshow('Image', img)
img2 = img.copy()
h, w = img.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
cv2.floodFill(img, mask, (0, 0), 255);
im_floodfill_inv = cv2.bitwise_not(img)
im_out = img2 | im_floodfill_inv
cv2.imshow('Improved', im_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
