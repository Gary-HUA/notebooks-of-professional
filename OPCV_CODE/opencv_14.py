import numpy as np
import cv2 as cv
img = cv.imread("E:/python_OpenCV lib/gradient_demo.jpg")
kernel = np.ones((3, 3), np.uint8)
top_hat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)  # 礼帽 得出边缘毛刺
black_hat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)  # 黑帽 图像边缘轮廓
res = np.hstack((img, top_hat, black_hat))
cv.imshow("result", res)
cv.waitKey(0)
cv.destroyAllWindows()
