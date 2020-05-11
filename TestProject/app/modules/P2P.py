import asyncio
import os
import time
from functools import partial

import aioxmpp
from PyQt5 import QtSql
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQuery
from aioxmpp import JID
from aioxmpp.im.p2p import Conversation, Member

from app import getAvatarRootPath
from utils import Log, TimeUtils
from app.view.ChatWith import ChatWin

class Chat(QObject):
    _Sign_Close_Conv =pyqtSignal(str)
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

            self.insertMsg(userName=str(self.core.jid),isSelf=0,chatWith=str(conversation.jid),messageFrom=jid,messageContext=str(message.body[aioxmpp.structs.LanguageTag.fromstr('en')]),createTime=time.time())
            win.chatWin.append('({}){}:\n{}'.format(TimeUtils.getTimeWithoutDay(),jid,str(message.body[aioxmpp.structs.LanguageTag.fromstr('en')])))

    def delWin(self,friend_jid):
        #窗口关闭，离开会话  ps：leave()是个协程，需要将其加入并发队列
        asyncio.ensure_future(self.conversationList[str(friend_jid)]['conversation'].leave())
        del self.conversationList[str(friend_jid)]
        self._Sign_Close_Conv.emit(str(friend_jid))
        Log.info("关闭聊天窗口", self.conversationList)

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
            win = self.getWin(conv)
            self.conversationList[jid]['conversation'].on_message.connect(partial(self.on_message, self.conversationList[jid]['conversation']))
            Log.info("新开窗口", self.conversationList[jid]['conversation'])
        win = self.conversationList[jid]['win']
        win.show()

    def getWin(self,conv):
        mFlag = str(conv.jid)
        if mFlag in self.conversationList:
            win = self.conversationList[mFlag]['win']
        else:
            win = ChatWin(conv.jid,str(self.core.jid))
            win._sendMsg2Friend.connect(self.sendMsg)
            win._closeSignal.connect(self.delWin)
            win.setCore(self.core)
            win.setChatInfor(mFlag)
            rootPath = getAvatarRootPath(str(self.core.jid))
            iconPath = os.path.join(rootPath,'{}.jpg'.format(str(conv.jid)))
            if os.path.exists(iconPath):
                print(iconPath)
                win.setWindowIcon(QIcon(iconPath))
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

    def insertMsg(self,userName, isSelf, chatWith, messageFrom , messageContext,createTime):
        try:
            query = QSqlQuery()
            sql = "insert into message(userName, isSelf, chatWith, messageFrom , messageContext,createTime) values('{}',{},'{}','{}','{}',{});".format(userName,
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
            # query.bindValue(userName)
            # query.bindValue(isSelf)
            # query.bindValue(chatWith)
            # query.bindValue(messageFrom)
            # query.bindValue(messageContext)
            # query.bindValue(createTime)
            if not query.exec_():
                print("插入出错")
                query.lastError()
            else:
                print("插入成功")
            query.clear()
            del query
        except Exception:
            return