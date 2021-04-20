import asyncio
import os

from PyQt5 import QtSql
from PyQt5.QtCore import pyqtSignal, QObject, QStringListModel, QSize
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QListWidgetItem
from ofrestapi.exception import InvalidResponseException

import app
import utils
from app.view import RoomItem
from app.view.MainWin import EDMianWin
from utils import Log,FileUtils
from aioxmpp import AvatarService, JID, RosterClient
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
        self.mWin.setCore(core)
        self.mWin.user_nane.setText(core.jid.localpart)
        self.mWin._chat2Friend_signal.connect(self.chat2Friend)
        self.mWin._chat2Room_signal.connect(self.chat2Room)
        self.mWin.show()
        self.core._sign_login.emit(1)#发射关闭登陆界面信号
        self.avatar_server = self._client.summon(AvatarService)#唤起头像服务
        self.roster = self._client.summon(RosterClient)
        # roster.on_subscribe.connect(self.A1)
        # roster.on_subscribed.connect(self.A2)
        # roster.subscribe(JID.fromstr("qq2255@{}".format(Config._host)))
        await ensure_future(self.getFriendList())
        await ensure_future(self.getRoomList())
        await ensure_future(self.getHistoryChatList())
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
            metadata = await self.avatar_server.get_avatar_metadata(self.core.jid)
            if metadata:
                picture = await asyncio.ensure_future(metadata[0].get_image_bytes())
                picPath = os.path.join(app.getAvatarRootPath(self.core.jid.localpart),'{}.jpg'.format(str(self.core.jid)))
                if not os.path.exists(picPath):
                    FileUtils.savaToPng(picPath, picture)
            usericon = QPixmap.fromImage(QImage(picPath)) if os.path.exists(picPath) else QPixmap(":src\images\CustomerService.png")
            self.mWin.avatar.setBaseSize(QSize(40,40))
            temp = utils.PixmapToRound(self.mWin.avatar, usericon)
            self.mWin.avatar.setScaledContents(True)
            self.mWin.avatar.setPixmap(temp)

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
        self.initDatabase()
        query = QSqlQuery()
        sql = "select * from message where isSelf!=1 and userName='{}' GROUP BY chatWith;".format(str(self.core.jid).replace(("/"+str(self.core.jid.resource)),''))
        query.prepare(sql)
        query.exec_()
        while query.next():
            userName, isSelf, chatWith, messageFrom, messageContext, createTime = query.value(0), query.value(
                1), query.value(2), query.value(3), query.value(4), query.value(5)
            data = {'entity_jid':chatWith,"time":createTime}
            self.mWin.loadHistoryChat(data)

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

    def initDatabase(self):
        self.database = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.database.setDatabaseName('data.db')
        self.database.open()
        query = QSqlQuery()
        query.prepare("create table if not exists message(userName varchar(64), isSelf int, chatWith varchar(64), messageFrom varchar(64), messageContext text,createTime TIMESTAMP default (datetime('now', 'localtime')));")
        if not query.exec_():
            query.lastError()
            Log.info('读取message表失败', 'Error')
        else:
            Log.info('读取message', 'Seccsess')
        del query