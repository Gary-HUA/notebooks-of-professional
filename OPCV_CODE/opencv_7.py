import cv2 as cv
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
src = src+20  # 图像加一个值 就是每个像素每个通道都加
cv.imshow("ori", src)
cv.waitKey(0)
cv.destroyAllWindows()