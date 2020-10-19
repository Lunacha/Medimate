import cv2
import numpy as np
from matplotlib import pyplot as plt


class ImgPreprocessor:
    def __init__(self):
        self.image = None
        self.kernel = np.ones((5, 5), np.uint8)

    def ProcExecute(self, file_name):
        self.image = cv2.imread("./data/" + file_name, cv2.IMREAD_GRAYSCALE)
        self.image = cv2.resize(self.image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
        self.image = cv2.GaussianBlur(self.image, (1, 1), cv2.BORDER_DEFAULT)


        #kernel_sharpen = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        #self.image = cv2.filter2D(self.image, -1, kernel_sharpen)

        #self.image = cv2.adaptiveThreshold(cv2.medianBlur(self.image,3), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41,4)
        self.image = cv2.adaptiveThreshold(cv2.bilateralFilter(self.image, 3, 75, 75), 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 43, 10)
        cv2.imwrite("./data/tmp.jpg", self.image)

    def display(self):
        plt.imshow(self.image,cmap="gray"), plt.axis("off")
        plt.show()
