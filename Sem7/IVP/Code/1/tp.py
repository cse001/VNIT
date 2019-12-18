import cv2
import numpy as np
from PIL import Image,ImageDraw

img = cv2.imread('messi5.jpg',0)
temp = img.rotate(90,expand=True)
cv2.imshow('o',img)
cv2.imshow('t',temp)
cv2.waitKey(0)
cv2.destroyAllWindows()
