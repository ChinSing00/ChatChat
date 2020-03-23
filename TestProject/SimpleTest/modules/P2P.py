import asyncio
import aioxmpp
from utils import Log
from SimpleTest.view.PersonalChat import PersonalChatWin

class Chat():

    def __init__(self):
        self._client = None
        self.chatList = {}

    async def setup(self,core):
        self._client = core.client
        Log.info("单人聊天模块", "已加载")
        # 接收消息
        mDispatcher = self._client.summon(aioxmpp.dispatcher.SimpleMessageDispatcher)  # 生成消息调度器
        mDispatcher.register_callback(aioxmpp.MessageType.CHAT, None, self.message_receiver)  # 注册消息回调
        server = self._client.summon(aioxmpp.im.p2p.Service)
        server.on_conversation_new.connect(self.on_conversation_new)
        await asyncio.ensure_future(self._run())

    async def _run(self):
        while True:
           await asyncio.sleep(1)

    def message_receiver(self,msg):
        pass

    async def message_sender(self,s):
        Log.info("信息发送",str(s))
        msg = aioxmpp.Message(to=aioxmpp.JID.fromstr(s['JID']),type_=aioxmpp.MessageType.CHAT)
        msg.body = s['msg']
        await self._client.send(msg)

    def on_conversation_new(self,conversation):
        print(conversation)
        conversation.on_message.connect(self.oott)
        conversation


    def oott(self, message, member, source, **kwargs):
        #print(member.direct_jid.bare())
        if member in self.chatList:
            win = self.chatList[member]
            win.chatWin.append(str(message.body[aioxmpp.structs.LanguageTag.fromstr('en')]))
        else:
            win = PersonalChatWin(member)
            win.setWindowTitle(str(member.direct_jid))
            #win._sendMsg2Core.connect()
            win._closeSignal.connect(self.delWin)
            win.chatWin.append(str(message.body[aioxmpp.structs.LanguageTag.fromstr('en')]))
            self.chatList[member] = win
            win.show()

    def delWin(self,member):
        del self.chatList[member]

