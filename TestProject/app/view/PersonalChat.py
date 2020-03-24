from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal

from ui import chatroom

class PersonalChatWin(QtWidgets.QWidget,chatroom.Ui_Form):
    _sendMsg2Core = pyqtSignal(dict)
    _closeSignal = pyqtSignal(dict)
    def __init__(self,user_data,parent=None):
        super(PersonalChatWin, self).__init__(parent)
        self.user_data = user_data
        self.setupUi(self)
        self.initWin()

    def initWin(self):
        self.setWindowTitle(str(self.user_data.direct_jid))
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
        data = {'JID':self.windowTitle()}
        if btnName == 'sendmsg':
            if self.inputWin.toPlainText() != '':
                data['msg'] = str(self.inputWin.toPlainText())
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
        print(data)
        self._sendMsg2Core.emit(data)
    def checkBoxListener(self):
        pass

    def close(self):
        self._closeSignal.emit(self.user_data)
        super().close()