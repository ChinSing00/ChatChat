import asyncio
import os
from functools import partial

from PyQt5.QtCore import pyqtSignal, QObject
from ofrestapi.exception import InvalidResponseException

import app
from app.view.MainWin import EDMianWin
from utils import Log,FileUtils
from aioxmpp import RosterClient, AvatarService, JID
from asyncio import sleep, ensure_future, create_task, get_event_loop
from ofrestapi import Users
from app import Config

class FriendsList(QObject):
    _chat2Friend_signal = pyqtSignal(dict)
    def __init__(self):
        super(FriendsList, self).__init__()
        self._client = None
        self.mWin = EDMianWin()
        self._queue =asyncio.Queue(maxsize=5)

    async def _run(self):
        Log.info("主程序模块","已加载")
        while True:
            await sleep(1)

    async def setup(self,core):
        self.core = core
        self._client = core.client
        self.mWin.user_nane.setText(core.jid.localpart)
        self.mWin._chat2Friend_signal.connect(self.chat2Friend)
        self.mWin.show()
        self.core._sign_login.emit(1)#发射关闭登陆界面信号
        self.avatar_server = self._client.summon(AvatarService)#唤起头像服务
        await ensure_future(self.getInfo())
        await ensure_future(self._run())

    def chat2Friend(self,data):
        self._chat2Friend_signal.emit(data)

    async def req_avatar(self,friend,task):
        avatar_path = None
        if not task:
            pass
        else:
            bin_data = await ensure_future(task[0].get_image_bytes())  # get_image_bytes()为协程,result[0]为最新的图片
            avatar_path = os.path.join(app.getAvatarRootPath( self.core.jid.localpart), '{}.jpg'.format(friend['jid']))
            FileUtils.savaToPng(avatar_path, bin_data)
        friend['avatar_path'] = avatar_path
        self.mWin.loadData(friend)

    def save_avatar_callback(self,friend,task):
        if not task:
            pass
        else:
            bin_data = task.result()


    async def getInfo(self):
        _user = Users('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)
        try:
            '''
            friendList的数据格式：
            {'rosterItem': [{'jid': 'chinsing00@192.168.123.230', 'nickname': 'chinsing00', 'subscriptionType': 3, 'groups': ['Friends']},{...}]}
            '''
            friend_List = _user.get_user_roster(self.core.jid.localpart)#只需要用户名就行，不需要加域名
            del _user #清除user，避免服务器生成过多的连接导致服务器连接池溢出
            print(friend_List)
            for friend in friend_List['rosterItem']:
                # task执行后返回 <AbstractAvatarDescriptor> 对象
                task = await get_event_loop().create_task(
                    self.avatar_server.get_avatar_metadata(JID.fromstr(friend['jid']), require_fresh=True,
                                                           disable_pep=False))
                await ensure_future(self.req_avatar(friend,task))
        except InvalidResponseException:
            Log.info("RestAPi","获取好友列表失败")
