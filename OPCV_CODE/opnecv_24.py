import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import Model as Mo
img = cv.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
res = cv.equalizeHist(img)  # 直方图均衡化 使得图像的灰度色彩对比度增大
# 自适应直方图均衡化
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(3, 3))  #
res1 = clahe.apply(img)
# result = np.hstack((img, res, res1))
hist1 = cv.calcHist([img], [0], None, [256], [0, 256])
hist2 = cv.calcHist([res], [0], None, [256], [0, 256])
hist3 = cv.calcHist([res1], [0], None, [256], [0, 256])
plt.subplot(221), plt.imshow(img, "gray")  # 显示的原图像
plt.subplot(222), plt.imshow(res, "gray")
plt.subplot(223), plt.imshow(res1, "gray")
plt.subplot(224),plt.plot(img), plt.plot(hist1), plt.plot(hist2), plt.plot(hist3)  # 这里画出了直方图
plt.xlim(0, 256)
plt.show()
