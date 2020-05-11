from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel

from app.view.RegisterWin import EDRegister


class MyLabel(QLabel):
    Click = pyqtSignal()
    is_show = True

    def __init__(self,parent):
        super(MyLabel,self).__init__(parent)
        print('666666666666')
        self.Click.connect(self.openRegWin)

    #用户注册Label点击处理
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.Click.emit()

    def openRegWin(self):
        print("99999")
        if self.is_show:
            self.is_show = False
            reg = EDRegister()
            reg.show()