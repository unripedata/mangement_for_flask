#!/usr/local/bin/python3
#-*- encoding: utf-8 -*-
import socketserver
import json

from common.socket.tcp.server.lib.tcpClientManager import TCPClientManager


class TCPHandler(socketserver.BaseRequestHandler):
    tcpClientManger = TCPClientManager()

    def handle(self):
        print('[%d] 연결 요청' % self.client_address[1])
        client_name = None
        try:
            client_name = self.registerUsername()
            if client_name is not None:
                msg = self.request.recv(1024)
                while msg:
                    req = {'server': self.client_address[0], 'msg': json.loads(msg.decode())}
                    msg = self.request.recv(1024)
        except Exception as e:
            print(e)
         
        if client_name is not None:
            print('[%s] 접속종료' % self.client_address[0])
            self.tcpClientManger.removeClient(client_name)
 
    def registerUsername(self):
        while True:
            conn, addr = self.request, self.client_address
            msg = {'job': 'init'}
            conn.send(json.dumps(msg).encode())
            try:
                msg = self.request.recv(1024)
                if msg:
                    conn.send(json.dumps(True).encode())
                else:
                    conn.send(json.dumps(False).encode())
                    return None
            except Exception as ex:
                print(ex)
            client_name = msg.decode()
            client_name = self.tcpClientManger.addClient(client_name, self.request, self.client_address)

            if client_name is not None:
                return client_name
            else:
                return None