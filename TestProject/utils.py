# coding=utf-8
import os, sys
import time

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

class TimeUtils():
    @staticmethod
    def getTimeWithoutDay():
        return time.strftime("%H:%M:%S", time.localtime())

if __name__ == '__main__':
    print(type(TimeUtils.getTimeWithoutDay()))