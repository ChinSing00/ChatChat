# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 585)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QWidget(Form)
        self.left.setObjectName("left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.left)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 20)
        self.verticalLayout.addWidget(self.widget)
        self.chatWin = QtWidgets.QTextBrowser(self.left)
        self.chatWin.setObjectName("chatWin")
        self.verticalLayout.addWidget(self.chatWin)
        self.widget_3 = QtWidgets.QWidget(self.left)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 1, 0, 1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.emotion = QtWidgets.QPushButton(self.widget_3)
        self.emotion.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/icon/素材中心.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emotion.setIcon(icon)
        self.emotion.setIconSize(QtCore.QSize(32, 32))
        self.emotion.setCheckable(False)
        self.emotion.setFlat(True)
        self.emotion.setObjectName("emotion")
        self.horizontalLayout_3.addWidget(self.emotion)
        self.sendimg = QtWidgets.QPushButton(self.widget_3)
        self.sendimg.setText("")
        self.sendimg.setIcon(icon)
        self.sendimg.setIconSize(QtCore.QSize(32, 32))
        self.sendimg.setAutoDefault(True)
        self.sendimg.setDefault(True)
        self.sendimg.setFlat(True)
        self.sendimg.setObjectName("sendimg")
        self.horizontalLayout_3.addWidget(self.sendimg)
        self.screenshot = QtWidgets.QPushButton(self.widget_3)
        self.screenshot.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/icon/列表.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.screenshot.setIcon(icon1)
        self.screenshot.setIconSize(QtCore.QSize(32, 32))
        self.screenshot.setAutoDefault(True)
        self.screenshot.setFlat(True)
        self.screenshot.setObjectName("screenshot")
        self.horizontalLayout_3.addWidget(self.screenshot)
        spacerItem1 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 20)
        self.verticalLayout.addWidget(self.widget_3)
        self.inputWin = QtWidgets.QTextEdit(self.left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputWin.sizePolicy().hasHeightForWidth())
        self.inputWin.setSizePolicy(sizePolicy)
        self.inputWin.setObjectName("inputWin")
        self.verticalLayout.addWidget(self.inputWin)
        self.widget_2 = QtWidgets.QWidget(self.left)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.sendmsg = QtWidgets.QPushButton(self.widget_2)
        self.sendmsg.setObjectName("sendmsg")
        self.horizontalLayout_4.addWidget(self.sendmsg)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 20)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 5)
        self.verticalLayout.setStretch(4, 1)
        self.horizontalLayout.addWidget(self.left)
        self.mid_line = QtWidgets.QFrame(Form)
        self.mid_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.mid_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mid_line.setObjectName("mid_line")
        self.horizontalLayout.addWidget(self.mid_line)
        self.right = QtWidgets.QWidget(Form)
        self.right.setObjectName("right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.right)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout.addWidget(self.right)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setToolTip(_translate("Form", "<html><head/><body><p>ToolTips?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.sendmsg.setText(_translate("Form", "发送信息"))
from src import img_rc
