
class BaseEntity(object):
    def __init__(self,jid):
        self.JID = jid



class User(BaseEntity):
    def __init__(self,JID,PWD):
        super(User,self).__init__(JID)
        self.PWD = PWD
