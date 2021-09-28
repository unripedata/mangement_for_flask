#!/usr/bin/env python3
#-*- encoding: utf-8 -*-
from setting import init


if __name__ == "__main__":
    init()

# import time
# import asyncio



# from common.socket.tcp.client.tcpClient import TCPClient
# from common.thread.threadDev import ThreadDev
#
# from app.device.device import Device
# from common.utils import Utils
# from common.init import Init
#
# HOST = '125.180.129.217'
# PORT = 20000
#
#





# if __name__ == "__main__":

    # thread 공통 함수
    # threadDev = ThreadDev()
    # tcpClient = TCPClient(host=HOST, port=PORT)
    # while True:
    #     # thread 실행 여부 체크
    #     if not threadDev.state('tcpClient')["result"]:
    #         threadDev.run("tcpClient", tcpClient.runBatch, (worker,))
    #     time.sleep(30)