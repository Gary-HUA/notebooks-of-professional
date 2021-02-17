import cv2 as cv
import numpy as np
"""图像的旋转加上拉升就是图像仿射变换，仿射变化也是需要一个M矩阵就可以，但是由于仿射变换比较复杂，一般直接找很难找到这个矩阵，
opencv提供了根据变换前后三个点的对应关系来自动求解M。这个函数是
M=cv2.getAffineTransform(pos1,pos2),
其中两个位置就是变换前后的对应位置关系。
输出的就是仿射矩阵M。然后在使用函数cv2.warpAffine() 进行变换。
"""
img = cv.imread("E:/python_OpenCV lib/lena.jpg")
rows, cols = img.shape[:2]
print(img.shape)
# pst的值和图像的变换三个点有密切关系 运行代码查看各自代表值
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv.getAffineTransform(pts1, pts2)
res = cv.warpAffine(img, M, (rows, cols))
# 图像的透射
"""透视需要的是一个3*3的矩阵，同理opencv在构造这个矩阵的时候还是采用一种点对应的关系来通过函数自己寻找的，因为我们自己很难计算出来。
这个函数是M = cv2.getPerspectiveTransform(pts1,pts2)，
其中pts需要变换前后的4个点对应位置。得到M后在通过函数cv2.warpPerspective(img,M,(200,200))进行"""
pst3 = np.float32([[50, 60], [100., 52], [28, 200], [200, 220]])  # 四点
pst4 = np.float32([[0, 0], [200, 0], [0, 200], [200, 200]])
M1 = cv.getPerspectiveTransform(pst3, pst4)  # notice
res1 = cv.warpPerspective(img, M1, (110, 110))  # notice
cv.imshow("ori", img)
cv.imshow("res", res)
cv.imshow("res1", res1)
cv.waitKey(0)
cv.destroyAllWindows()