# coding=utf-8
import base64
import os, sys
import time

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

#QSS样式读取器
class StyleReader():
    def __init__(self):
        pass

    @staticmethod
    def readQss(style):
        with open(style, 'r',encoding='UTF-8') as f:
            return f.read()

    @staticmethod
    def readQssFromFile(style):
        path = os.path.join(BASE_DIR,'src','stylesheet',style)
        with open(path, 'r', encoding='UTF-8') as f:
            return f.read()
#日志
class Log():
    @staticmethod
    def info(flag,msg):
        print('{}:{}'.format(flag,msg))

class FileUtils():
    def __init__(self):
        pass
    @staticmethod
    def savaToPng(path,data):
        with open(path, 'wb') as file:
            file.write(data)
        file.close()

class SimpleImgUtils():
    def __init__(self):
        pass

    # 图片缩放
    @staticmethod
    def ShrinkImage(path,scale=1):
        img = QImage(path)  # 创建图片实例
        mgnWidth = int(img.width() * scale)
        mgnHeight = int(img.height() * scale)  # 缩放宽高尺寸
        size = QSize(mgnWidth, mgnHeight)
        return QPixmap.fromImage(img.scaled(size, Qt.IgnoreAspectRatio))  # 修改图片实例大小并从QImage实例中生成QPixmap实例以备放入QLabel控件中

    @staticmethod
    def Image2Base64(image_path):
        with open(image_path, 'rb') as f:
            image = f.read()
        return base64.b64encode(image)

class TimeUtils():
    @staticmethod
    def getTimeWithoutDay():
        return time.strftime("%H:%M:%S", time.localtime())




if __name__ == '__main__':
    print(type(TimeUtils.getTimeWithoutDay()))