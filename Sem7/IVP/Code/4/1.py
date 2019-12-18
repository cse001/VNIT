import cv2
def Dilate(img, k):
    h, w = img.shape[:2]
    img2 = img.copy()
    p = k // 2
    for i in range(p, h - p):
        for j in range(p, w - p):
            f = 0
            for x in range(i - p, i + p + 1):
                for y in range(j - p, j + p + 1):
                    if (img[x][y] == 255):
                        f = 1
            if (f == 1):
                img2[i][j] = 255
    return img2
def Erode(img, k):
    h, w = img.shape[:2]
    img2 = img.copy()
    p = k // 2
    for i in range(p, h - p):
        for j in range(p, w - p):
            c = 0
            for x in range(i - p, i + p + 1):
                for y in range(j - p, j + p + 1):
                    if (img[x][y] == 255):
                        c += 1
            if (c == k * k):
                img2[i][j] = 255
            else:
                img2[i][j] = 0
    return img2
def Opening(img, k):
    return Dilate(Erode(img, k), k)

def Closing(img, k):
    return Erode(Dilate(img, k), k)


img = cv2.imread("body1.bmp", 0)
img_ = cv2.imread("body2.bmp", 0)
cv2.imshow('Image', img)

img2 = Dilate(img, 5)
cv2.imshow('Dilated', img2)

img3 = cv2.subtract(img2, img)
cv2.imshow('Diff_dilation', img3)

img4 = Erode(img, 5)
cv2.imshow('Eroded', img4)

img5 = cv2.subtract(img, img4)
cv2.imshow('Diff_erosion', img5)

img6 = Opening(img, 5)
cv2.imshow('Opening', img6)

img7 = Closing(img, 5)
cv2.imshow('Closing', img7)
cv2.waitKey(0)
cv2.destroyAllWindows()
