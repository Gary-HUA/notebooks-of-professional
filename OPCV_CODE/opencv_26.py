import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("E:/python_OpenCV lib/lena_gray.jpg", 0)
# 1.转换成np.float32 格式
img_float32 = np.float32(img)
# 2.傅里叶变换 dft
dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
# 3.np的fftshift得到低频在中心位置的频谱图
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = int(rows/2), int(cols/2)     # 中心位置

# 4.高通滤波
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1  # 低通滤波 所以计算图像长宽是为制作mask,中心(30+30)x(30x30)区域为1

# 5.IDFT
fshift = dft_shift*mask					# 仅保留了中心区域
f_ishift = np.fft.ifftshift(fshift)		# 把中心位置的东西放回原位	ifftshift
img_back = cv2.idft(f_ishift)			# 从频谱图转换回来 idft
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])	# 转换一下 得到灰度图能表示的形式

plt.subplot(121),plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap='gray')
plt.title('Result'), plt.xticks([]), plt.yticks([])

plt.show()
