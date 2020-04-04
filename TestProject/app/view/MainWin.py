import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QGroupBox, QVBoxLayout
from quamash import QApplication

import utils
from app.view.Animation import OpenAnimation
from ui import main
from utils import Log
from app.view import EntityItem
from src import img_rc #导入资源

class EDMianWin(QtWidgets.QMainWindow,main.Ui_MainWindow,OpenAnimation):
    signal2Core = pyqtSignal(int)
    def __init__(self,parent=None):
        super(EDMianWin, self).__init__(parent)
        self.setupUi(self)
        self.iniWin()

    def iniWin(self):
        self.isPressed = False
        self.origan_skin = True
        self.friends_data = {}
        desktop = QApplication.desktop()
        x = (desktop.width() - self.frameSize().width())
        y = (desktop.height() - self.frameSize().height()) // 2
        self.move(x, y)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setDuration(1000)
        self.connectToListener()

    def connectToListener(self):
        self.close_btn.clicked.connect(self.close)
        self.minimum_btn.clicked.connect(self.showMinimized)
        self.skin_btn.clicked.connect(self.changeSkin)

    #加载好友，头像等数据
    def loadData(self,item):
        groupbox = None
        container_layout =None
        Log.info("加载好友数据列：",item)
        if not item['groups'][0] in self.friends_data:
            groupbox = QGroupBox(self.chat_list)
            groupbox.setFlat(True)
            container_layout = QVBoxLayout()
            container_layout.setAlignment(QtCore.Qt.AlignTop)
            groupbox.setLayout(container_layout)
            self.chat_list.addItem(groupbox, item['groups'][0])
            self.add__friend(container_layout, item)
            self.friends_data[item['groups'][0]] = container_layout
        else:
            self.add__friend(self.friends_data[item['groups'][0]], item)

    def add__friend(self,container_layout,item):
        item_widget = EntityItem.EItem()
        item_widget.setData(item)
        container_layout.addWidget(item_widget)

    def changeSkin(self):
        from PyQt5.Qt import QApplication
        if self.origan_skin:
            skin = "skin2.qss"
            self.origan_skin = False
        else:
            skin = "skin.qss"
            self.origan_skin =True
        QApplication.instance().setStyleSheet(utils.StyleReader.readQssFromFile(skin))
    def closeEvent(self, event):
        """
        对MainWindow的函数closeEvent进行重构
        退出软件时结束所有进程
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '小提示',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            os._exit(0)
        else:
            event.ignore()
    #重写鼠标按下事件
    def mousePressEvent(self, event):
        self.isPressed = True
        self.startPos = event.globalPos()  # 记录鼠标点击的位置
        return QMainWindow().mousePressEvent(event)
    #重写鼠标释放事件
    def mouseReleaseEvent(self, event):
        self.isPressed = False
        return QMainWindow().mouseReleaseEvent(event)
    #重写移动事件
    def mouseMoveEvent(self, event):
        if self.isPressed:
            # if self.win.isMaximized:
            #     self.win.showNormal()
            # 计算窗口应该移动的距离
            movePos = event.globalPos() - self.startPos
            self.startPos = event.globalPos()
            self.move(self.pos() + movePos)
        return QMainWindow().mouseMoveEvent(event)

