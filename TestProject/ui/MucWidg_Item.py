# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MucWidg_Item.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(172, 50)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(4, 2, 2, 2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QLabel(Form)
        self.icon.setMinimumSize(QtCore.QSize(40, 32))
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.name = QtWidgets.QLabel(Form)
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.icon.setText(_translate("Form", "TextLabel"))
        self.name.setText(_translate("Form", "TextLabel"))
