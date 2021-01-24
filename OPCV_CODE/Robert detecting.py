import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import Model
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
img_RGB = cv.cvtColor(src, cv.COLOR_BGR2RGB) #转成RGB 方便后面显示
gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 图像转为灰度图
# Robert 算子
# template
kernel_x = np.array([[1, 0], [0, -1]], dtype=int)
kernel_y = np.array([[0, 1], [-1, 0]], dtype=int)
x = cv.filter2D(gray_img, cv.CV_16S, kernel_x)
y = cv.filter2D(gray_img, cv.CV_16S, kernel_y)
# 转UNIT8
absx = cv.convertScaleAbs(x)
abxy = cv.convertScaleAbs(y)
Roberts = cv.addWeighted(absx, 0.5, abxy, 0.5, 0)
# 显示正常中文标签
# plt.rcParams["font.sans-serif"] = ["SimHei"]

# 显示图形
# titles = [u'原始图像', u'Roberts算子']
# images = [img_RGB, Roberts]
# for i in range(2):
#     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])
#
# plt.show()
# 显示结果图像
plt.subplot(121), plt.imshow(img_RGB), plt.title("original"), plt.axis("off")
plt.subplot(122), plt.imshow(Roberts), plt.title("robert algorithm"), plt.axis("off")
plt.show()
