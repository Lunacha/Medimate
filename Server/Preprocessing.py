import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("./data/roical.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
kernel = np.ones((1,1), np.uint8)


image = cv2.dilate(image, kernel, iterations=1)
image = cv2.erode(image, kernel, iterations=1)

kernel_sharpen = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
image = cv2.filter2D(image, -1, kernel_sharpen)

#imageTH = cv2.adaptiveThreshold(cv2.medianBlur(image,1), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31,2)
image = cv2.adaptiveThreshold(cv2.bilateralFilter(image, 5, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 31,4)


plt.imshow(image, cmap="gray"), plt.axis("off")

plt.show()

