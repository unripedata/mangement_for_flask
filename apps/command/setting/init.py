#!/usr/local/bin/python3
#-*- encoding: utf-8 -*-
from common.socket.tcp.server.tcpServer import TCPServer
from common import Utils
from common.thread import ThreadDev
from setting import config, worker, web

import time


def registerWorkerServer():
    while True:
        token = config.UID
        web_url = config.WEB_URL + "/api/check/ip"
        web_res = Utils.requestUrl(method="GET", url=web_url)
        ip = web_res.text
        j = {"token": config.TOKEN, "uid": config.UID, "ip": ip}
        reg_url = config.INNER_API + "/worker/server/register"
        resApi = Utils.requestUrl(method="POST", url=url, json=j)
        if resApi.status_code == 200:
            result = {"result": True}
        else:
            result = {"result": False}
        time.sleep(config.REREG_TIME)


def init():
    print(config.UID)
    t = ThreadDev()
    while True:
        if not t.alive('regist'):
            t.run('regist', registerWorkerServer, ())
        if not t.alive('web'):
            t.run('web', web.run, ())
        if not t.alive('worker'):
            t.run('worker', worker.run, ())
        time.sleep(config.CHECK_TIME)





