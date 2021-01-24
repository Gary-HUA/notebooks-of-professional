# 图像中一般存在 平面, 边界, 角点等三大类形状 我们通过Harris检测出图像中X,Y方向变化比较大的角点区域
import cv2 as cv
import numpy as np
# cv2.cornerHarris(img, blockSize, k)  img为float32类型图像, blocksize 指定区域大小可能是个高斯函数, ksize求导窗口大小.K 0.04/0.06
img = cv.imread("E:/python_OpenCV lib/corner_Harris.jpg")  # 输入图像
# print(type(img))  # <class 'numpy.ndarray'>  这里需要图像的类型转换
# print(img.shape)  # (225, 224, 3)
# print(img.size)  # 151200
# 图像的预处理
# 结果得出图像有点小 magnification processing
img = cv.resize(img, dsize=None, fx=2, fy=2)
print(img.shape)
gary_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度图转换
print(type(gary_img))  # <class 'numpy.ndarray'>
gray_type = np.float32(gary_img)  # 图像的格式转换
res = cv.cornerHarris(gray_type, 2, 3, 0.04)
print("result_shape:", res.shape)  # result_shape: (225, 224)
# 角点判定
img[res > 0.05*res.max()] = [0, 0, 255]  # 就是我们的判断结果 为 True 那么就是角点 进行绿色标注 我们通过对0.01的更改获得更加精准的值
# 画出结果图像
cv.imshow("result", img)
cv.waitKey(0)
cv.destroyAllWindows()



