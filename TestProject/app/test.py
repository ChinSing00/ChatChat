from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#消息提醒
from app.view import EntityItem
from ui import entity_item


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

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    from app.view.MainWin import EDMianWin
    # w = EDMianWin()
    # w.show()
    item_widget = EntityItem.EItem()
    item_widget.show()
    # item_widget.user_icon.setPixmap(QPixmap("icon/用户.svg"))
    # item_widget.user_name.setText(str(item.jid))
    sys.exit(app.exec_())