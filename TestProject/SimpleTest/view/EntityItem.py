from ui import entity_item
from PyQt5.QtWidgets import QWidget

class EItem(QWidget,entity_item.Ui_Form):
    def __init__(self, parent=None):
        super(EItem, self).__init__(parent)
        self.setupUi(self)