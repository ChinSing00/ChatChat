# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(780, 585)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QWidget(Form)
        self.left.setObjectName("left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.left)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.widget)
        self.chatWin = QtWidgets.QTextBrowser(self.left)
        self.chatWin.setObjectName("chatWin")
        self.verticalLayout.addWidget(self.chatWin)
        self.widget_3 = QtWidgets.QWidget(self.left)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.emotion = QtWidgets.QPushButton(self.widget_3)
        self.emotion.setObjectName("emotion")
        self.horizontalLayout_3.addWidget(self.emotion)
        self.sendimg = QtWidgets.QPushButton(self.widget_3)
        self.sendimg.setObjectName("sendimg")
        self.horizontalLayout_3.addWidget(self.sendimg)
        self.screenshot = QtWidgets.QPushButton(self.widget_3)
        self.screenshot.setObjectName("screenshot")
        self.horizontalLayout_3.addWidget(self.screenshot)
        spacerItem1 = QtWidgets.QSpacerItem(96, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_3)
        self.inputWin = QtWidgets.QTextEdit(self.left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputWin.sizePolicy().hasHeightForWidth())
        self.inputWin.setSizePolicy(sizePolicy)
        self.inputWin.setObjectName("inputWin")
        self.verticalLayout.addWidget(self.inputWin)
        self.widget_2 = QtWidgets.QWidget(self.left)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.sendmsg = QtWidgets.QPushButton(self.widget_2)
        self.sendmsg.setObjectName("sendmsg")
        self.horizontalLayout_4.addWidget(self.sendmsg)
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout.addWidget(self.left)
        self.right = QtWidgets.QWidget(Form)
        self.right.setObjectName("right")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.right)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout.addWidget(self.right)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        Form.setToolTip(_translate("Form", "<html><head/><body><p>ToolTips?</p></body></html>"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.emotion.setText(_translate("Form", "emotion"))
        self.sendimg.setText(_translate("Form", "sendimg"))
        self.screenshot.setText(_translate("Form", "screenshot"))
        self.sendmsg.setText(_translate("Form", "发送"))
