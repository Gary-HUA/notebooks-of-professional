# 图像的阈值操作
# ret dst = cv2.threshold(src, thresh, maxval, type) thresh一般是127 maxval =255 type(二值化操作类型)有五种类型
import cv2 as cv
import matplotlib.pyplot as plt
src = cv.imread("E:/python_OpenCV lib/lena_gray.jpg")  # 输入原图(因为阈值的特性我们使用二值图像)
# 1.THRESH_BINARY
# ret, img_bi = cv.threshold(src, 127, 255, cv.THRESH_BINARY)  # 大于阈值的像素值赋值为255,
# cv.imshow("test", img_bi)
# 2.THRESH_BINARY_INV
# ret, img_bi_inv = cv.threshold(src, 127, 255, cv.THRESH_BINARY_INV)  # 二值得反转,
# cv.imshow("test", img_bi_inv)
# 3.cv.THRESH_TRUNC  大于阈值部分取值阈值
# ret, img_bi_trunc = cv.threshold(src, 127, 255, cv.THRESH_TRUNC)  # 大于阈值的像素值取阈值127,
# cv.imshow("test", img_bi_trunc)
# 4.THRESH_TOZONE   大于阈值不变,小于阈值的为0
# ret, img_bi_tozone = cv.threshold(src, 127, 255, cv.THRESH_TOZERO)  # 大于阈值的像素值不变,小于阈值的取0,
# cv.imshow("test", img_bi_tozone)
# 5 THRESH_TOZONE_INV
# ret, img_bi_tozone_inv = cv.threshold(src, 127, 255, cv.THRESH_TOZERO_INV)  # 大于阈值的像素值不变,小于阈值的取0,
# cv.imshow("test", img_bi_tozone_inv)
cv.waitKey(0)
cv.destroyAllWindows()
