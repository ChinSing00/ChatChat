# encoding: utf-8
import asyncio
import os
import sys
import qdarkgraystyle
from PyQt5 import QtGui, QtCore
from PyQt5.Qt import QApplication
from app.Core import core
from app.view.EDlogin import LoginDialog
import quamash

from utils import StyleReader, Log


def coreNLogin_Conn(loginWin,core):
    loginWin.signal2Core.connect(core.start)#接收Login信号
    core._sign_login.connect(loginWin.LoginDone)#接收LoginDone信号
    loginWin.open()

if __name__ == '__main__':
    app = QApplication([])
    style = StyleReader.readQssFromFile("skin.qss")
    #app.setStyleSheet(style)#设置全局皮肤样式

    # 使用Quamash的事件循环（使aioxmpp与pyqt5的事件循环可以互通）不使用会导致登陆画面不能正常初始化\
    with quamash.QEventLoop(app) as loop:
        asyncio.set_event_loop(loop)
        try:
            core = core(loop)
            loginWin = LoginDialog()
            coreNLogin_Conn(loginWin,core)
            loop.run_forever()
            sys.exit(app.exec_())
        except Exception:
            Log.info("初始化出错","appMian")
