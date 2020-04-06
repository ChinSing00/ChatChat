import asyncio
from functools import partial

import aioxmpp
from PyQt5.QtCore import pyqtSignal, QObject
from aioxmpp import JID
from aioxmpp.im.p2p import Conversation, Member

from utils import Log, TimeUtils
from app.view.PersonalChat import PersonalChatWin

class Chat(QObject):
    _recvChat_Signal = pyqtSignal(dict)

    def __init__(self):
        super(Chat, self).__init__()
        self._client = None
        self.conversationList = {}

    async def setup(self,core):
        self.core = core
        self._client = core.client
        Log.info("单人聊天模块", "已加载")
        #P2P单聊消息
        self.p2p_server = self._client.summon(aioxmpp.im.p2p.Service)
        self.p2p_server.on_conversation_new.connect(self.on_conversation_new)
        self._recvChat_Signal.connect(self.getChat)
        await asyncio.ensure_future(self._run())

    async def _run(self):
        while True:
           await asyncio.sleep(1)

    def on_conversation_new(self,conversation):
        conversation.on_message.connect(partial(self.on_message,conversation))

    def on_message(self,conversation ,message, member, source,**kwargs):
        '''
        :param conversation
        :param message 接收到的消息 <aioxmpp.Message>
        :param member 发送消息成员 <aioxmpp.im.conversation.AbstractConversationMember>
        :param
        '''
        if member == conversation.me:
            return
        mFlag = str(member.conversation_jid)
        if mFlag in self.conversationList:
            win = self.conversationList[mFlag]['win']
        else:
            win = PersonalChatWin(member.conversation_jid)
            win._sendMsg2Friend.connect(self.sendMsg)
            win._closeSignal.connect(self.delWin)
            data = {}
            data['win'] = win
            data['conversation'] = conversation
            self.conversationList[mFlag] = data
            win.show()
        if aioxmpp.structs.LanguageTag.fromstr('en') in message.body:
            win.chatWin.append('({}){}:\n{}'.format(TimeUtils.getTimeWithoutDay(),mFlag,str(message.body[aioxmpp.structs.LanguageTag.fromstr('en')])))

    def delWin(self,friend_jid):
        del self.conversationList[str(friend_jid)]

    def sendMsg(self,data):
        msg = aioxmpp.Message(
            to=data['JID'],  # recipient_jid must be an aioxmpp.JID
            type_=aioxmpp.MessageType.CHAT,
        )
        msg.body[None] = data['msg']
        Log.info('发送信息至[{}]'.format(str(data['JID'])),data)
        self.conversationList[str(data['JID'])]['conversation'].send_message(msg)

    def getChat(self,friend):
        if friend['jid'] in self.conversationList:
            win = self.conversationList[friend['jid']]['win']
        else:
            win = PersonalChatWin(JID.fromstr(friend['jid']))
            win._sendMsg2Friend.connect(self.sendMsg)
            win._closeSignal.connect(self.delWin)
            data = {}
            data['win'] = win
            conversation = Conversation(self.p2p_server,JID.fromstr(friend['jid']))
            conversation.on_message.connect(partial(self.on_message,conversation))
            data['conversation'] = conversation
            self.conversationList[friend['jid']] = data
        win.show()
