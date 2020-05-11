import asyncio
import os
import time
from datetime import datetime

from PyQt5 import QtWidgets, QtCore, QtSql
from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem
from ofrestapi import Muc
from quamash import QApplication

import utils
from app import cache, Config
from app.view.Animation import OpenAnimation
from app.view.FriendItem import User_Item, Child_Item
from app.view.RoomItem import Room_Item
from ui import main
from utils import Log
from src import img_rc

class EDMianWin(QtWidgets.QMainWindow,main.Ui_MainWindow,OpenAnimation):
    _chat2Friend_signal = pyqtSignal(dict)
    _chat2Room_signal = pyqtSignal(dict)
    def __init__(self,parent=None):
        super(EDMianWin, self).__init__(parent)
        self.setupUi(self)
        self.iniWin()

    def iniWin(self):
        self.origan_skin = True
        self.initArrow()
        self.friends_data = {}
        self.rooms_data = {}
        self.templist = {}
        self.history_datalist = {}
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
        self.room_list.itemDoubleClicked.connect(self.onRoomListClicked)
        self.history_list.itemDoubleClicked.connect(self.onHistoryClicked)

    #双击好友项打开聊天窗口
    def onTreeListClicked(self,index):
        item = self.chat_list.currentItem() #获取组
        if not isinstance(item,User_Item):
            friend_item = item.treeWidget().itemWidget(item,0) #获取到item下的widget
            # print(friend_item.data)
            self._chat2Friend_signal.emit(friend_item.data)
            self.loadHistoryChat({'entity_jid': friend_item.data['jid'], 'time': datetime.now()})

    def onRoomListClicked(self,item):
        # print(item)
        # print(item.listWidget().itemWidget(item))
        data = item.listWidget().itemWidget(item).data
        self._chat2Room_signal.emit(data)
        jid = data['roomName'] + '@' + Config._mucService
        self.loadHistoryChat({'entity_jid': jid, 'time': datetime.now()})

    def onHistoryClicked(self,item):
        entity = item.listWidget().itemWidget(item)
        jid = None
        if isinstance(entity,Child_Item):
            self._chat2Friend_signal.emit(entity.data)
            jid = entity.data['jid']
        elif isinstance(entity,Room_Item):
            self._chat2Room_signal.emit(entity.data)


    #加载好友，头像等数据
    def loadData(self,item):
        # Log.info("加载好友数据列：",item)
        group = item['groups'][0]
        self.templist[item['jid']] = item
        if not group in self.friends_data:
            item_list = User_Item(self.chat_list,group)
            self.friends_data[group] = item_list
        user = self.friends_data[group]
        user.setUsers(item)

        cache.user_items.append(user)  # 把该节点保存到数组用(方便下次启动快速显示)

    def loadRoom(self,room_data):
        item = QListWidgetItem()
        item.setSizeHint(QSize(270,65))
        self.room_list.addItem(item)
        widget = Room_Item(room_data=room_data)
        self.room_list.setItemWidget(item,widget)

    def loadHistoryChat(self,entityData):
        if entityData['entity_jid'] in self.history_datalist:
            return
        item = QListWidgetItem()
        self.history_list.addItem(item)
        item.setSizeHint(QSize(270, 65))
        friend = '@{}'.format(Config._host)
        room = '@{}'.format(Config._mucService)
        widget =None
        if entityData["entity_jid"].endswith(friend):
            if entityData["entity_jid"] in self.templist:
                item.setSizeHint(QSize(270, 50))
                user = self.templist[entityData["entity_jid"]]
                widget =Child_Item(user=user)
        elif entityData["entity_jid"].endswith(room):
            roomRestApi = Muc('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)
            data =  roomRestApi.get_room(entityData["entity_jid"].replace(room,''))
            widget = Room_Item(room_data=data)
        else:
            return
        self.history_datalist[entityData["entity_jid"]] = widget
        self.history_list.setItemWidget(item, widget)

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
        database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        database.setDatabaseName('data.db')
        database.close()
        self._client.stop()
        asyncio.get_event_loop().stop()
        asyncio.get_event_loop().close()
        QApplication.instance().closingDown()
        os._exit(0)
        # """
            # 对MainWindow的函数closeEvent进行重构
            # 退出软件时结束所有进程
            # """
            # reply = QtWidgets.QMessageBox.question(self,
            #                                        '小提示',
            #                                        "是否要退出程序？",
            #                                        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            #                                        QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.NoIcon)
            # if reply == QtWidgets.QMessageBox.Yes:
            #     event.accept()
            #     os._exit(0)
            # else:
            #     event.ignore()
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

    def setClient(self,client):
        self._client = client