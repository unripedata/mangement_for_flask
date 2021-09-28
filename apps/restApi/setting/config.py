import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '20210418_UnripeData')
    TOKEN = '20210506_20_57_UnripeData'
    HOST = '0.0.0.0'
    PORT = '80'
    DEBUG = False
    DUPLICATE_LOGIN = False

    MARIA_USER = "root"
    MARIA_PWD = "2310"
    MARIA_HOST = "172.19.0.101"
    MARIA_PORT = 3306
    MARIA_DB = "imw_web"

    REDIS_PWD = "2310"
    REDIS_HOST = "172.19.0.102"
    REDIS_PORT = 9001


class DevConfig(Config):
    MARIA_HOST = "db.unripedata.com"
    MARIA_PORT = 10001

    REDIS_HOST = "db.unripedata.com"

    PORT = '5000'
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
