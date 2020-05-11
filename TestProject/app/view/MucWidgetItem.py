from PyQt5.QtWidgets import QWidget

import utils
from ui import MucWidg_Item


class MucWidItem( QWidget,MucWidg_Item.Ui_Form):
    def __init__(self,usericon,name, parent=None):
        super(MucWidItem, self).__init__(parent)
        self.setupUi(self)
        temp = utils.PixmapToRound(self.icon, usericon)
        self.icon.setScaledContents(True)
        self.icon.setPixmap(temp)
        self.name.setText(name)