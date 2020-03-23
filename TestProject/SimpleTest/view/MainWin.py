import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QGroupBox, QVBoxLayout

from ui import main
from utils import Log
from SimpleTest.view import EntityItem
from src import img_rc #导入资源

class EDMianWin(QtWidgets.QMainWindow,main.Ui_MainWindow):
    signal2Core = pyqtSignal(int)
    def __init__(self,parent=None):
        super(EDMianWin, self).__init__(parent)
        self.setupUi(self)
        self.iniWin()

    def iniWin(self):
        self.isPressed = False
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.connectToListener()

    def connectToListener(self):
        self.close_btn.clicked.connect(self.close)
        self.minimum_btn.clicked.connect(self.showMinimized)

    #加载好友，头像等数据
    def loadData(self,roster):
        for group in roster:
            groupbox= QGroupBox(self.char_list)
            groupbox.setFlat(True)
            container_layout = QVBoxLayout()
            groupbox.setLayout(container_layout)
            self.char_list.addItem(groupbox,group)

            Log.info("加载好友列表",group)
            for item in roster[group]:
                Log.info("加载【{}】好友：".format(group), item.jid)
                self.generate_item(container_layout,item)

    def generate_item(self,container_layout,item):
        item_widget = EntityItem.EItem()
        item_widget.user_icon.setPixmap(QPixmap(":/src/icon/icon/用户.svg"))
        item_widget.user_name.setText(str(item.jid))
        container_layout.addWidget(item_widget)

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
    # 重写鼠标按下事件
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

