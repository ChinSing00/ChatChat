# encoding: utf-8
import asyncio
from PyQt5.Qt import QApplication
from SimpleTest.Core import core
from SimpleTest.view.MainWin import EDMianWin
from SimpleTest.view.EDlogin import LoginDialog
import quamash

from utils import StyleReader


def coreNLogin_Conn(loginWin,core):
    loginWin.signal2Core.connect(core.start)#接收Login信号
    core._sign_login.connect(loginWin.LoginDone)#接收LoginDone信号
    loginWin.show()
if __name__ == '__main__':
    app = QApplication([])
    style = StyleReader.readQssFromFile("skin.qss")
    app.setStyleSheet(style)#设置全局皮肤样式
    loop = quamash.QEventLoop(app) #使用Quamash的事件循环（使aioxmpp与pyqt5的事件循环可以互通）不使用会导致登陆画面不能正常初始化
    asyncio.set_event_loop(loop)
    loop.set_debug(True)
    with loop:
        try:
            core = core(loop)
            loginWin = LoginDialog()
            coreNLogin_Conn(loginWin,core)
            loop.run_forever()
        except Exception:
            print(Exception.__name__)
    app.exec_()
