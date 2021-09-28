#!/usr/local/bin/python3
#-*- encoding: utf-8 -*-
from common.socket.tcp.server.tcpServer import TCPServer
from setting import config


def run():
    tcpServer = TCPServer()
    tcpServer.runServer(config.TCP_PORT)




