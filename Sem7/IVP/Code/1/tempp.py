
opt=0
#opt = input ("1 For Horizontal \n 2 For Vertical \n 3 For Both \n4 To Display them all\n")
img = cv2.imread('messi5.jpg',0)
h,w = img.shape
sum = [ [0 for i in range(w)] for j in range(h)]
for i in range(h-1):
	for j in range(w-1):
		sum[i][j] = int(img[i][j])
for i in range(h-1):
	for j in range(w-1):
		sum[i][j] += int(img[i][j])
new_img = np.zeros((h,w), np.uint8)
for i in range(h-1):
	for j in range(w-1):
		new_img[i][j] = (sum[i][j]/2)
cv2.imshow('New', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
