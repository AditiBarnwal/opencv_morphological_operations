# eroding the outer surface (the foreground) of the image.
# binary images contain two pixels 0 and 255,
# first involves eroding the foreground of the image, and have the foreground as white.

# The thickness of erosion depends on the SIZE and SHAPE of the defined kernel.

# use NumPy’s ones() function to define a kernel.
# other functions like NumPy zeros, customized kernels, and others that can be used to define kernels.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv2.imread("Meyer.jpg", 0)

# binarize the image
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# define the kernel
kernel = np.ones((5, 5), np.uint8)

# invert the image
invert = cv2.bitwise_not(binr)

# erode the image
erosion = cv2.erode(invert, kernel, iterations=1)

# print the output
plt.imshow(erosion, cmap='gray')
cv2.imshow("erosion", erosion)
cv2.waitKey(0)

# output should be a thinner image than the original one.
