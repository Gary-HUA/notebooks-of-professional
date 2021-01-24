# mask operator
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import Model as Mo
img = cv.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
# 创建mask
mask = np.zeros(img.shape[0:2], np.uint8)  # 画出一个窗口
mask[50:200, 50:200] = 255  # mask的大小范围

# 对图像进行掩模
masked_img = cv.bitwise_and(img, img, mask=mask)  # &操作  图像和掩模进行重合计算
hist_full = cv.calcHist([img], [0], None, [256], [0, 256])  # 计算直方图
hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])
# 展示结果  这里221 "gray" 都是固定参数 不要改变
plt.subplot(221), plt.imshow(img, "gray")  # 显示的原图像
plt.subplot(222), plt.imshow(mask, "gray")  # 掩模
plt.subplot(223), plt.imshow(masked_img, "gray")  # 掩模后的图像
plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)  # 这里画出了直方图
plt.xlim([0, 256])
plt.show()


