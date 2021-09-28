import os
from uuid import uuid4


class Config:
    REREG_TIME = 360
    CHECK_TIME = 5
    TOKEN = '20210506_20_57_UnripeData'
    INNER_API = 'http://172.19.0.150:16000'
    WEB_URL = 'http://imw.unripedata.com'
    UID = str(uuid4())
    HOST = '0.0.0.0'
    WEB_PORT = 80
    TCP_PORT = 20000
    DEBUG = False
    TEST = False


class DevConfig(Config):
    INNER_API = 'http://127.0.0.1:5000'
    WEB_URL = 'http://localhost:8080'
    PORT = '9090'
    DEBUG = True


class TestConfig(Config):
    DEBUG = True
    TEST = True


config_by_name = {
    'dev': DevConfig,
    'test': TestConfig,
    'publish': Config
}

config = config_by_name[os.getenv('FLASK_ENV') or 'dev']()
