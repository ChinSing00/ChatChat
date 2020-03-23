# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entity_item.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(271, 68)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.user_icon = QtWidgets.QLabel(self.widget)
        self.user_icon.setGeometry(QtCore.QRect(10, 10, 80, 52))
        self.user_icon.setText("")
        self.user_icon.setTextFormat(QtCore.Qt.PlainText)
        self.user_icon.setPixmap(QtGui.QPixmap(":/src/icon/icon/用户.svg"))
        self.user_icon.setObjectName("user_icon")
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.user_name = QtWidgets.QLabel(self.widget_2)
        self.user_name.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.user_name.setWordWrap(True)
        self.user_name.setObjectName("user_name")
        self.verticalLayout.addWidget(self.user_name)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.widget_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.user_name.setText(_translate("Form", "好友名称"))
        self.label_3.setText(_translate("Form", "签名动态"))
from src import img_rc
