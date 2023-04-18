# Morphological gradient different from the other operations,
# it first applies erosion and dilation individually on the image and
# then computes the difference between the eroded and dilated image.

# The output will be an outline of the given image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv2.imread("Meyer.jpg", 0)

# binarize the image
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# define the kernel
kernel = np.ones((3, 3), np.uint8)

# invert the image
invert = cv2.bitwise_not(binr)

# use morph gradient
morph_gradient = cv2.morphologyEx(invert, cv2.MORPH_GRADIENT, kernel)

# print the output
plt.imshow(morph_gradient, cmap='gray')
cv2.imshow("morph_gradient", morph_gradient)
cv2.waitKey(0)
