# 开运算 先腐蚀再膨胀
import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/NAME.JPG", cv.IMREAD_GRAYSCALE)
kernel = np.ones((3, 3), np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)  # 开 腐蚀 去掉边角的毛刺
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  # 闭
result = np.hstack((img, opening, closing))
cv.imshow("open and close", result)
cv.waitKey(0)
cv.destroyAllWindows()