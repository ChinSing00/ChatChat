import os
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow
from quamash import QApplication

import utils
from app import cache
from app.view.Animation import OpenAnimation
from app.view.entity_item_one import User_Item
from ui import main
from utils import Log
from src import img_rc

class EDMianWin(QtWidgets.QMainWindow,main.Ui_MainWindow,OpenAnimation):
    _chat2Friend_signal = pyqtSignal(dict)
    def __init__(self,parent=None):
        super(EDMianWin, self).__init__(parent)
        self.setupUi(self)
        self.iniWin()

    def iniWin(self):
        self.origan_skin = True
        self.initArrow()
        self.friends_data = {}
        desktop = QApplication.desktop()
        x = (desktop.width() - self.frameSize().width()) - 20
        y = (desktop.height() - self.frameSize().height()) // 2 - 50
        self.move(x, y)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setDuration(1000)
        self.connectToListener()

    def connectToListener(self):
        self.close_btn.clicked.connect(self.close)
        self.minimum_btn.clicked.connect(self.showMinimized)
        self.skin_btn.clicked.connect(self.changeSkin)
        self.chat_list.doubleClicked.connect(self.onTreeListClicked)

    #双击好友项打开聊天窗口
    def onTreeListClicked(self,index):
        item = self.chat_list.currentItem() #获取组
        if not isinstance(item,User_Item):
            friend_item = item.treeWidget().itemWidget(item,0) #获取到item下的widget
            print(friend_item.data)
            self._chat2Friend_signal.emit(friend_item.data)

    #加载好友，头像等数据
    def loadData(self,item):
        Log.info("加载好友数据列：",item)
        group = item['groups'][0]
        if not group in self.friends_data:
            item_list = User_Item(self.chat_list,group)
            self.friends_data[group] = item_list
        user = self.friends_data[group]
        user.setUsers(item)
        cache.user_items.append(user)  # 把该节点保存到数组用(方便下次启动快速显示)

    def initArrow(self):
        # 初始化分组arrow图标
        icon = QIcon()
        icon.addPixmap(QPixmap(":src/icon/下拉.svg"), state = QIcon.Off)
        icon.addPixmap (QPixmap(":src/icon/下拉.svg"), state = QIcon.On)
        cache.item_icon = icon
        del icon

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
                                               QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.NoIcon)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            os._exit(0)
        else:
            event.ignore()
    #重写鼠标按下事件
    def mousePressEvent(self, event):
        self.startPos = event.globalPos()  # 记录鼠标点击的位置
        return QMainWindow().mousePressEvent(event)
    #重写鼠标释放事件
    def mouseReleaseEvent(self, event):
        return QMainWindow().mouseReleaseEvent(event)
    #重写移动事件
    def mouseMoveEvent(self, event):
        movePos = event.globalPos() - self.startPos
        self.startPos = event.globalPos()
        self.move(self.pos() + movePos)
        return QMainWindow().mouseMoveEvent(event)

