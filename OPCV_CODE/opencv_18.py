import cv2 as cv
import numpy as np
img = cv.imread("E:/python_OpenCV lib/contours.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   # 彩色图以灰度图的形式显示
ret, thresh = cv.threshold(gray_img, 50, 255, cv.THRESH_BINARY)  # 使用阈值函数对灰度图进行二值化
# cv.imwrite("E:/python_OpenCV lib/contours_binary.jpg", thresh)
# cv.imshow("thresh", thresh)
# cv.waitKey(0)
# cv.destroyAllWindows()
# 计算轮廓  cv2.findContours(img,mode,method)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
# 绘制轮廓 先进行copy 避免在原图作画
draw_img1 = img.copy()
draw_img2 = img.copy()
draw_img3 = img.copy()
# 参数如下：传入绘制图像，轮廓，轮廓索引，颜色模式，线条厚度
all_contours = cv.drawContours(draw_img1, contours, -1, (0, 255, 0), 2)	 # -1是指所有的轮廓
contours_0 = cv.drawContours(draw_img2, contours, 0, (0, 0, 255), 2)		# 检测到的第1个轮廓
contours_1 = cv.drawContours(draw_img3, contours, 1, (255, 0, 0), 2)		# 检测到的第2个轮廓
# 图像轮廓特征
cnt = contours[3]  #
# res = cv.contourArea(cnt)  # 轮廓特征的面积
res = cv.arcLength(cnt, True)  # 周长 True 表示闭合
print(cnt)
print(res)
#  图像轮廓近似
epsilon1 = 0.01*cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon1, True)
draw_approx = cv.drawContours(draw_img1, [approx], -1, (0, 0, 255), 2)

cv.imshow('res', np.hstack((all_contours, contours_0, contours_1,)))
cv.waitKey(0)



