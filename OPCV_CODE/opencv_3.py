import cv2
# 视频的基本操作 把视频的每一帧看做图片进行处理
src = cv2.VideoCapture("E:/python_OpenCV lib/video_test.mp4")  # 获取视频源
if src.isOpened():  # 判断视频是否打开
    opened, frame = src.read()  # 读取视频的每一帧
else:
    opened = False

while open:
    ret, frame = src.read()
    if frame is None:
        break
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 视频操作为灰度图
        cv2.imshow("result", gray)
        if cv2.waitKey(10) & 0xFF == 27:  # 每一帧的间隔  27 是为了关闭视频
            break
src.release()
cv2.destroyAllWindows()



