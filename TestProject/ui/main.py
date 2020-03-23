# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/src/icon/icon/人群.svg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow#background-image: url(:/src/images/images/main_bg1.png);")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.win_container = QtWidgets.QWidget(MainWindow)
        self.win_container.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.win_container.setStyleSheet("")
        self.win_container.setObjectName("win_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.win_container)
        self.verticalLayout_2.setContentsMargins(1, 0, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.win_container)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.minimum_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimum_btn.sizePolicy().hasHeightForWidth())
        self.minimum_btn.setSizePolicy(sizePolicy)
        self.minimum_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/src/icon/icon/下拉.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimum_btn.setIcon(icon1)
        self.minimum_btn.setAutoRepeat(False)
        self.minimum_btn.setFlat(True)
        self.minimum_btn.setObjectName("minimum_btn")
        self.horizontalLayout.addWidget(self.minimum_btn)
        self.close_btn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.close_btn.sizePolicy().hasHeightForWidth())
        self.close_btn.setSizePolicy(sizePolicy)
        self.close_btn.setStyleSheet("a{width: 20px;\n"
"            height: 20px;\n"
"            line-height: 20px;\n"
"            display: block;\n"
"            position: absolute;\n"
"            left:10px;\n"
"            top:10px;\n"
"            font-family: Helvetica, STHeiti;\n"
"            _font-family: \'\\u9ed1\\u4f53\', \'Book Antiqua\', Palatino;\n"
"            font-size: 18px;\n"
"            border-radius: 20px;\n"
"            background: #999;\n"
"            color: #FFF;\n"
"            box-shadow: 0 1px 3px rgba(0, 0, 0, .3);\n"
"            -moz-transition: linear .06s;\n"
"            -webkit-transition: linear .06s;\n"
"            transition: linear .06s;\n"
"            padding: 0;\n"
"            text-align: center;\n"
"            text-decoration: none;\n"
"            outline: none;\n"
"            cursor: pointer;}\n"
"a:hover {\n"
"            width: 24px;\n"
"            height: 24px;\n"
"            line-height: 24px;\n"
"            left:8px;\n"
"            top:8px;\n"
"            color: #FFF;\n"
"            box-shadow: 0 1px 3px rgba(209, 40, 42, .5);\n"
"            background: #d1282a;\n"
"            border-radius: 24px;\n"
"            transition: all 0.2s ease-out;\n"
"            opacity: 0.8;\n"
"        }\n"
"\n"
"\n"
"")
        self.close_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/src/icon/icon/关闭.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon2)
        self.close_btn.setDefault(True)
        self.close_btn.setFlat(True)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.tabWidget = QtWidgets.QTabWidget(self.win_container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")
        self.chat_tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_tab.sizePolicy().hasHeightForWidth())
        self.chat_tab.setSizePolicy(sizePolicy)
        self.chat_tab.setObjectName("chat_tab")
        self.tabWidget.addTab(self.chat_tab, "")
        self.conversation = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.conversation.sizePolicy().hasHeightForWidth())
        self.conversation.setSizePolicy(sizePolicy)
        self.conversation.setObjectName("conversation")
        self.char_list = QtWidgets.QToolBox(self.conversation)
        self.char_list.setGeometry(QtCore.QRect(0, 0, 331, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.char_list.sizePolicy().hasHeightForWidth())
        self.char_list.setSizePolicy(sizePolicy)
        self.char_list.setFrameShape(QtWidgets.QFrame.HLine)
        self.char_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.char_list.setLineWidth(1)
        self.char_list.setObjectName("char_list")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 327, 607))
        self.page.setObjectName("page")
        self.char_list.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_2.setObjectName("page_2")
        self.char_list.addItem(self.page_2, "")
        self.tabWidget.addTab(self.conversation, "")
        self.tab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 99)
        MainWindow.setCentralWidget(self.win_container)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.char_list.setCurrentIndex(0)
        self.char_list.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chat_tab), _translate("MainWindow", "聊天"))
        self.char_list.setItemText(self.char_list.indexOf(self.page), _translate("MainWindow", "Page 1"))
        self.char_list.setItemText(self.char_list.indexOf(self.page_2), _translate("MainWindow", "Page 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.conversation), _translate("MainWindow", "通讯录"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "暂定页"))
from src import img_rc
