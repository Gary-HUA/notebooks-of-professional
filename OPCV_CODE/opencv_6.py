# 边界填充copyMakeBorder  边界需要画出来 使用了matplotlib
# replicate 复制方法
# reflect 反射
# reflect_101
# wrap
# constant
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread("E:/python_OpenCV lib/lena.jpg")
top_size, bottom_size, left_size, right_size = (20, 20, 20, 20)  # 制定扩充边界的大小
img_replace = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv.BORDER_REPLICATE)
plt.subplot(231), plt.imshow(img, "gray"), plt.title("original")
plt.subplot(232), plt.imshow(img_replace, "gray"), plt.title("replace")
plt.savefig("E:/python_OpenCV lib/lena.jpg")
plt.show()


# import cv2
# import matplotlib.pyplot as plt
# img = cv2.imread("E:/python_OpenCV lib/lena.jpg")
# top_size,bottom_size,left_size,right_size = (50,50,50,50)
# 边界填充方法
# img_replace = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REPLICATE)
# img_reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,cv2.BORDER_REFLECT)
# img_reflect101 = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_REFLECT_101)
# img_wrap = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv2.BORDER_WRAP)
# img_constant = cv2.copyMakeBorder(img, top_size, bottom_size, left_size, right_size,cv2.BORDER_CONSTANT, value=0)
# # cv_show('img_wrap',img_wrap) 显示图
# plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(img_replace,'gray'),plt.title('Replace')
# plt.subplot(233), plt.imshow(img_reflect, 'gray'), plt.title('REFLECT')
# plt.subplot(234), plt.imshow(img_reflect101, 'gray'), plt.title('REFLECT_101')
# plt.subplot(235), plt.imshow(img_wrap, 'gray'), plt.title('WRAP')
# plt.subplot(236), plt.imshow(img_constant, 'gray'), plt.title('CONSTANT')
# plt.savefig('cat_fill.jpg')
# plt.show()
