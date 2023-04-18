# Import the necessary packages
# Read the image
# Binarize the image.
# it is advised to keep the foreground in white, will performing OpenCV’s invert operation
# on the binarized image to make the foreground white.
# We are defining a 3×3 kernel filled with ones

# Then use Opencv dilate() function to dilate the boundaries of the image.
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

# dilate the image
dilation = cv2.dilate(invert, kernel, iterations=1)

# print the output
plt.imshow(dilation, cmap='gray')
cv2.imshow("dilation", dilation)
cv2.waitKey(0)

# output should be a thicker image than the original one
