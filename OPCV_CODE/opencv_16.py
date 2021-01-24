import numpy as np
import cv2 as cv
# canny 轮廓获取 根据两个参数进行制定双阈值的范围
img = cv.imread("E:/python_OpenCV lib/lena.jpg", cv.IMREAD_GRAYSCALE)
res_1 = cv.Canny(img, 300, 400)  # canny 方法 双阈值参数根据图像进行调整 大于阈值是边界 , 在阈值之间连续的值是边界 小于阈值的舍弃
res_2 = cv.Canny(img, 100, 200)
res = np.hstack((img, res_1, res_2))
cv.imshow("result", res)
cv.waitKey(0)
cv.destroyAllWindows()
