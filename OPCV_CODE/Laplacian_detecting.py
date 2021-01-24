import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# 拉普拉斯算法  对噪声点效果很差
dst = cv.Laplacian(gray_img, cv.CV_16S, ksize=3)
Laplacian = cv.convertScaleAbs(dst)
plt.subplot(121), plt.imshow(RGB_img), plt.title("origin_img"), plt.axis("off")
plt.subplot(122), plt.imshow(Laplacian, cmap=plt.cm.gray), plt.title("Laplacian"), plt.axis("off")
plt.show()