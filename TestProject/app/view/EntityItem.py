from PyQt5.QtGui import QPixmap

from ui import entity_item
from PyQt5.QtWidgets import QWidget

class EItem(QWidget,entity_item.Ui_Form):
    def __init__(self, parent=None):
        super(EItem, self).__init__(parent)
        self.setupUi(self)
        self.initWin()

    def initWin(self):
        pass
    def setData(self,data):
        self.user_icon.setPixmap(QPixmap(":/src/icon/icon/用户.svg"))
        self.user_name.setText(str(data.jid))