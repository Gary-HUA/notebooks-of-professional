import cv2 as cv
src = cv.imread("E:/python_OpenCV lib/lena.jpg")
res = src[20:400, 50:220]  # H W POSITION 把图像按照期望进行切割截取
cv.imshow("result", res)
cv.imwrite("E:/python_OpenCV lib/lena_cutting.jpg", res)
cv.waitKey(0)
cv.destroyAllWindows()