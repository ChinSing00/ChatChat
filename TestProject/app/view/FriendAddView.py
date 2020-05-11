from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog

from ui.addFriend import Ui_addFriend


class AddFirendWin(QDialog,Ui_addFriend):
    _Sign_Mian = pyqtSignal(str)
    def __init__(self,parent=None):
        super(AddFirendWin, self).__init__(parent)
        self.setupUi(self)
