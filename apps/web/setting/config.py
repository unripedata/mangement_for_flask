import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '202010418_UnripeData')
    HOST = '0.0.0.0'
    PORT = '80'
    INNER_API = 'http://172.19.0.150:16000'
    TEMPLATE = os.getcwd() + '/web/templates'
    STATIC = os.getcwd() + '/web/static'
    TEMPLATE_NAME = "/001"
    TCPSERVER_PORT = "9000"
    TOKEN = '20210506_20_57_UnripeData'
    CLIENT_TOKEN = 'test'
    DEBUG = False

class DevConfig(Config):
    INNER_API = 'http://127.0.0.1:5000'
    PORT = '8080'
    DEBUG = True

class TestConfig(Config):
    INNER_API = 'http://api.imw.unripedata.com'
    DEBUG = True
    TEST = True

config_by_name = {
    'dev': DevConfig,
    'test': TestConfig,
    'publish': Config
}

config = config_by_name[os.getenv('FLASK_ENV') or 'dev']()
