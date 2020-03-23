import os
from PyQt5 import QtWidgets, QtSql,Qt
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtCore import pyqtSignal
from SimpleTest.view.Animation import OpenAnimation
from  utils import Log
from ui import login


class LoginDialog(QtWidgets.QDialog,login.Ui_loginWin,OpenAnimation):
    signal2Core = pyqtSignal(dict)
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.setDuration(1000)#设置淡入淡出
        self.initDatabase()
        self.connectToListener()


    def connectToListener(self):
        self.login_btn.pressed.connect(self.btnListener)

    def btnListener(self):
        if self.loginAccount.text() != "" and  self.loginPwd.text() != "":
            user={}
            user['JID'] = self.loginAccount.text()+"@192.168.123.230/S1mple"
            user['PWD'] = self.loginPwd.text()
            self.signal2Core.emit(user)
        else:
            QtWidgets.QMessageBox.information(self, '登陆错误', '账号密码不能为空！请输入！')
    def checkBoxListener(self):
        pass
    def initDatabase(self):
        Log.info('初始化数据库', 'Start')
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('data.db')
        self.database.open()
        query = QSqlQuery()
        query.prepare("create table if not exists user(id integer primary key autoincrement, account varchar(16), pwd varchar(32), is_check int default(0), last_time TIMESTAMP default (datetime('now', 'localtime')));")
        if not query.exec_():
            query.lastError()
            Log.info('初始化数据库', 'Error')
        else:
            Log.info('初始化数据库', 'Seccsess')
        query.clear()
        query.prepare('select account,pwd,is_check,MAX(last_time) from user;')
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

    def savePwdAndAutoLogin(self):
        user = {}
        user['JID'] = self.loginAccount.text() + "@192.168.123.230/S1mple"
        user['PWD'] = self.loginPwd.text()
        insert_sql = "insert or replace into  user(account,pwd,is_check,last_time) values(?,?,?,datetime('now', 'localtime'));"  # 插入或更新(数据已存在)数据
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

