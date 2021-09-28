import os
from uuid import uuid4


class Config:
    TCP_PORT = 20000
    TCP_HOST = '125.180.129.217'
    WEB = '127.0.0.1'
    CHECK_TIME = 5

class DevConfig(Config):
    TCP_PORT = 20000
    TCP_HOST = '192.168.123.108'
    WEB = 'http://localhost:8080'


class TestConfig(Config):
    DEBUG = True
    TEST = True


config_by_name = {
    'dev': DevConfig,
    'test': TestConfig,
    'publish': Config
}

config = config_by_name[os.getenv('FLASK_ENV') or 'dev']()
