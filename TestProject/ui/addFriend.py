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
        addFriend.resize(296, 240)
        self.verticalLayout = QtWidgets.QVBoxLayout(addFriend)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalFrame = QtWidgets.QFrame(addFriend)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout_5.setContentsMargins(4, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.from_jid = QtWidgets.QLabel(self.horizontalFrame)
        self.from_jid.setMinimumSize(QtCore.QSize(180, 0))
        self.from_jid.setText("")
        self.from_jid.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.from_jid.setObjectName("from_jid")
        self.horizontalLayout_5.addWidget(self.from_jid)
        spacerItem = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.top_btn_gb = QtWidgets.QFrame(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_btn_gb.sizePolicy().hasHeightForWidth())
        self.top_btn_gb.setSizePolicy(sizePolicy)
        self.top_btn_gb.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.top_btn_gb.setObjectName("top_btn_gb")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.top_btn_gb)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.minimum_btn = QtWidgets.QPushButton(self.top_btn_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimum_btn.sizePolicy().hasHeightForWidth())
        self.minimum_btn.setSizePolicy(sizePolicy)
        self.minimum_btn.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.minimum_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/icon/下拉.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimum_btn.setIcon(icon)
        self.minimum_btn.setAutoRepeat(False)
        self.minimum_btn.setFlat(True)
        self.minimum_btn.setObjectName("minimum_btn")
        self.horizontalLayout_6.addWidget(self.minimum_btn)
        self.close_btn = QtWidgets.QPushButton(self.top_btn_gb)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.close_btn.setStyleSheet("")
        self.close_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/icon/关闭.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon1)
        self.close_btn.setDefault(True)
        self.close_btn.setFlat(True)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout_6.addWidget(self.close_btn)
        self.horizontalLayout_5.addWidget(self.top_btn_gb)
        self.horizontalLayout_5.setStretch(1, 8)
        self.horizontalLayout_5.setStretch(2, 3)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.line = QtWidgets.QFrame(addFriend)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.container = QtWidgets.QWidget(addFriend)
        self.container.setObjectName("container")
        self.formLayout = QtWidgets.QFormLayout(self.container)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.searchID = QtWidgets.QLineEdit(self.container)
        self.searchID.setMinimumSize(QtCore.QSize(0, 30))
        self.searchID.setObjectName("searchID")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.searchID)
        self.nickname = QtWidgets.QLineEdit(self.container)
        self.nickname.setMinimumSize(QtCore.QSize(0, 30))
        self.nickname.setObjectName("nickname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.nickname)
        self.addto = QtWidgets.QComboBox(self.container)
        self.addto.setMinimumSize(QtCore.QSize(0, 30))
        self.addto.setObjectName("addto")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.addto)
        self.add = QtWidgets.QPushButton(self.container)
        self.add.setMinimumSize(QtCore.QSize(0, 30))
        self.add.setObjectName("add")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.add)
        self.search = QtWidgets.QPushButton(self.container)
        self.search.setMinimumSize(QtCore.QSize(0, 30))
        self.search.setObjectName("search")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.search)
        self.verticalLayout.addWidget(self.container)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 99)

        self.retranslateUi(addFriend)
        QtCore.QMetaObject.connectSlotsByName(addFriend)

    def retranslateUi(self, addFriend):
        _translate = QtCore.QCoreApplication.translate
        addFriend.setWindowTitle(_translate("addFriend", "Dialog"))
        self.add.setText(_translate("addFriend", "添加"))
        self.search.setText(_translate("addFriend", "搜索"))
from src import img_rc
