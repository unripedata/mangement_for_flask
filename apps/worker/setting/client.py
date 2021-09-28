#!/usr/local/bin/python3
#-*- encoding: utf-8 -*-
import time
from setting import config

from common.utils import Utils
from common.socket.tcp.client import TCPClient

async def worker(cate, msg):
    tcpClient = TCPClient()
    if msg == 'init':
        time.sleep(1)
        ip = Utils.ipCheck()
        reMsg = ip
        tcpClient.reMsg(reMsg)
    # if msg == 'sync_system_status':
    #     device = Device()
    #     result = device.job_sys_status()
    #     ip = Utils.ipCheck()
    #     result["ip"] = ip
    #     url = Init.getCommandPath() + "/save/client/device/info"
    #     req = Utils.requestUrl(method='POST', url=url, json=result)


def run():
    tcpClient = TCPClient(host=config.TCP_HOST, port=config.TCP_PORT)
    tcpClient.runBatch(worker)






