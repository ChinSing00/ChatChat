from PyQt5 import QtWidgets, QtGui, QtSql
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtSql import QSqlQuery
from aioxmpp import JID

from ui import chatroom
from utils import TimeUtils


class ChatWin(QtWidgets.QWidget,chatroom.Ui_chat_win):
    _sendMsg2Friend = pyqtSignal(dict)
    _closeSignal = pyqtSignal(JID)
    def __init__(self,jid,parent=None):
        super(ChatWin, self).__init__(parent)
        self.friend_jid = jid
        self.setupUi(self)
        self.initWin()

    def initWin(self):
        self.setWindowTitle(str(self.friend_jid))
        self.connectToListener()

    def connectToListener(self):
        self.sendmsg.pressed.connect(lambda :self.btnListener(self.sendmsg))
        self.emotion.pressed.connect(lambda :self.btnListener(self.emotion))
        self.menu.pressed.connect(lambda :self.btnListener(self.menu))


    def btnListener(self,sender):

        btnName = sender.objectName()
        data = {'JID':self.friend_jid,'action':btnName}
        user_icon = "D:\CodeSave\py\ChatChat\TestProject\src\images\CustomerService.png"
        ss = '''<a>({})自己:</a><a>{}</a>'''
        if btnName == 'sendmsg':
            if self.inputWin.toPlainText() != '':
                data['msg'] = str(self.inputWin.toPlainText())
                self.inputWin.setText('')
                self.chatWin.append(ss.format(TimeUtils.getTimeWithoutDay(),data['msg']))
                self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
                self.database.setDatabaseName('data.db')
                self.database.open()
                query = QSqlQuery()
                query.prepare("")

                self._sendMsg2Friend.emit(data)
                return
            else:
                return
        elif btnName == 'emotion':
            pass
        elif btnName == 'sendimg':
            pass

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self._closeSignal.emit(self.friend_jid)
        super().closeEvent(a0)

