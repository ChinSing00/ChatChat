import asyncio
import aioxmpp
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from aiosasl import AuthenticationFailure, SASLError

from utils import Log
from app.modules.P2P import Chat
from app.modules.Main import FriendsList

class core(QObject):
    _sign_login = pyqtSignal(int)
    def __init__(self,loop, parent=None):
        super(core, self).__init__(parent)
        self.jid = ""
        self.password = ""
        self._loop = loop


    async def run(self):
        futures = []
        Log.info("模块加载", "正在加载...")
        flist = FriendsList()
        chat = Chat()
        flist._chat2Friend_signal.connect(chat._recvChat_Signal.emit)

        async with self.client.connected() as stream:
            futures.append(asyncio.ensure_future(flist.setup(self)))
            futures.append(asyncio.ensure_future(chat.setup(self)))
            await asyncio.gather(*futures)#并发运行序列中的可等待对象


    def start(self, user):
        Log.info('开始登陆', user)
        self.jid = aioxmpp.JID.fromstr(user['JID'])
        self.password = user['PWD']
        try:
            # no_verify=True大坑！，注意关闭认证；参考：https://docs.zombofant.net/aioxmpp/devel/api/public/security_layer.html
            # 在实际程序中可能要自己定义security_layer以达到通信安全
            self.client = aioxmpp.PresenceManagedClient(self.jid,aioxmpp.make_security_layer(self.password, no_verify=True),loop=self._loop)
            self.client.set_presence(aioxmpp.PresenceState(available=True,show=aioxmpp.PresenceShow.FREE_FOR_CHAT),{aioxmpp.structs.LanguageTag.fromstr('en'):'在线'})
            self.client.on_failure.connect(self.on_failure)#启动失败时操作
            self.client.on_stream_established.connect(self.on_login_success)#在链接服务器时操作
            self.client.on_stream_suspended.connect(self.on_internet_disconnect)#服务器链接中断时操作
            self.client.on_stream_destroyed.connect(self.on_internet_disconnect)#服务器链接失败时操作
        except Exception:
            return

    def on_failure(self,err):
        if isinstance(err,AuthenticationFailure):
            self._sign_login.emit(0)
        if isinstance(err,SASLError):
            self._sign_login.emit(3)
        Log.info("错误",type(err))

    def on_login_success(self):
        asyncio.ensure_future(self.run(), loop=self._loop)  # 加入主循环
        Log.info("登陆成功", 'nice')

    def on_internet_disconnect(self,reason):
        Log.info("网络错误", reason)

