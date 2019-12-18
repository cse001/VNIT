import cv2

def FindImage(img1,img2):
    h1, w1 = img1.shape
    h2, w2 = img2.shape

    for i in range(h1-h2):
        for j in range(w1-w2):
            t = 0
            for p in range(h2):
                for q in range(w2):
                    if(img1[i+p][j+q] != img2[p][q]):
                        t = 1
                        break
            if(t == 0):
                print("Image matched and found at " + str(i) + "," + str(j))
                image = img1[i:i+h2 , j:j+w2]
                cv2.imshow('Range Of Image',image)

img1 = cv2.imread("utk.png",0)
img2 = cv2.imread("t.png",0)
FindImage(img1,img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
