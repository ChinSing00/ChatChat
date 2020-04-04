import asyncio
import os
from functools import partial

from ofrestapi.exception import InvalidResponseException

import app
from app.view.MainWin import EDMianWin
from utils import Log,FileUtils
from aioxmpp import RosterClient, AvatarService, JID
from asyncio import sleep, ensure_future, create_task, get_event_loop
from ofrestapi import Users
from app import Config

class FriendsList():
    def __init__(self):
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
        self.mWin.show()
        self.core._sign_login.emit(1)#发射关闭登陆界面信号
        self.avatar_server = self._client.summon(AvatarService)#唤起头像服务
        await ensure_future(self.getInfo())
        await ensure_future(self._run())

    def initRoster(self):
        self.mWin.loadData(self.roster_server.groups)
        Log.info('加载好友列表：','start...')
        print(self.roster_server.groups)
        for group in self.roster_server.groups:
            for item in self.roster_server.groups[group]:
                Log.info("加载【{}】好友：".format(group),item.jid)

    def req_avatar_callback(self,friend,task):
        result = task.result()#result为 <AbstractAvatarDescriptor> 对象的列表集合
        if not result:
            self.save_avatar_callback(friend,task=None)
        else:
            save_task = ensure_future(result[0].get_image_bytes())  # get_image_bytes()为协程,result[0]为最新的图片
            save_task.add_done_callback(partial(self.save_avatar_callback, friend))


    def save_avatar_callback(self,friend,task):
        avatar_path = None
        if not task:
            pass
        else:
            bin_data = task.result()
            path_dir = os.path.join(app.BASE_DIR, 'avatar',self.core.jid.localpart)
            if not os.path.exists(path_dir):
                os.mkdir(path_dir)
            avatar_path  = os.path.join(path_dir,'{}.png'.format(friend['jid']))
            FileUtils.savaToPng(avatar_path,bin_data)
        friend['avatar_path'] = avatar_path
        self.mWin.loadData(friend)
    async def getInfo(self):
        tasks=[]
        friend_List = None
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
                task = get_event_loop().create_task(
                    self.avatar_server.get_avatar_metadata(JID.fromstr(friend['jid']), require_fresh=True,
                                                           disable_pep=False))
                task.add_done_callback(partial(self.req_avatar_callback, friend))
                tasks.append(task)
            await asyncio.gather(*tasks)
        except InvalidResponseException:
            Log.info("RestAPi","获取好友列表失败")
