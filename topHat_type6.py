# Opening is performed on the binary image and the output of TOP HAT operation
# is a difference between the input image and the opened image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

import cv2

# read the image
img = cv2.imread("meyer.jpg", 0)
# binarize the image
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# define the kernel
kernel = np.ones((5, 5), np.uint8)
kernel1 = np.ones((15, 15), np.uint8)

# use morph gradient
morph_gradient = cv2.morphologyEx(binr, cv2.MORPH_TOPHAT, kernel)
morph_gradient1 = cv2.morphologyEx(binr, cv2.MORPH_TOPHAT, kernel1)
# print the output
plt.imshow(morph_gradient, cmap='gray')
cv2.imshow("morph", morph_gradient)
cv2.imshow("morph1", morph_gradient1)
cv2.waitKey(0)
