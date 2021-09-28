#!/usr/local/bin/python3
#-*- encoding: utf-8 -*-
import time
from setting import config, client
from common.thread import ThreadDev


def init():
    t = ThreadDev()
    while True:
        if not t.alive('client'):
            t.run('client', client.run, ())
        time.sleep(config.CHECK_TIME)




