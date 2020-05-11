import asyncio
import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize,Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QWidget, QLabel, QListWidgetItem
from aioxmpp import AvatarService, JID
from ofrestapi import Muc

import app
import ui
import utils
from app import Config
from app.view.MucWidgetItem import MucWidItem
from ui.MucWidget import Ui_Form
from utils import FileUtils, Log
from ui import MucWidg_Item

class CMIWidget(QWidget,Ui_Form):
    def __init__(self,jid,core,parent=None):
        super(CMIWidget, self).__init__(parent)
        self.setupUi(self)
        self.room_jid = jid
        self.core = core
        self._client = core.client
        self._muc_avatarService = self._client.summon(AvatarService)
        self.init()


    def init(self):
        nameFilter = '@{}'.format(Config._mucService)
        roomName = self.room_jid.replace(nameFilter,'')
        room = Muc('http://{}:{}'.format(Config._host, Config._restPort), Config._restPort_secret)
        roomInfo = room.get_room(roomName)
        members = []
        members.extend(roomInfo['members'])
        members.extend(roomInfo['owners'])
        members.extend(roomInfo['admins'])
        asyncio.ensure_future(self.getMembersAvatar(members))
        self.count.setText('{}/{}'.format(len(members),roomInfo['maxUsers']))
        mlist = str(roomInfo['admins']) if roomInfo['admins'] else None
        if mlist:
            self.admin.setText(mlist.replace('@{}'.format(Config._host),''))
        else:
            self.admin.setText("暂无")


    async def getMembersAvatar(self,memberList):
        rootPath = os.path.join(app.getAvatarRootPath(self.core.jid.localpart), self.room_jid)
        if not os.path.exists(rootPath) :
            os.mkdir(rootPath)
        self.room_path = rootPath
        for member in  memberList:
            metadata = await asyncio.ensure_future(self._muc_avatarService.get_avatar_metadata(JID.fromstr(member)))
            if metadata:
                picture = await asyncio.ensure_future(metadata[0].get_image_bytes())
                picPath = os.path.join(rootPath,'{}.jpg'.format(member))
                FileUtils.savaToPng(picPath, picture)
        self.loadMember(memberList)
    def loadMember(self,members):
        print(members)
        for member in members:
            item = QListWidgetItem()
            item.setSizeHint(QSize(174,40))
            self.listWidget.addItem(item)
            userhead  = os.path.join(self.room_path,'{}.jpg'.format(member))
            usericon = QPixmap.fromImage(QImage(userhead)) if os.path.exists(userhead) else QPixmap(":src\images\CustomerService.png")
            widget = MucWidItem(usericon,member.replace("@{}".format(Config._host),''))
            self.listWidget.setItemWidget(item,widget)
