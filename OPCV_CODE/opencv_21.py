import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena.jpg", 1)


def cv_show(img, name):
    cv.imshow(name, img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 参数 图像, channels(灰度图0,彩色123对应着BGR) mask(掩模图像要整个图像的直方图就是NONE)
hist = cv.calcHist([img], [0], None, [256], [0, 256])  # 直方图的计算
plt.hist(img.ravel(), 256)
plt.show()
