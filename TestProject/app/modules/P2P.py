import asyncio
from functools import partial

import aioxmpp
from PyQt5 import QtSql
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtSql import QSqlQuery
from aioxmpp import JID
from aioxmpp.im.p2p import Conversation, Member

from utils import Log, TimeUtils
from app.view.ChatWith import ChatWin

class Chat(QObject):

    def __init__(self):
        super(Chat, self).__init__()
        self._client = None
        self.conversationList = {}

    async def setup(self,core):
        self.core = core
        self._client = core.client
        Log.info("单人聊天模块", "已加载")
        await asyncio.ensure_future(self._run())

    async def _run(self):
        while True:
           await asyncio.sleep(1)

    def on_message(self,conversation ,message, member, source,**kwargs):
        '''
        :param conversation
        :param message 接收到的消息 <aioxmpp.Message>
        :param member 发送消息成员 <aioxmpp.im.conversation.AbstractConversationMember>
        :param
        '''
        # Log.info("member.conversation_jid",member.conversation_jid)
        # Log.info("member.conversation_jid",type(member.conversation_jid))
        jid = str(conversation.jid)
        win = self.conversationList[jid]['win']
        if aioxmpp.structs.LanguageTag.fromstr('en') in message.body:
            win.chatWin.append('({}){}:\n{}'.format(TimeUtils.getTimeWithoutDay(),jid,str(message.body[aioxmpp.structs.LanguageTag.fromstr('en')])))

    def delWin(self,friend_jid):
        #窗口关闭，离开会话  ps：leave()是个协程，需要将其加入并发队列
        asyncio.ensure_future(self.conversationList[str(friend_jid)]['conversation'].leave())
        del self.conversationList[str(friend_jid)]
        Log.info("P2P2", self.conversationList)

    def sendMsg(self,data):
        msg = aioxmpp.Message(
            to=data['JID'],
            type_=aioxmpp.MessageType.CHAT,
        )
        msg.body[None] = data['msg']
        self.conversationList[str(data['JID'])]['conversation'].send_message(msg)

    def on_chatwith(self,conv):
        jid = str(conv.jid)
        if jid not in self.conversationList:
            Log.info("新开窗口",jid)
            win = self.getWin(conv)
            self.conversationList[jid]['conversation'].on_message.connect(partial(self.on_message, self.conversationList[jid]['conversation']))
        win = self.conversationList[jid]['win']
        win.show()

    def getWin(self,conv):
        mFlag = str(conv.jid)
        if mFlag in self.conversationList:
            win = self.conversationList[mFlag]['win']
        else:
            win = ChatWin(conv.jid)
            win._sendMsg2Friend.connect(self.sendMsg)
            win._closeSignal.connect(self.delWin)
            data = {}
            data['win'] = win
            data['conversation'] = conv
            self.conversationList[mFlag] = data
        return win

    def initDatabase(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('data.db')
        if not self.database.isOpen():
            self.database.open()

    def insertMsg(self):
        query = QSqlQuery()
        query.prepare()