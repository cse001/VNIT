import sys
import cv2
import numpy as np
import math

def lowPassFilter(x, y, cx, cy, rad): #Gaussian Low Pass Filter
    f = (x - cx) ** 2 + (y - cy) ** 2
    f = math.exp(-(f / (2 * (rad ** 2))))
    return f

originalImg = cv2.imread('97.jpg', cv2.IMREAD_GRAYSCALE)
fftOfImg = np.fft.fft2(originalImg)
fShiftOfImage = np.fft.fftshift(fftOfImg)
magnitude_spectrum = np.log(np.abs(fShiftOfImage)+1)*20 

rows, cols = originalImg.shape
crow, ccol = int(rows / 2), int(cols / 2)

filter_type = raw_input('Filter Type (H or L): ')
radius = float(raw_input('Radius: '))

if filter_type == 'H':
    for i in range(rows):
        for j in range(cols):
            fShiftOfImage[i, j] = fShiftOfImage[i, j] * (1 - lowPassFilter(i, j, crow, ccol, radius))
else:
    for i in range(rows):
        for j in range(cols):
            fShiftOfImage[i, j] = fShiftOfImage[i, j] * lowPassFilter(i, j, crow, ccol, radius)
f_ishift = np.fft.ifftshift(fShiftOfImage)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
cv2.imshow("Magnitude Spectrum", np.array(magnitude_spectrum, dtype=np.uint8))
cv2.imshow("Original", originalImg)
if filter_type == 'H':
    cv2.imshow("After HPF", np.array(originalImg + img_back, dtype=np.uint8))
else:
    cv2.imshow("After LPF", np.array(img_back, dtype=np.uint8))

cv2.waitKey(20000)
cv2.destroyAllWindows()
