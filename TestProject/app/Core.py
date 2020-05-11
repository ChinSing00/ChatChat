import asyncio
import aioxmpp
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject
from aiosasl import AuthenticationFailure, SASLError
from aioxmpp import JID

from app import cache, Config
from app.modules import Muc
from app.modules.Muc import MucChat
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
        flist , p2p , muc  = FriendsList(), Chat(),MucChat()

        handerller = cache.ConversationHandller()
        #接收好友、群组信息
        handerller._Sign_P2P.connect(p2p.on_chatwith)
        handerller._Sign_Muc.connect(muc.on_chatwith)
        p2p._Sign_Close_Conv.connect(handerller.on_ConvOrRoom_close)
        muc._Sign_Close_Conv.connect(handerller.on_ConvOrRoom_close)

        #发送好友、群组信息
        flist._chat2Friend_signal.connect(handerller.on_chatwith_friend)
        flist._chat2Room_signal.connect(handerller.on_chatwith_room)
        handerller._Notifiytion_Mian.connect(flist.mWin.loadHistoryChat)
        async with self.client.connected() as stream:
            Log.info("模块加载", "正在加载...")
            futures.append(asyncio.ensure_future(handerller.setup(self)))
            futures.append(asyncio.ensure_future(flist.setup(self)))
            futures.append(asyncio.ensure_future(p2p.setup(self)))
            futures.append(asyncio.ensure_future(muc.setup(self)))
            await asyncio.gather(*futures)#并发运行序列中的可等待对象
            Log.info("模块加载", "正在加载完成")

    def start(self, user):
        Log.info('开始登陆', user)
        self.jid = aioxmpp.JID.fromstr(user['JID'])
        self.password = user['PWD']
        try:
            # no_verify=True大坑！，注意关闭认证；参考：https://docs.zombofant.net/aioxmpp/devel/api/public/security_layer.html
            # 可能要自己定义security_layer以达到通信安全
            self.client = aioxmpp.PresenceManagedClient(self.jid,aioxmpp.make_security_layer(self.password, no_verify=True),loop=self._loop)
            self.client.set_presence(aioxmpp.PresenceState(available=True,show=aioxmpp.PresenceShow.FREE_FOR_CHAT),{aioxmpp.structs.LanguageTag.fromstr('en'):'在线'})
            self.client.on_failure.connect(self.on_failure)#启动失败时操作
            self.client.on_stream_established.connect(self.on_login_success)#在链接服务器时操作
            self.client.on_stream_suspended.connect(self.on_internet_disconnect)#服务器链接中断时操作
            self.client.on_stream_destroyed.connect(self.on_internet_disconnect)#服务器链接失败时操作
        except ConnectionRefusedError:
            self._sign_login.emit(3)
            return
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
        QtWidgets.QMessageBox.question(QtWidgets.QWidget(), '网络连接错误', '请重新登陆！')

