from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

from ui import chatroom
from utils import TimeUtils


class PersonalChatWin(QtWidgets.QWidget,chatroom.Ui_Form):
    _sendMsg2Friend = pyqtSignal(dict)
    _closeSignal = pyqtSignal(dict)
    def __init__(self,jid,parent=None):
        super(PersonalChatWin, self).__init__(parent)
        self.  friend_jid = jid
        self.setupUi(self)
        self.initWin()

    def initWin(self):
        self.setWindowTitle(str(self.friend_jid))
        self.connectToListener()
        self.show()

    def connectToListener(self):
        self.sendmsg.pressed.connect(lambda :self.btnListener(self.sendmsg))
        self.emotion.pressed.connect(lambda :self.btnListener(self.emotion))
        self.sendimg.pressed.connect(lambda :self.btnListener(self.sendmsg))
        self.screenshot.pressed.connect(lambda :self.btnListener(self.screenshot))

    def btnListener(self,sender):
        print(sender.objectName())
        btnName = sender.objectName()
        data = {'JID':self.friend_jid,'action':btnName}
        user_icon = "D:\CodeSave\py\ChatChat\TestProject\src\images\CustomerService.png"
        ss = '''<div class="">
                  <div>
                    <img src="{}">
                  </div>
                  <div>
                    <div class=""></div>
                    <span>{}</span>
                  </div>
                </div>'''
        if btnName == 'sendmsg':
            if self.inputWin.toPlainText() != '':
                data['msg'] = str(self.inputWin.toPlainText())
                self.inputWin.setText('')
                #self.chatWin.append('({}):\n{}'.format(TimeUtils.getTimeWithoutDay(),ss+data['msg']))
                self.chatWin.append(ss.format(user_icon,data['msg']))
            else:
                return
        elif btnName == 'emotion':
            pass
        elif btnName == 'sendimg':
            pass
        elif btnName == 'screenshot':
            pass
        elif btnName == 'todo1':
            pass
        elif btnName == 'todo2':
            pass
        elif btnName == 'todo3':
            pass
        self._sendMsg2Friend.emit(data)
    def checkBoxListener(self):
        pass

    def close(self):
        self._closeSignal.emit(self.friend_jid)
        super().close()