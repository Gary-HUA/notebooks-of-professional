# 图像插值是因为图像在几何变化中 源图像的像素值可能不能整值进行表达 我们需要进行插值计算 获得变化图像的像素值
import cv2 as cv
# cv. resize(src, dsize[, dst[, fx[, fy[ , interpolation])
# 通常, 缩小图像使用区域插值, 放大使用三次样条插值和双线性插值,
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
print(src.shape)  # (225, 225, 3)
print(src.size)
width = int(src.shape[0]*0.3)  # x
height = int(src.shape[1]*0.3)  # y
dsize = (width, height)  # 重置大小
resized = cv.resize(src, dsize, interpolation=cv.INTER_LINEAR)   # 双线性插值法 直接通过长宽计算,效果和下算法验证一样.
# 图像变换数据 将图像的x,y 扩大1.5倍
fx = 1.5
fy = 1.5
# 算法验证
resized1 = cv.resize(src, dsize=None, fx=fx, fy=fy, interpolation=cv.INTER_NEAREST)  # 最近邻插值法
resized2 = cv.resize(src, dsize=None, fx=fx, fy=fy, interpolation=cv.INTER_LINEAR)  # 双线性插值法
resized3 =cv.resize(src, dsize=None, fx=fx, fy=fy, interpolation=cv.INTER_CUBIC)  # 基于4*4的三次插值法
resized4 = cv.resize(src, dsize=None, fx=fx, fy=fy, interpolation=cv.INTER_AREA)  # 区域插值,块匹配算法
print("resized shape", resized.shape)  # int(225*0.3, 225*0.3, 3)
print("nearest interpolation", resized1.shape)  #
cv.imshow("ori", src)
cv.imshow("res", resized)
cv.imshow("nearest interpolation", resized1)
cv.imshow("bilinear interpolation", resized2)
cv.imshow("three linear interpolation", resized3)
cv.imshow("block interpolation", resized4)
cv.waitKey(0)
cv.destroyAllWindows()