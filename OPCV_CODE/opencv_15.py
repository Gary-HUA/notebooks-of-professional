# cv2.Sobel(src, ddepth, dx, dy, ksize) 进行sobel算子计算
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/lena.jpg", cv.IMREAD_GRAYSCALE)
# 计算 x 方向的轮廓
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)  # 1,0 表示只算水平,不算黑白
sobelxx = cv.convertScaleAbs(sobelx)  # 对像素值进行绝对值计算
# 计算Y方向的轮廓
sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
sobelyy = cv.convertScaleAbs(sobely)

# xy方向融合 不建议直接计算,先计算再求和 融合的更好
sobelxy = cv.addWeighted(sobelxx, 0.5, sobelyy, 0.5, 0)  # 分别计算
# sobelxy_1 = cv.Sobel(img, cv.CV_64F, 1, 1, ksize=3)  # 直接计算 不建议使用 图像不能达到预期目的
res = np.hstack((img, sobelxx, sobelyy, sobelxy))

cv.imshow("result", res)
cv.waitKey(0)
