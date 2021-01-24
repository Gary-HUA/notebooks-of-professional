# 图像融合  首先图像shape相等 或者cv.resize(src,(a,b)) 图像的等比例缩放 cv.resize(src,(0,0),fx=a,fx=b)
# import cv2 as cv
# src = cv.imread("E:/python_OpenCV lib/lena.jpg")
# result = cv.resize(src, (0, 0), fx=2, fy=2)
# cv.imshow("result", result)
# cv.waitKey()
# cv.destroyAllWindows()
import cv2 as cv


def details(image):
    print(type(image))
    print(image.size)
    print(image.shape)
    print(image.dtype)


# 图像大小进行一致化
src1 = cv.imread("E:/python_OpenCV lib/img_addation1.jpg")
src2 = cv.imread("E:/python_OpenCV lib/img_addation2.jpg")
details(src1)
print("------")
details(src2)
changed = cv.resize(src1, (295, 171))
details(changed)
# 融合   这里的融合会有背景混乱 图像噪声过大的结果
# fashion = src2+changed
# cv.imshow("fashion img", fashion)
# 使用cv.addWeighted  分别以两张图片的权重进行融合 a*x1+b*x2+c a=0.4 b=0.6
re_fashion = cv.addWeighted(src2, 0.3, changed, 0.7, 0)
cv.imshow("re_fashion", re_fashion)
cv.imwrite("E:/python_OpenCV lib/lena_cutting.jpg", re_fashion)
cv.waitKey(0)
cv.destroyAllWindows()
