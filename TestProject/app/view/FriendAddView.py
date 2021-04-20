from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QCursor
from ofrestapi import Users
from ofrestapi.exception import UserNotFoundException

from app import Config
from ui.addFriend import Ui_addFriend
from utils import Log


class AddFirendWin(QtWidgets.QDialog,Ui_addFriend):
    _Sign_Mian = pyqtSignal(str)
    def __init__(self,core=None,parent=None):
        super(AddFirendWin, self).__init__(parent)
        self.core = core
        self.setupUi(self)
        self.initWin()

    def initWin(self):
        self.posMouseOrigin = QCursor().pos();
        self.search.clicked.connect(self.searchFriend)
        self.nickname.setDisabled(True)
        self.add.setDisabled(True)
        self.addto.setDisabled(True)
        self.addto.setCurrentIndex(0)
        self.nickname.setPlaceholderText('昵称')
        self.searchID.setPlaceholderText('用户名')
        self.close_btn.clicked.connect(self.close)
        self.minimum_btn.clicked.connect(self.showMinimized)

    def searchFriend(self):
        self.addto.clear()
        groupList =[]
        jid = str(self.core.jid)
        jid_withoutDomian=jid.replace('@{}'.format(Config._host),'')
        _user = Users('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)

        if not self.searchID.text() and self.searchID.text()!=jid_withoutDomian:
            return

        friends = _user.get_user_roster(jid_withoutDomian)
        for friend in friends['rosterItem']:
            print(friend)
            if friend['groups']:
                if friend['groups'][0] not in groupList:
                    groupList.append(friend['groups'][0])
            if self.searchID.text() in friend['jid']:
                Log.info("添加用户","用户已在好友列表！")
                return

        friendName = self.searchID.text()
        searchList = None
        try:
            searchList = _user.get_user(friendName)
        except UserNotFoundException:
            QtWidgets.QMessageBox.information(self, '查询好友', '服务器中没有好友的信息！')

        if not searchList:
            Log.info("添加用户", "用户不存在于服务器上！")
            return
        print(searchList)
        index = 1
        for group in groupList:
            print(group)
            self.addto.addItem(group)
            index=index+1

        self.nickname.setEnabled(True)
        self.nickname.setText(searchList['name'])
        self.add.setEnabled(True)
        self.addto.setEnabled(True)

    #重写鼠标按下事件
    def mousePressEvent(self, event):
        self.posMouseOrigin = QCursor().pos()

    #重写移动事件
    def mouseMoveEvent(self, event):
        posNow=  QCursor.pos()
        posAfter = posNow - self.posMouseOrigin
        self.move(self.pos() + posAfter)
        self.posMouseOrigin = posNow
