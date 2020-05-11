# coding=utf-8
import base64
import os, sys
import time

import aioxmpp
from PyQt5 import QtSql
from PyQt5.QtCore import Qt, QSize, QRegExp, QRectF
from PyQt5.QtGui import QPixmap, QImage, QRegExpValidator, QPicture, QPainter, QPainterPath, QPen, QColor, QBitmap
from PyQt5.QtWidgets import  QLineEdit

import app

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
#文件保存
class FileUtils():
    def __init__(self):
        pass

    def savaToPng(path,data):
        with open(path, 'wb') as file:
            file.write(data)
        file.close()
#图片处理
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
#时间处理
class TimeUtils():
    @staticmethod
    def getTimeWithoutDay():
        return time.strftime("%H:%M:%S", time.localtime())

class DBUtils():
    def __init__(self,name):
        self.DB = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.DB.setDatabaseName(name)

    @property
    def getDB(self):
        return self.DB
    def open(self):
        self.DB.open()

class MyValiator():

    @staticmethod
    def Valida2StrNum(widget,valid_to:QLineEdit):
        #数字和26个英文字母组成的字符串
        reg = QRegExp('[a-zA-z0-9]+$')
        validator = QRegExpValidator(widget)
        validator.setRegExp(reg)
        valid_to.setValidator(validator)

    @staticmethod
    def Valida2Str(widget, valid_to: QLineEdit):
        #中文、英文、数字包括下划线
        reg = QRegExp("^[\u4E00-\u9FA5A-Za-z0-9_]+$")
        validator = QRegExpValidator(widget)
        validator.setRegExp(reg)
        valid_to.setValidator(validator)

def render_avatar_image(image: QImage, size: float):
    if image.isNull():
        return None

    aspect_ratio = image.width() / image.height()
    if aspect_ratio > 1:
        width = size
        height = size / aspect_ratio
    else:
        width = size * aspect_ratio
        height = size

    x0 = (size - width) / 2
    y0 = (size - height) / 2

    path = QPainterPath()
    path.addEllipse(QRectF(x0, y0, width, height))
    picture = QPicture()
    painter = QPainter(picture)
    painter.setRenderHint(QPainter.Antialiasing,True)
    pen = QPen(Qt.black, 5)
    pen.setStyle(Qt.SolidLine)
    painter.setPen(pen)
    painter.setClipPath(path)
    painter.drawImage(
        QRectF(x0, y0, width, height),
        image,
    )
    painter.end()
    return picture
def PixmapToRound(label, icon):
    x0 = label.width()
    y0 = label.height()
    temp = QPixmap(x0,y0)
    temp.fill(Qt.transparent)
    painter = QPainter(temp)
    painter.setRenderHint(QPainter.Antialiasing, True)
    painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
    path = QPainterPath()
    path.addEllipse(0, 0, x0,y0);
    painter.setClipPath(path);
    painter.drawPixmap(0, 0, x0, y0, icon)
    painter.end()
    return temp


if __name__ == '__main__':
    print(type(TimeUtils.getTimeWithoutDay()))