import cv2
import numpy as np

imageSource = 'two_cats.jpg'
img = cv2.imread(imageSource, cv2.IMREAD_GRAYSCALE)
noise_type = str(raw_input('Noise Type (G or SP): '))
noise_type = noise_type.strip(' ')
if noise_type == 'G':
    row, col = img.shape
    mean = input('Mean: ')
    variance = input('Variance: ')
    sigma = variance ** 0.5
    gaussian = np.ndarray(img.shape, dtype=np.uint8)
    cv2.randn(gaussian, mean, sigma)
    noisyImage = img + gaussian
    cv2.imshow("Original Image", np.array(img, dtype=np.uint8))
    cv2.imshow("Image with Gaussian Noise", np.array(noisyImage, dtype=np.uint8))
else:
    row, col = img.shape
    saltProbability = float(raw_input('The Probability of salt: '))
    noisePercentage = float(raw_input('Total noise percentage: '))
    noisyImage = np.copy(img)
    numberOfSalts = np.ceil(noisePercentage * img.size * saltProbability)
    for i in range(int(numberOfSalts)):
        x = np.random.randint(0, img.shape[0] - 1)
        y = np.random.randint(0, img.shape[1] - 1)
        noisyImage[x, y] = 255
    numberOfPepper = np.ceil(noisePercentage * img.size * (1. - saltProbability))
    xcoords = [np.random.randint(0, img.shape[0] - 1, int(numberOfPepper))]
    ycoords = [np.random.randint(0, img.shape[1] - 1, int(numberOfPepper))]
    for i in range(int(numberOfPepper)):
        x = np.random.randint(0, img.shape[0] - 1)
        y = np.random.randint(0, img.shape[1] - 1)
        noisyImage[x, y] = 0
    cv2.imshow("Original", np.array(img, dtype=np.uint8))
    cv2.imshow("SaltPepper noise added", np.array(noisyImage, dtype=np.uint8))

cv2.waitKey(20000)
cv2.destroyAllWindows()
