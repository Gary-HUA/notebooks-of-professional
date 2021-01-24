#  pyramid of image
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/lena_pyramid.jpg")
up_samp = cv.pyrUp(img)  # 高斯金字塔就是向下采样 图像变小,高斯卷积然后删除了偶数行列,
down_sampling = cv.pyrDown(img)  # 拉普拉斯金字塔 向上采样,图像变大, 扩大位置填充0
cv.imshow("original", img)
cv.imshow("up_sampling", up_samp)
cv.imshow("down_sampling", down_sampling)
cv.waitKey(0)
cv.destroyAllWindows()

