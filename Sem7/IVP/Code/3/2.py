import cv2
import numpy as np
from matplotlib import pyplot as plt

filterX = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])  #Sobel Filter in X
filterY = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])  #Sobel Filter in Y
img = cv2.imread('two_cats.jpg', cv2.IMREAD_GRAYSCALE)  #Read the image
img_dft = np.fft.fft2(img)                              #Get the Fourier Transformation
sobelx_filter_dft = np.fft.fft2(filterX, s=img.shape)   #Fourier Transformation of Sobel in X
sobely_filter_dft = np.fft.fft2(filterY, s=img.shape)
filteredx_img_dft = img_dft * sobelx_filter_dft
filteredy_img_dft = img_dft * sobely_filter_dft

filteredx_img_back = np.fft.ifft2(filteredx_img_dft)
filteredy_img_back = np.fft.ifft2(filteredy_img_dft)
ans = - filteredy_img_back.real - filteredx_img_back.real

plt.subplot(111), plt.imshow(ans, cmap='gray')
plt.title("Ans image"), plt.xticks([]), plt.yticks([])
plt.show()

cv2.waitKey(0)
