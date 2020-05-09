import asyncio
import os

from PyQt5.QtCore import pyqtSignal, QObject, QStringListModel
from PyQt5.QtWidgets import QListWidgetItem
from ofrestapi.exception import InvalidResponseException

import app
from app.view import RoomItem
from app.view.MainWin import EDMianWin
from utils import Log,FileUtils
from aioxmpp import AvatarService, JID
from asyncio import sleep, ensure_future, get_event_loop
from ofrestapi import Users, Muc
from app import Config

class FriendsList(QObject):
    _chat2Friend_signal = pyqtSignal(dict)
    _chat2Room_signal = pyqtSignal(dict)
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
        self.mWin._chat2Room_signal.connect(self.chat2Room)
        self.mWin.show()
        self.core._sign_login.emit(1)#发射关闭登陆界面信号
        self.avatar_server = self._client.summon(AvatarService)#唤起头像服务
        await ensure_future(self.getFriendList())
        await ensure_future(self.getHistoryChatList())
        await ensure_future(self.getRoomList())
        await ensure_future(self._run())

    def chat2Friend(self,data):
        self._chat2Friend_signal.emit(data)

    def chat2Room(self,data):
        self._chat2Room_signal.emit(data)


    async def getFriendList(self):
        _user = Users('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)
        try:
            '''
            friendList的数据格式：
            {'rosterItem': [{'jid': 'chinsing00@192.168.123.230', 'nickname': 'chinsing00', 'subscriptionType': 3, 'groups': ['Friends']},{...}]}
            '''
            friend_List = _user.get_user_roster(self.core.jid.localpart)#只需要用户名就行，不需要加域名
            del _user #清除user，避免服务器生成过多的连接导致服务器连接池溢出
            for friend in friend_List['rosterItem']:
                # task执行后返回 <AbstractAvatarDescriptor> 对象
                task = await get_event_loop().create_task(
                    self.avatar_server.get_avatar_metadata(JID.fromstr(friend['jid']), require_fresh=True,
                                                           disable_pep=False))
                #得到<AbstractAvatarDescriptor> 对象后进行头像保存本地及加载好友列表
                avatar_path = None
                if task:
                    bin_data = await ensure_future(task[0].get_image_bytes())  # get_image_bytes()为协程,result[0]为最新的图片
                    avatar_path = os.path.join(app.getAvatarRootPath(self.core.jid.localpart),
                                               '{}.jpg'.format(friend['jid']))
                    FileUtils.savaToPng(avatar_path, bin_data)
                friend['avatar_path'] = avatar_path
                self.mWin.loadData(friend)
        except InvalidResponseException:
            Log.info("RestAPi","获取好友列表失败")

    async def getHistoryChatList(self):
        pass

    '''数据格式：{'chatRooms': [{'roomName': 'test22', 'naturalName': '王企鹅', 'description': '用于群聊测试', 'subject': 'BBS', 'creationDate': 1587396444462, 'modificationDate': 1587396444479, 'maxUse
                   rs': 30, 'persistent': True, 'publicRoom': True, 'registrationEnabled': True, 'canAnyoneDiscoverJID': True, 'canOccupantsChangeSubject': True, 'canOccupantsInvite': True, 'canChangeNick
                   name': True, 'logEnabled': True, 'loginRestrictedToNickname': True, 'membersOnly': False, 'moderated': True, 'broadcastPresenceRoles': ['moderator', 'participant', 'visitor'], 'owners':
                    ['admin@192.168.123.230', 'chinsing00@192.168.123.230'], 'admins': [], 'members': ['user@192.168.123.230'], 'outcasts': [], 'ownerGroups': [], 'adminGroups': [], 'memberGroups': [], 'o
                   utcastGroups': []}]}
               '''
    async def getRoomList(self):
        try:
            roomList = None
            room = Muc('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)
            roomList = room.get_rooms()
            for room in roomList['chatRooms']:
                self.mWin.loadRoom(room)
        except Exception:
            pass
