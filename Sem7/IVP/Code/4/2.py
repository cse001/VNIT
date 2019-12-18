import cv2
import numpy as np
def Erode(img, k1, k2):
    h, w = img.shape[:2]
    img2 = np.zeros((h, w, 1), np.uint8)
    k3 = k1 - k2
    p = k1 // 2
    q = k2 // 2
    if q == 0:
        q = -1
    for i in range(p, h - p):
        for j in range(p, w - p):
            c = 0
            for x in range(i - p, i + p + 1):
                for y in range(j - p, j + p + 1):
                    if (abs(x - i) <= q and abs(y - j) <= q):
                        if (img[x][y] == 0):
                            c += 1
                    else:
                        if (img[x][y] == 255):
                            c += 1

            if (c == k1 * k1):
                img2[i][j] = 255
                if (i < 150):
                    print(i, j)
            else:
                img2[i][j] = 0
    return img2


def Intersection(img1, img2):
    h, w = img1.shape[:2]
    new = np.zeros((h, w, 1), np.uint8)
    for i in range(h):
        for j in range(w):
            if (img1[i][j] == 255 and img2[i][j] == 255):
                new[i][j] = 255
    return new


def HitorMiss(img):
    h, w = img.shape[:2]
    print("Eroding B1.......")
    B1 = Erode(img, 11, 0)
    cv2.imshow('B1', B1)
    print("Eroding B2.......")
    B2 = Erode(255 - img, 13, 11)
    cv2.imshow('B2', B2)
    B3 = Intersection(B1, B2)
    return B3


img = cv2.imread("semafor.bmp", 0)
cv2.imshow('Image', img)
cv2.imshow('Image2', 255 - img)
res = HitorMiss(img)
cv2.imshow('HitMiss', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
