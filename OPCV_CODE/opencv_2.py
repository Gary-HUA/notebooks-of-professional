import cv2 as cv
# 定义一个方法 用于获取图片的格式等基本信息


def image_info(img):
    print(type(img))  # <class 'numpy.ndarray'>
    print(img.shape)  # (256, 256, 3)
    print(img.size)  # 196608
    print(img.dtype)  # uint8


src = cv.imread("E:/python_OpenCV lib/lena.jpg", cv.IMREAD_GRAYSCALE)  # 加载一张图片,第二个参数定义色彩(cv.IMREAD_COLOR)
cv.imwrite("E:/python_OpenCV lib/lena_gray.jpg", src)  # 保存图像信息,第一个参数是位置,第二个参数是源文件
cv.imshow("image", src)  # 显示一张图片
image_info(src)
cv.waitKey(0)  # 等待窗口,任意键关闭
cv.destroyAllWindows()  # 销毁窗口
