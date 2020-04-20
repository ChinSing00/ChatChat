from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel

from app.view.RegisterWin import EDRegister


class MyLabel(QLabel):
    Click = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.Click.emit()
    def openRegWin(self):
        reg = EDRegister()
        reg.show()