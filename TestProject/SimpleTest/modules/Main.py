from SimpleTest.view.MainWin import EDMianWin
from utils import Log
from aioxmpp import RosterClient, AvatarService
from asyncio import sleep,ensure_future


class FriendsList():
    def __init__(self):
        self._client = None
        self.server = None
        self.mWin = EDMianWin()

    async def _run(self):
        while True:
           await sleep(1)

    async def setup(self,core):
        self._client = core.client
        self.core = core
        self.mWin.show()
        self.core._sign_login.emit(1)#发射关闭登陆界面信号
        self.roster_server = self._client.summon(RosterClient)
        self.avatar_server = self._client.summon(AvatarService)
        self.roster_server.on_initial_roster_received.connect(self.initRoster)
        self.avatar_set = self.avatar_server.get_avatar_metadata(self.core.jid)
        #Log.info("用户头像",[i for i in self.avatar_set])
        map(lambda x:Log.info("用户头像",x),self.avatar_set)
        Log.info("主程序模块","已加载")
        await ensure_future(self._run())

    def initRoster(self):

        self.mWin.loadData(self.roster_server.groups)
        Log.info('加载好友列表：','start...')
        print(self.roster_server.groups)
        for group in self.roster_server.groups:
            for item in self.roster_server.groups[group]:
                Log.info("加载【{}】好友：".format(group),item.jid)