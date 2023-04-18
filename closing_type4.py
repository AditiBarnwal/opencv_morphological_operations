# blend of erosion and dilation constraints
# removes the noise of image

# import the necessary packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read the image
img = cv2.imread(r"\Images\noise.png", 0)

# binarize the image
binr = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# define the kernel
kernel = np.ones((3, 3), np.uint8)

# opening the image
closing = cv2.morphologyEx(binr, cv2.MORPH_CLOSE, kernel, iterations=1)

# print the output
plt.imshow(closing, cmap='gray')
cv2.imshow("closing", closing)
cv2.waitKey(0)
