import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 图像转为灰度图
img_RGB = cv.cvtColor(src, cv.COLOR_BGR2RGB)  # 为了显示原图
# Prewitt 算子 基于Robert算子的进阶版 3*3的模板 直观视觉是轮廓对比Robert 更加粗
# 模板
kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)
x = cv.filter2D(gray_img, cv.CV_16S, kernel_x)
y = cv.filter2D(gray_img, cv.CV_16S, kernel_y)

absX = cv.convertScaleAbs(x)
absY = cv.convertScaleAbs(y)
Prewitt = cv.addWeighted(absX, 0.5, absY, 0.5, 0)

# 显示结果图像
plt.subplot(121), plt.imshow(img_RGB), plt.title("origin image"), plt.axis('off')  # 坐标轴关闭
plt.subplot(122), plt.imshow(Prewitt), plt.title("Prewitt"), plt.axis('off')
plt.show()
