# 图像滤波 (remove nosing)  filter average , box_filter, gaussian_blur ,median_blur
import cv2 as cv
from matplotlib import pyplot as plt
src = cv.imread("E:/python_OpenCV lib/lena_nosing.jpg")  # 椒盐噪声源图像
cv.imshow("original", src)
blur = cv.blur(src, (3, 3))  # 均值滤波(模糊化比较严重,噪声没有太大的减少)
# cv.imshow("result", blur)
box_filter = cv.boxFilter(src, -1, (3, 3), normalize=True)  # 方框滤波  当值为ture 和均值滤波一样,
# cv.imshow("result", box_filter)
Gussian_Blur = cv.GaussianBlur(src, (3, 3), 1)  # 更重视中间值 上下左右的比重增加,而对角数值比重进行减轻
# cv.imshow("result", Gussian_Blur)
median_blur = cv.medianBlur(src, 5) # 中值滤波 基本没有噪声 但是平滑较严重

titles = ["src", "blur", "box_filter", "gussian_blur", "median_blur"]
results = [src, blur, box_filter, Gussian_Blur, median_blur]
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(results[i], "gray"), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])   # 不显示坐标轴
plt.show()
