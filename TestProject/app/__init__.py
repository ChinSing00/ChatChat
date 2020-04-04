import sys,os
sys.path.append("..")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class Config():
    _host = '192.168.123.230'
    _restPort = '9090'
    _restPort_secret = 'dyMW0FcWB3GH9Rmo'