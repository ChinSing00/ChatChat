import time

from PyQt5 import QtWidgets, QtGui, QtSql, QtCore
from PyQt5.QtCore import pyqtSignal, QSize, QPoint
from PyQt5.QtGui import QCursor
from PyQt5.QtSql import QSqlQuery
from aioxmpp import JID

from app import Config
from app.view.ChatMucInfoWidget import CMIWidget
from ui import chatroom
from utils import TimeUtils


class ChatWin(QtWidgets.QWidget,chatroom.Ui_chat_win):
    _sendMsg2Friend = pyqtSignal(dict)
    _closeSignal = pyqtSignal(JID)
    def __init__(self,jid,selfJid,parent=None):
        super(ChatWin, self).__init__(parent)
        self.jid = jid
        self.selfJid = selfJid
        self.setupUi(self)
        self.initWin()

    def initWin(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.from_jid.setText(str(self.jid))
        self.connectToListener()

    def connectToListener(self):
        self.sendmsg.pressed.connect(lambda :self.btnListener(self.sendmsg))
        self.close_btn.clicked.connect(self.close)
        self.minimum_btn.clicked.connect(self.showMinimized)

    def setChatInfor(self,jid):
        friend = '@{}'.format(Config._host)
        room = '@{}'.format(Config._mucService)
        if jid.endswith(friend):
            pass
        if jid.endswith(room):
            self.right.setAlignment(QtCore.Qt.AlignTop)
            widget = CMIWidget(jid, self.core)
            widget.setFixedSize(QSize(180,472))
            self.right.addWidget(widget)

    def btnListener(self,sender):

        btnName = sender.objectName()
        data = {'JID':self.jid,'action':btnName}
        user_icon = "D:\CodeSave\py\ChatChat\TestProject\src\images\CustomerService.png"
        ss = '''<a>({})自己:</a><a>{}</a>'''
        if btnName == 'sendmsg':
            if self.inputWin.toPlainText() != '':
                data['msg'] = str(self.inputWin.toPlainText())
                self.inputWin.setText('')
                self.chatWin.append(ss.format(TimeUtils.getTimeWithoutDay(),data['msg']))
                self._sendMsg2Friend.emit(data)
                self.insertMsg(userName=self.selfJid,isSelf=1,chatWith=str(self.jid),messageFrom=str(self.jid),messageContext=data['msg'],createTime=time.time())
                return
            else:
                return
        # elif btnName == 'emotion':
        #     pass
        # elif btnName == 'sendimg':
        #     pass
    def setCore(self,core):
        self.core = core
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self._closeSignal.emit(self.jid)
        super().closeEvent(a0)

    def getHistoryMsg(self):
        try:
            query = QSqlQuery()
            sql = "select * from message where chatWith='{}' ORDER BY createTime ASC limit 20;".format(str(self.jid))
            print(sql)
            query.prepare(sql)
            if not query.exec_():
                print("查询出错")
                query.lastError()
            else:
                print("查询成功")
            while query.next():
                userName, isSelf, chatWith, messageFrom, messageContext, createTime=query.value(0),query.value(1),query.value(2),query.value(3),query.value(4),query.value(5)
                time_local = time.localtime(createTime / 1000)
                dt = time.strftime("%d %H:%M:%S", time_local)
                msg = ''
                if isSelf==1:
                    msg = '''<a>({})自己:</a><a>{}</a>'''.format(dt,messageContext)
                else:
                    msg = '''<a>({}){}:</a><a>{}</a>'''.format(dt,messageFrom,messageContext)
                print(msg)
                self.chatWin.append(msg)
        except Exception:
            return
    def insertMsg(self, userName, isSelf, chatWith, messageFrom, messageContext, createTime):
        try:
            query = QSqlQuery()
            sql = "insert into message(userName, isSelf, chatWith, messageFrom , messageContext,createTime) values('{}',{},'{}','{}','{}',{});".format(
                userName,
                isSelf,
                chatWith,
                messageFrom,
                messageContext,
                createTime)
            print("userName={},isSelf={},chatWith={},messageFrom={},messageContext={},createTime={}".format(userName,
                                                                                                            isSelf,
                                                                                                            chatWith,
                                                                                                            messageFrom,
                                                                                                            messageContext,
                                                                                                            createTime))
            query.prepare(sql)
            if not query.exec_():
                print("插入出错")
                query.lastError()
            else:
                print("插入成功")
            query.clear()
            del query
        except Exception:
            return

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        super().showEvent(a0)
        self.getHistoryMsg()

    #重写鼠标按下事件
    def mousePressEvent(self, event):
        self.posMouseOrigin = QCursor().pos();

    #重写移动事件
    def mouseMoveEvent(self, event):
        posNow=  QCursor.pos()
        posAfter = posNow - self.posMouseOrigin;
        self.move(self.pos() + posAfter);
        self.posMouseOrigin = posNow;