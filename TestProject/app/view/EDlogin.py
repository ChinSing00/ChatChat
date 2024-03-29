import os
from PyQt5 import QtWidgets, QtSql, Qt, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import pyqtSignal
from app.view.Animation import OpenAnimation
from utils import Log, MyValiator
from ui import login
from app import Config


class LoginDialog(QtWidgets.QDialog,login.Ui_loginWin,OpenAnimation):
    signal2Core = pyqtSignal(dict)
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.initWin()
        self.initDatabase()

    def initWin(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.from_jid.setText('登录')
        self.setDuration(1000)#设置淡入淡出
        self.loginAccount.setPlaceholderText("用户名")
        self.loginPwd.setPlaceholderText("密码")
        MyValiator.Valida2StrNum(self,self.loginAccount)
        #MyValiator.Valida2StrNum(self,self.loginPwd)
        self.connectToListener()

    def connectToListener(self):
        self.login_btn.pressed.connect(self.btnListener)
        self.loginAccount.textChanged.connect(self.loginPwd.clear)
        self.close_btn.clicked.connect(self.close)
        self.minimum_btn.clicked.connect(self.showMinimized)
        self.remeberPwd.toggled[bool].connect(self.onChecked)
    def onChecked(self,bool):
        if not bool:
            self.loginAccount.clear()
            self.loginPwd.clear()
    def btnListener(self):
        if self.loginAccount.text() != "" and  self.loginPwd.text() != "":
            user={}
            user['JID'] ="{}@{}".format(self.loginAccount.text(),Config._host)
            user['PWD'] = self.loginPwd.text()
            self.signal2Core.emit(user)
            self.login_btn.setDisabled(True)
        else:
            QtWidgets.QMessageBox.information(self, '登陆错误', '账号密码不能为空！请输入！')

    def initDatabase(self):
        Log.info('初始化数据库', 'Start')
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('data.db')
        self.database.open()
        query = QSqlQuery()
        query.prepare("create table if not exists user(id integer primary key autoincrement, userName varchar(64), password varchar(32), isRemember int default(0), loginTime TIMESTAMP default (datetime('now', 'localtime')));")
        if not query.exec_():
            query.lastError()
            Log.info('初始化数据库', 'Error')
        else:
            Log.info('初始化数据库', 'Seccsess')
        query.clear()
        query.prepare('select userName,password,isRemember,MAX(loginTime) from user;')
        query.exec_()
        while query.next():
            acc,pwd ,isCheck,time= query.value(0),query.value(1),query.value(2),query.value(3)
            print('acc={},pwd={},isCheck={},time={}\n'.format(acc, pwd, isCheck, time))
            if isCheck == 1 :
                self.loginAccount.setText(acc)
                self.loginPwd.setText(pwd)
                self.remeberPwd.setChecked(True)
    def LoginDone(self,flag):
        if flag == 1:
            self.savePwdAndAutoLogin()
            self.database.close()
            self.close()
        elif flag == 0:
            QtWidgets.QMessageBox.information(self,'登陆错误', '密码或账号错误！请重新登陆！')
            self.login_btn.setEnabled(True)

    def savePwdAndAutoLogin(self):
        user = {}
        user['JID'] = '{}@{}'.format(self.loginAccount.text(),Config._host)
        user['PWD'] = self.loginPwd.text()
        insert_sql = "insert or replace into  user(userName,password,isRemember,loginTime) values(?,?,?,datetime('now', 'localtime'));"  # 插入或更新(数据已存在)数据
        query = QSqlQuery()
        query.prepare(insert_sql)
        query.addBindValue(self.loginAccount.text())
        query.addBindValue(user['PWD'])
        if self.remeberPwd.isChecked() == True:
            query.addBindValue(1)
        else:
            query.addBindValue(0)
        if not query.exec_():
            print("插入出错")
            query.lastError()
        else:
            print("插入成功")
        self.signal2Core.disconnect()


    #重写鼠标按下事件
    def mousePressEvent(self, event):
        self.posMouseOrigin = QCursor().pos()

    #重写移动事件
    def mouseMoveEvent(self, event):
        posNow=  QCursor.pos()
        posAfter = posNow - self.posMouseOrigin
        self.move(self.pos() + posAfter)
        self.posMouseOrigin = posNow