# 梯度运算= 膨胀-腐蚀  膨胀一个轮廓 然后再对原图像进行腐蚀 得出一个轮廓
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/gradient_demo.jpg")
kernel = np.ones((3, 3), np.uint8)
dilate = cv.dilate(img, kernel, iterations=5)
erosion = cv.erode(img, kernel, iterations=5)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
res = np.hstack((dilate, erosion, gradient))
cv.imshow("result", res)
cv.waitKey(0)
cv.destroyAllWindows()