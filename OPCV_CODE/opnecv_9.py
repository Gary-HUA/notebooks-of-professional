import cv2 as cv
# 视频文件的操作
src = cv.VideoCapture("E:/python_OpenCV lib/video_test.mp4")
# 首先判断是否正确打开 获取的是第一帧的图像
if src.isOpened():
    opened, frame = src.read()
    cv.imshow("frame", frame)  # 这里是show的源第一帧图像
# 如果不能正常打开 就opened 判为False
else:
    opened = False
# 正常打开的情况下 进行每一帧的循环读取
while open:
    ret, frame = src.read()
    if frame is None:
        break
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow("result",gray)
        if cv.waitKey(50) & 0xFF == 27:
            break
src.release()  # 关闭机器
cv.destroyAllWindows()
