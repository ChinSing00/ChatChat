from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QEvent
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox
from ofrestapi import Users
from ofrestapi.exception import UserNotFoundException

from app import Config
from utils import MyValiator
from ui import register
from app.view.Animation import OpenAnimation


class EDRegister(QtWidgets.QDialog,register.Ui_register_win,OpenAnimation):
    def __init__(self,parent=None):
        super(EDRegister, self).__init__(parent)
        self.setupUi(self)
        self.setDuration(1000)  # 设置淡入淡出
        self.connectToListener()
        self.initWin()

    def initWin(self):
        self.posMouseOrigin = QCursor().pos();
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.from_jid.setText("注册新用户")
        #设置校验器，进行非法字符校验
        MyValiator.Valida2StrNum(self,self.username)
        MyValiator.Valida2Str(self,self.nickname)
        MyValiator.Valida2StrNum(self,self.password)
        MyValiator.Valida2StrNum(self,self.password_check)
        #用户名检测,注册事件过滤器
        self.username.installEventFilter(self)
        self.username.setPlaceholderText("输入用户名")
        self.nickname.setPlaceholderText("输入昵称")
        self.password.setPlaceholderText("输入密码")
        self.password_check.setPlaceholderText("重复输入密码")

    def connectToListener(self):
        self.register_btn.clicked.connect(self.doRegister)
        self.close_btn.clicked.connect(self.close)
        self.minimum_btn.clicked.connect(self.showMinimized)
        self.password_check.textEdited[str].connect(lambda :self.onChange())
        self.password.textEdited[str].connect(lambda: self.onChange())

    def doRegister(self):
        vlidate = self.username.text() and self.nickname.text() and len(self.password.text())>=6 and (self.password_check.text()==self.password.text())
        if vlidate:
            try:
                username = self.username.text()
                pwd = self.password.text()
                nick = self.nickname.text()
                user =  Users('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)
                user.add_user(username,pwd,name=nick)
                QMessageBox.information(self, "注册成功", "账号：[{}]\nJID:[{}@{}]\n昵称:[{}]".format(username,username,Config._host,nick))
                self.close()
            except Exception:
                QMessageBox.information(self, "错误", "注册出错")

    def onChange(self):
        #密码长度校验
        if len(self.password.text())>=6:
            self.password.setStyleSheet("QLineEdit{color: black;}")
            if self.password.text() != self.password_check.text():
                self.password_check.setStyleSheet("QLineEdit{color: red;}")
                self.password_check.text()
            else:
                self.password_check.setStyleSheet("QLineEdit{color: black;}")
        else:
            self.password.setStyleSheet("QLineEdit{color: red;}")
    #事件过滤
    def eventFilter(self, widget, event):
        if widget == self.username:
            if event.type() == QEvent.FocusOut:
                if not self.username.text():
                    self.username.setStyleSheet("QLineEdit{background-color: red;opacity:0.5;}")
                    return False
                try:
                    reqUser = Users('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)
                    reqUser.get_user(self.username.text())
                    QMessageBox.information(self,"错误","该用户名已存在")
                    self.username.clear()
                    self.username.setFocus()
                except UserNotFoundException:
                    pass
                self.username.setStyleSheet("QLineEdit{background-color: none;}")
        return False

    #重写鼠标按下事件
    def mousePressEvent(self, event):
        self.posMouseOrigin = QCursor().pos()

    #重写移动事件
    def mouseMoveEvent(self, event):
        posNow=  QCursor.pos()
        posAfter = posNow - self.posMouseOrigin
        self.move(self.pos() + posAfter)
        self.posMouseOrigin = posNow