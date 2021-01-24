import cv2 as cv  # bgr
import numpy as np
import matplotlib.pyplot as plt  # rgb
img = cv.imread("E:/python_OpenCV lib/lena.jpg", 1)
color = ("b", "g", "r")  # 使用cv2色彩模式
for i, col in enumerate(color):
    histr = cv.calcHist([img], [i], None, [256], [0,256])  # 计算直方图
    plt.plot(histr, color=col)
    plt.xlim([0, 256])  # 显示台控制 就是X轴的取值
    plt.show()  # 展示直方图结果

