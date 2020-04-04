import asyncio
import os
from functools import partial
import aioxmpp

from aioxmpp import AvatarService
from ofrestapi import Users
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#消息提醒
import app
from app import Config



class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.showMenu()
        self.other()

    def showMenu(self):
        "设计托盘的菜单，这里我实现了一个二级菜单"
        self.menu = QMenu()
        self.menu1 = QMenu()
        self.showAction1 = QAction("显示消息1", self, triggered=self.showM)
        self.showAction2 = QAction("显示消息2", self,triggered=self.showM)
        self.quitAction = QAction("退出", self, triggered=self.quit)

        self.menu1.addAction(self.showAction1)
        self.menu1.addAction(self.showAction2)
        self.menu.addMenu(self.menu1, )

        self.menu.addAction(self.showAction1)
        self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.menu1.setTitle("二级菜单")
        self.setContextMenu(self.menu)

    def other(self):
        self.activated.connect(self.iconClied)
        #把鼠标点击图标的信号和槽连接
        self.messageClicked.connect(self.mClied)
        #把鼠标点击弹出消息的信号和槽连接
        self.setIcon(QIcon("D:\CodeSave\py\TestProject\src\images\loading4.gif"))
        self.icon = self.MessageIcon()
        #设置图标

    def iconClied(self, reason):
        "鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击"
        if reason == 2 or reason == 3:
            pw = self.parent()
            if pw.isVisible():
                pw.hide()
            else:
                pw.show()
        print(reason)

    def mClied(self):
        self.showMessage("提示", "你点了消息", self.icon)

    def showM(self):

        self.showMessage("测试", "我是消息", self.icon)

    def quit(self):
        "保险起见，为了完整的退出"
        self.setVisible(False)
        self.parent().exit()
        qApp.quit()
        sys.exit()

class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        ti = TrayIcon(self)
        ti.show()

from app.view.PersonalChat import PersonalChatWin
class win1(PersonalChatWin):
    def __init__(self,paren=None):
        super(win1,self).__init__(paren)

    def printSome(self,title):
        if title == self.windowTitle():
            print('this is {}'.format(self.windowTitle()))
    def setTxt(self,txt,win):
        if win == self.windowTitle():
            self.chatWin.setText(txt)


from app.view.Animation import OpenAnimation
class win2(QMainWindow,OpenAnimation):
    def __init__(self, parent=None):
        super(win2, self).__init__(parent)
        self.setDuration(1000)
        self.resize(448, 292)
        self.setWindowTitle('win2')
        self.btn = QPushButton(self)
        self.openWinCount = 0;
        self.btn.clicked.connect(self.openWin)

    def openWin(self):
        Signal().ShowWin()

class Signal(QObject):
    win2_sin = pyqtSignal(int)
    win1_sin = pyqtSignal(int)
    openWinCount = 0
    winList = {}
    def __init__(self):
        pass

    def ShowWin(self):
        win = win1()
        print(win,self.openWinCount)
        self.openWinCount += 1
        win.setWindowTitle('ChatWin{}'.format(self.openWinCount))
        self.winList[win.windowTitle()] = win
        win.show()
        print(self.winList)

    def send(self):
        self.win1_sin.emit('收到这条信息了！','ChatWin3')

    #单例实现
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Signal, cls).__new__(cls)
        return cls._instance

class core():
    def __init__(self):
        pass
def disco_callback(task):
    result = task.result()
    print(result.to_dict())
    for item in result.to_dict()["features"]:
        aioxmpp.disco.register_feature(item)
def subscribeava(task):
    result = task.result()
    print(result)
def callback(jid,task):
    result = task.result()
    print(result)
    for i in result:
        if i != None:
            print(i)
            sa = asyncio.ensure_future(i.get_image_bytes())
            sa.add_done_callback(partial(cb,jid))
def cb(jid,task):
    print(task.result())
    if task.result() != None:
        binimg = task.result()
        #print(binimg)
        path = os.path.join(app.BASE_DIR, 'avatar', '{}.png'.format(jid))
        with open(path, 'wb') as file:
            file.write(binimg)
        file.close()
async def get_all(ava,friendlist):
    tasks = []
    for item in friendlist:
        print(item['jid'])
        task = asyncio.get_event_loop().create_task(ava.get_avatar_metadata(aioxmpp.JID.fromstr(item['jid']), require_fresh=True))
        task.add_done_callback(partial(callback,item['jid']))
        tasks.append(task)
    await asyncio.gather(*tasks)
if __name__ == "__main__":
    import sys
    #app = QApplication(sys.argv)

    loop = asyncio.get_event_loop()
    mUser = Users('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)
    lista = mUser.get_user_roster('admin')
    # print(list)
    JID = aioxmpp.JID.fromstr("admin@192.168.123.230")
    client = aioxmpp.PresenceManagedClient(JID, aioxmpp.make_security_layer("qin1029.", no_verify=True) )
    client.start()
    # discoClient = client.summon(DiscoClient)
    # task = loop.create_task(discoClient.query_info(JID))
    # task.add_done_callback(disco_callback)
    # 用户头像
    ava = client.summon(AvatarService)
    task = loop.create_task(get_all(ava,lista['rosterItem']))
    loop.run_until_complete(task)

