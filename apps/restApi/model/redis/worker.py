#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
from common.db.redisDB import RedisDB


class Server(RedisDB):
    _instance = None
    _dbConn = None
    _prefixServer = 'imw:worker:server:'
    _prefixClient = 'imw:worker:client:'
    _timeout = 7200

    def regist(cls, ip, uid):
        result = True
        cls.connect()
        for key in cls._dbConn.keys(cls._prefixServer + '*'):
            if cls._dbConn.get(key) == uid:
                cls.delete(key)
        cls._dbConn.setex(cls._prefixServer + ip, cls._timeout, uid)
        return result

    def delete(cls, ip):
        result = True
        for key in cls._dbConn.keys(cls._prefixClient + ip + ':' + '*'):
            cls._dbConn.delete(key)
        cls._dbConn.delete(cls._prefixServer + ip)
        return result

    def check(cls, ip, uid):
        result = False
        cls.connect()
        serverUid = cls._dbConn.get(cls._prefixServer + ip)
        if serverUid is not None:
            if serverUid == uid:
                cls._dbConn.expire(cls._prefixServer + ip, cls._timeout)
                result = True
            else:
                result = cls.regist(ip, uid)
        else:
            result = cls.regist(ip, uid)

        return result

    def list(cls):
        result = []
        cls.connect()
        for key in cls._dbConn.keys(cls._prefixServer + '*'):
            result.append(key.replace(cls._prefixServer, ""))
        return result

    def uid(cls, ip):
        cls.connect()
        uid = cls._dbConn.get(cls._prefixServer + ip)
        if uid is None:
            uid = ''
        return uid


class Client(RedisDB):
    _instance = None
    _dbConn = None
    _prefixServer = 'imw:worker:server:'
    _prefixClient = 'imw:worker:client:'
    _timeout = 7200

    def regist(cls, serverIp, clientIp):
        result = {}
        cls.connect()
        if cls._prefixServer + serverIp in cls._dbConn.keys(cls._prefixServer + '*'):
            if cls._prefixClient + clientIp in cls._dbConn.keys(cls._prefixClient + '*'):
                cls._dbConn.delete(serverIp, clientIp)
            cls._dbConn.setex(cls._prefixServer + serverIp + ':' + clientIp, cls._timeout, serverUid)

    def delete(cls, serverIp, clientIp):
        result = True
        cls._dbConn.delete(cls._prefixServer + serverIp + ':' + clientIp)
        return result

    def list(cls):
        result = {}
        cls.connect()
        for serverKey in cls._dbConn.keys(cls._prefixServer + '*'):
            serverIp = serverKey.replace(cls._prefixServer, '')
            result[serverIp] = []
            for clientKey in cls._dbConn.keys(cls._prefixClient + serverIp + ':'):
                result[serverIp].append(clientKey.replace(cls._prefixClient + serverIp + ':', ''))
        return result
