# coding=utf-8
import os, sys
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

#todo python下switch语句实现
class Switch():
    def __init__(self):
        pass