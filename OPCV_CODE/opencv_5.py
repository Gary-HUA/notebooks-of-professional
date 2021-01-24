import cv2
src = cv2.imread("E:/python_OpenCV lib/lena.jpg")  # 源图像
b, g, r = cv2.split(src)  # 对图像进行通道划分
r[50:100, 50:100] = 0  # 操作通道值 把红色通道制定区域设置为0
g[50:100, 50:100] = 0  # 双通道操作
image_new = cv2.merge((b, g, r))  # 合成操作后的通道
cv2.imshow("new_image", image_new)
cv2.waitKey(0)
cv2.destroyAllWindows()

