import sys,os
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def getAvatarRootPath(localpart):

    path_dir = os.path.join(BASE_DIR, 'avatar',localpart)
    if not os.path.exists(path_dir):
        os.mkdir(path_dir)
    return  path_dir

class Config():
    _host = '192.168.123.230'
    _restPort = '9090'
    _restPort_secret = 'dyMW0FcWB3GH9Rmo'
    _resourceName = 'simple'
    _mucService = 'conference.'+_host

class AppContext():
    pass


def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton