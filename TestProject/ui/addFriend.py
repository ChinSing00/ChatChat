# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addFriend.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addFriend(object):
    def setupUi(self, addFriend):
        addFriend.setObjectName("addFriend")
        addFriend.resize(424, 218)
        self.verticalLayout = QtWidgets.QVBoxLayout(addFriend)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(addFriend)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.search = QtWidgets.QPushButton(addFriend)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tlist = QtWidgets.QTableWidget(addFriend)
        self.tlist.setAutoFillBackground(False)
        self.tlist.setAutoScrollMargin(8)
        self.tlist.setAlternatingRowColors(False)
        self.tlist.setShowGrid(True)
        self.tlist.setColumnCount(4)
        self.tlist.setObjectName("tlist")
        self.tlist.setRowCount(0)
        self.verticalLayout.addWidget(self.tlist)

        self.retranslateUi(addFriend)
        QtCore.QMetaObject.connectSlotsByName(addFriend)

    def retranslateUi(self, addFriend):
        _translate = QtCore.QCoreApplication.translate
        addFriend.setWindowTitle(_translate("addFriend", "Dialog"))
        self.search.setText(_translate("addFriend", "搜索"))
        self.tlist.setSortingEnabled(False)
