import threading

import cv2
import numpy
from PIL import ImageGrab


class MyThread(threading.Thread):



    def __init__(self, path):
        threading.Thread.__init__(self)
        self.stop_even = threading.Event()
        self.path = path
        screen = ImageGrab.grab()  # 获得当前屏幕
        length, width = screen.size  # 获得当前屏幕的大小
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # 编码格式
        self.out = cv2.VideoWriter(self.path, fourcc, 32, (length, width))  # 输出文件命名为a.mp4,帧率为32，可以调节

    def run(self):
        self.stop_even.clear()

        while (True):
            img = ImageGrab.grab()  # 指定截取坐标(左边X，上边Y，右边X，下边Y)
            img_np = numpy.array(img)
            frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)  # ImageGrab获取的颜色为BGR排序，需转换为RGB
            self.out.write(frame)

            if self.stop_even.is_set():
                break
        self.out.release()
        cv2.destroyAllWindows()


    def stop(self):
        self.stop_even.set()