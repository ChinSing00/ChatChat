import asyncio
from functools import partial

import aioxmpp
from PyQt5.QtCore import pyqtSignal, QObject
from aioxmpp import JID, MUCClient

import app
from utils import Log, TimeUtils
from app.view.ChatWith import ChatWin

class MucChat(QObject):

    def __init__(self):
        super(MucChat, self).__init__()
        self._client = None
        self.roomList = {}

    async def setup(self,core):
        self.core = core
        self._client = core.client
        await asyncio.ensure_future(self._run())

    async def _run(self):
        while True:
           await asyncio.sleep(1)

    def on_chatwith(self,room):
        jid = str(room.jid)
        if jid not in self.roomList:
            win = self.getWin(room)
            self.roomList[jid]['room'].on_message(partial(self.on_message,self.roomList[jid]['room']))
        self.roomList[jid]['win'].show()
        # win.show()

    def delWin(self,room_jid):
        #窗口关闭，离开会话  ps：leave()是个协程，需要将其加入并发队列
        asyncio.ensure_future(self.roomList[str(room_jid)]['room'].leave())
        del self.roomList[str(room_jid)]

    def getWin(self,room):
        mFlag = str(room.jid)
        if mFlag in self.roomList:
            win = self.roomList[mFlag]['win']
        else:
            win = ChatWin(room.jid)
            win._sendMsg2Friend.connect(self.sendMsg)
            win._closeSignal.connect(self.delWin)
            data = {}
            data['win'] = win
            data['room'] = room
            self.roomList[mFlag] = data
        return win

    def on_message(self,room,message, member, source,**kwargs):
        jid = str(member.conversation_jid)
        win = self.roomList[jid]['win']
        if aioxmpp.structs.LanguageTag.fromstr('en') in message.body:
            win.chatWin.append('({}){}:\n{}'.format(TimeUtils.getTimeWithoutDay(),jid,str(message.body[aioxmpp.structs.LanguageTag.fromstr('en')])))

    def sendMsg(self,data):
        msgData = aioxmpp.Message(
            to=data['JID'],  # recipient_jid must be an aioxmpp.JID
            type_=aioxmpp.MessageType.GROUPCHAT,
        )
        msgData.body[None] = data['msg']
        self.roomList[str(data['JID'])]['room'].send_message(msgData)

    def on_join(self,jid,member, **kwargs):
        self.roomList[jid]['win'].chatWin.append("<a style='{color:red}'>---------------------------欢迎【{}】进入房间--------------------------------</a>".format(str(member.conversation_jid)))
