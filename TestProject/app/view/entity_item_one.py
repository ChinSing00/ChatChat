from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QTreeWidgetItem

from app import cache
from app.view.ui_item import Ui_Item
from ui import ui_item

class Child_Item(QWidget, Ui_Item):

    def __init__(self, parent = None, userhead = "", name = "", mood = "", times = "", which = 0):
        # print(type(parent))
        super(Child_Item, self).__init__(parent)
        self.data = None
        self.setupUi(self, userhead, name, mood, times, which)


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
        childWidget = Child_Item(None, user['avatar_path'], (user['nickname'] if 'nickname' in user and user['nickname'] else user['jid'] ), mood="", times='', which = 0)
        childWidget.data =  user
        self.treeWidget().setItemWidget(childItem, 0, childWidget)

