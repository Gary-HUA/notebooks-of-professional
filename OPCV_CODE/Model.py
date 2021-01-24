import cv2 as cv
def result(self):
    print(type(self))
    print(self.size)
    print(self.shpae)


def wait_win(self):
    cv.imshow("res",self)
    cv.waitKey(0)
    cv.destroyAllWindows()




