# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chatroom.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_chat_win(object):
    def setupUi(self, chat_win):
        chat_win.setObjectName("chat_win")
        chat_win.resize(646, 542)
        chat_win.setToolTip("")
        self.horizontalLayout = QtWidgets.QHBoxLayout(chat_win)
        self.horizontalLayout.setContentsMargins(5, 2, 5, 2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left = QtWidgets.QWidget(chat_win)
        self.left.setObjectName("left")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.left)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chatWin = QtWidgets.QTextBrowser(self.left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chatWin.sizePolicy().hasHeightForWidth())
        self.chatWin.setSizePolicy(sizePolicy)
        self.chatWin.setFrameShape(QtWidgets.QFrame.Box)
        self.chatWin.setFrameShadow(QtWidgets.QFrame.Plain)
        self.chatWin.setLineWidth(1)
        self.chatWin.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.chatWin.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.chatWin.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.chatWin.setOverwriteMode(False)
        self.chatWin.setObjectName("chatWin")
        self.verticalLayout.addWidget(self.chatWin)
        self.widget_3 = QtWidgets.QWidget(self.left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 1, 0, 1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(96, 6, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_3.setStretch(0, 20)
        self.verticalLayout.addWidget(self.widget_3)
        self.inputWin = QtWidgets.QTextEdit(self.left)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputWin.sizePolicy().hasHeightForWidth())
        self.inputWin.setSizePolicy(sizePolicy)
        self.inputWin.setFrameShadow(QtWidgets.QFrame.Plain)
        self.inputWin.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextEditable|QtCore.Qt.TextEditorInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.inputWin.setObjectName("inputWin")
        self.verticalLayout.addWidget(self.inputWin)
        self.widget_2 = QtWidgets.QWidget(self.left)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.sendmsg = QtWidgets.QPushButton(self.widget_2)
        self.sendmsg.setObjectName("sendmsg")
        self.horizontalLayout_4.addWidget(self.sendmsg)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 20)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(3, 1)
        self.horizontalLayout.addWidget(self.left)
        self.right = QtWidgets.QVBoxLayout()
        self.right.setContentsMargins(-1, 0, -1, 0)
        self.right.setSpacing(0)
        self.right.setObjectName("right")
        self.horizontalLayout.addLayout(self.right)
        self.horizontalLayout.setStretch(0, 99)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(chat_win)
        QtCore.QMetaObject.connectSlotsByName(chat_win)

    def retranslateUi(self, chat_win):
        _translate = QtCore.QCoreApplication.translate
        chat_win.setWindowTitle(_translate("chat_win", "Form"))
        self.chatWin.setHtml(_translate("chat_win", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ff0000;\"><br /></p></body></html>"))
        self.inputWin.setHtml(_translate("chat_win", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sendmsg.setText(_translate("chat_win", "发送信息"))
from src import img_rc
