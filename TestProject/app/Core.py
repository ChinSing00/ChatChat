import asyncio
import aioxmpp
from PyQt5.QtCore import pyqtSignal, QObject
from utils import Log


class core(QObject):
    _sign_login = pyqtSignal(int)
    def __init__(self,loop, parent=None):
        super(core, self).__init__(parent)
        self.jid = ""
        self.password = ""
        self._loop = loop


    async def run(self):
        from app.modules.P2P import Chat
        from app.modules.Main import FriendsList
        futures = []
        Log.info("模块加载", "正在加载...")
        futures.append(asyncio.ensure_future(FriendsList().setup(self)))
        futures.append(asyncio.ensure_future(Chat().setup(self)))
        async with self.client.connected() as stream:
            await asyncio.gather(*futures)#并发运行序列中的可等待对象
            #Log.info("模块加载", "加载完成")

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
            asyncio.ensure_future(self.run(), loop=self._loop)  # 加入主循环
        except Exception:
            self._sign_login.emit(0)
            print(Exception)
            return

    def on_failure(self,err):
        #self._sign_login.emit(0)
        Log.info("错误",err)

    def on_login_success(self):
        #asyncio.ensure_future(self.run(), loop=self._loop)  # 加入主循环
        Log.info("登陆成功", 'nice')

    def on_internet_disconnect(self,reason):
        Log.info("网络错误", reason)

