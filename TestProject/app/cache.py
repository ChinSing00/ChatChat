import aioxmpp
from aioxmpp import im, muc, structs, JID
from aioxmpp.im.p2p import Conversation

from PyQt5.QtCore import QPoint, pyqtSignal, QObject

import app
from app import Config
from utils import Log

globalPos = QPoint(0, 0)
item_icon = None
user_items = []

class ConversationHandller(QObject):
    _Sign_P2P = pyqtSignal(Conversation)
    _Sign_Muc = pyqtSignal(muc.service.Room)
    def __init__(self,parent=None):
        super(ConversationHandller,self).__init__(parent)
        self._ConversationList = {}

    async def setup(self,core):
        self.core = core
        self._client = core.client
        self.muc = self._client.summon(muc.Service)
        #监听会话接收
        self.muc_service = self._client.summon(im.ConversationService)
        self.muc_service.on_conversation_added.connect(self.recvConversation)
        self.p2p_service = self._client.summon(im.p2p.Service)
        self.p2p_service.on_conversation_new.connect(self.recvConversation)
    #ps:要注意保持会话或者房间对象的一致性，不一致会导致发送失败
    #送达会话分发
    def recvConversation(self,conv):
        jid = str(conv.jid)
        if jid not in self._ConversationList:
            self._ConversationList[jid] = conv
            Log.info("添加新会话", jid)

        if isinstance(self._ConversationList[jid],muc.service.Room):
            room = self._ConversationList[jid]
            self._Sign_Muc.emit(room)
        elif isinstance(self._ConversationList[jid],Conversation):
            pChat = self._ConversationList[jid]
            self._Sign_P2P.emit(pChat)


    #发起个人聊天
    def on_chatwith_friend(self,friend):
        jid = friend['jid']
        if jid not in self._ConversationList:
            conv = self.p2p_service.get_conversation(JID.fromstr(jid))
            self._ConversationList[jid] = conv
        self._Sign_P2P.emit( self._ConversationList[jid])

    #发起群聊聊天
    def on_chatwith_room(self,data):
        roomJID = '{}@{}'.format(data['roomName'],Config._mucService)
        Log.info("发起会话",roomJID)
        if roomJID not in self._ConversationList:
            #一定要有昵称才可以进入聊天室
            room,futrue = self.muc.join(JID.fromstr(roomJID),str(self.core.jid))
            self._ConversationList[roomJID] = room
            # self.sendMsg(roomJID,'666',room)
            # room.on_message.connect(self.on_message)
            # futrue.add_done_callback()
            # self._ConversationList[roomJID] = room

    # def on_message(self,message, member, source,**kwargs):
    #     print(str(message.body[structs.LanguageTag.fromstr('en')]),'\n')
    #
    # def sendMsg(self,jid,msg,room):
    #     msgData = aioxmpp.Message(
    #         to=JID.fromstr(jid),
    #         type_=aioxmpp.MessageType.GROUPCHAT,
    #     )
    #     msgData.body[None] = msg
    #     room.send_message(msgData)
