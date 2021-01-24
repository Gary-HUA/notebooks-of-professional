# 傅里叶变换  时域和空间域的不同角度问题
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
# 格式转换为np.float32
img_float32 = np.float32(img)
# 傅里叶变换 dft
dft = cv.dft(img_float32, flags=cv.DFT_COMPLEX_OUTPUT)
# np的 fftshift得到低频在中心的位置的频谱图
dft_shift = np.fft.fftshift(dft)
# 转换为灰度图的表示形式
magnitude_spectrum = 20*np.log(cv.magnitude(dft_shift[:,:,0], dft_shift[:, :, 1]))  # 0 and 1 两个通道
plt.subplot(121), plt.imshow(img, cmap="gray")
plt.title("input image"), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("magnitude spectrum"), plt.xticks([]), plt.yticks([])
plt.show()