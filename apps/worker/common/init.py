from uuid import uuid4

class Init():
    # web 주소
    _initPath = "http://shiptroll.com"
    # TCPServerApi 주소
    _commandPath = "http://cmd.shiptroll.com"

    # TCPSever 주소
    _host = 'www.shiptroll.com'
    _port = 20000

    @classmethod
    def getInitPath(cls):
        return cls._initPath

    @classmethod
    def getCommandPath(cls):
        return cls._commandPath

    @classmethod
    def getHost(cls):
        return cls._host

    @classmethod
    def getPort(cls):
        return cls._port
