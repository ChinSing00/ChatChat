from PyQt5.QtCore import QPoint, pyqtSignal
import app
globalPos = QPoint(0, 0)
item_icon = None
user_items = []

@app.Singleton
class ConversationHandller():
    _Sign_P2P = pyqtSignal(dict)
    def __int__(self):
        self._ConversationList = {}

    # def addConversation(self):
        

