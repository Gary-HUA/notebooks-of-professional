import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
gray_img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)  # 图像转为灰度图
# Canny 边缘检测
result = cv.Canny(gray_img, 300, 400)  # canny 边缘检测使用了双阈值进行处理图像中的轮廓问题
result_1 = cv.Canny(gray_img, 200, 300)  # 不同的双阈值处理
res = np.hstack((gray_img, result, result_1))  # 只能有一个参数.
cv.imshow("result", res)
cv.waitKey(0)
cv.destroyAllWindows()