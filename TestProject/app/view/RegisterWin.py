from PyQt5 import QtWidgets
from ui import register
from app.view.Animation import OpenAnimation


class EDRegister(QtWidgets.QDialog,register.Ui_Dialog,OpenAnimation):
    def __init__(self,parent=None):
        super(EDRegister, self).__init__(parent)
        self.setupUi(self)
        self.setDuration(1000)  # 设置淡入淡出