from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPainterPath
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

import utils
from app import cache
from ui.ui_item import Ui_Form
from ui import ui_item

class Child_Item(QWidget, Ui_Form):

    def __init__(self, parent = None,user='',time=''):
        # print(type(parent))
        subscriptionType = ['']
        super(Child_Item, self).__init__(parent)
        self.data = user
        self.setupUi(self)
        userhead = user['avatar_path']
        name = (user['nickname'] if 'nickname' in user and user['nickname'] else user['jid'])
        usericon = QPixmap.fromImage(QImage(userhead)) if userhead else QPixmap(":src\images\CustomerService.png")
        # usericon = QImage(userhead) if userhead else QImage(":src\images\CustomerService.png")
        # pic = utils.render_avatar_image(usericon,1)
        temp = utils.PixmapToRound(self.userLabel,usericon)
        self.userLabel.setScaledContents(True)
        self.userLabel.setPixmap(temp)
        self.nameLabel.setText( name)
        self.timeLabel.setText( time if time else '')

    @property
    def getData(self):
        return self.data

    @getData.setter
    def setData(self, data):
        self.data = data

class User_Item(QTreeWidgetItem):

    def __init__(self, parent = None, text = "", which = 0):
        QTreeWidgetItem.__init__(self, parent)
        self.setSizeHint(0, QSize(280, 30))    # 设置Item大小
        self.setTitle(text)    # 设置该Item的文字
        self.setIcon(0, cache.item_icon)
        self.which = which

    def setTitle(self, text = ""):
        self.setText(0, text)

    def setUsers(self, user = None):
        childItem = QTreeWidgetItem(self)
        childWidget = Child_Item(None,user)
        childWidget.data =  user
        self.treeWidget().setItemWidget(childItem, 0, childWidget)

