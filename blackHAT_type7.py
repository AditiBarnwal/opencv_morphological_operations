# black-hat operation : used in enhancing dark objects of interest on a bright background.
# output : is the difference between the closing of the input image and the input image.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv2.imread("Meyer.jpg", 0)

# binarize the image
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# define the kernel
kernel = np.ones((5, 5), np.uint8)

# invert the image
invert = cv2.bitwise_not(binr)

# use morph gradient
morph_gradient = cv2.morphologyEx(invert,
                                  cv2.MORPH_BLACKHAT,
                                  kernel)
# print the output
plt.imshow(morph_gradient, cmap='gray')
cv2.imshow("morph", morph_gradient)
cv2.waitKey(0)

