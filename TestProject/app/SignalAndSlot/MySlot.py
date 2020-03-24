from PyQt5.QtCore import QObject

class RecvMsgFromWin(QObject):
    def __init__(self):
        super(RecvMsgFromWin, self).__init__()
        self.core = None
    def setCore(self,core):
        self.core = core

    def getLoginData( self,msg1,msg2):
        user = {}
        user['JID'] = msg1
        user['PWD'] = msg2
        self.core.start(user)
