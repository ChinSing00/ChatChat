# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginWin(object):
    def setupUi(self, loginWin):
        loginWin.setObjectName("loginWin")
        loginWin.resize(458, 315)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loginWin.sizePolicy().hasHeightForWidth())
        loginWin.setSizePolicy(sizePolicy)
        loginWin.setAutoFillBackground(True)
        loginWin.setStyleSheet("")
        loginWin.setModal(True)
        self.layoutWidget = QtWidgets.QWidget(loginWin)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 130, 212, 107))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.autoLogin = QtWidgets.QCheckBox(self.layoutWidget)
        self.autoLogin.setObjectName("autoLogin")
        self.horizontalLayout_3.addWidget(self.autoLogin)
        self.remeberPwd = QtWidgets.QCheckBox(self.layoutWidget)
        self.remeberPwd.setObjectName("remeberPwd")
        self.horizontalLayout_3.addWidget(self.remeberPwd)
        self.retrievePwd = QtWidgets.QLabel(self.layoutWidget)
        self.retrievePwd.setObjectName("retrievePwd")
        self.horizontalLayout_3.addWidget(self.retrievePwd)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.login_btn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_4.addWidget(self.login_btn)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.loginPwd = QtWidgets.QLineEdit(self.layoutWidget)
        self.loginPwd.setMaxLength(32)
        self.loginPwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginPwd.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.loginPwd.setObjectName("loginPwd")
        self.horizontalLayout_2.addWidget(self.loginPwd)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.loginAccount = QtWidgets.QLineEdit(self.layoutWidget)
        self.loginAccount.setObjectName("loginAccount")
        self.horizontalLayout.addWidget(self.loginAccount)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)

        self.retranslateUi(loginWin)
        QtCore.QMetaObject.connectSlotsByName(loginWin)

    def retranslateUi(self, loginWin):
        _translate = QtCore.QCoreApplication.translate
        loginWin.setWindowTitle(_translate("loginWin", "登陆"))
        self.autoLogin.setText(_translate("loginWin", "自动登陆"))
        self.remeberPwd.setText(_translate("loginWin", "记住密码"))
        self.retrievePwd.setText(_translate("loginWin", "注册账号"))
        self.login_btn.setText(_translate("loginWin", "登陆"))
        self.label_2.setText(_translate("loginWin", "密  码"))
        self.label.setText(_translate("loginWin", "用户名"))

from src import img_rc
