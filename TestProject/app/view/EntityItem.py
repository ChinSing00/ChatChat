from PyQt5.QtGui import QPixmap, QIcon

from ui import entity_item
from PyQt5.QtWidgets import QWidget

from utils import Log


class EItem(QWidget,entity_item.Ui_Form):
    def __init__(self, parent=None):
        super(EItem, self).__init__(parent)
        self.setupUi(self)
        self.initWin()

    def initWin(self):
        pass
    def setData(self,data):
        Log.info('EItem',data)
        if not data['avatar_path']:
            self.user_icon.setIcon(QIcon('src/images/CustomerService.png'))
        else:
            self.user_icon.setIcon(QIcon(data['avatar_path']))
        if 'nickname' not in data or not data['nickname']:
            self.user_name.setText(str(data['jid']))
        else:
            self.user_name.setText(str(data['nickname']))
