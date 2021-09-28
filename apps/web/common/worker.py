# # -*- coding: utf-8 -*-
import json
from setting.config import config
from common.utils import Utils
from flask import session


class Server:
    def getList(self):
        result = []
        method = 'POST'
        apiUrl = config.INNER_API + '/worker/server/list'
        j = {'token': config.TOKEN}
        res = Utils.requestUrl(method=method, url=apiUrl, json=j)
        resJson = json.loads(res.text)
        return resJson['server']

class Client:
    def getList(self):
        method = 'POST'
        apiUrl = config.INNER_API + '/worker/client/list'
        j = {'token': config.TOKEN}
        res = Utils.requestUrl(method=method, url=apiUrl, json=j)
        return json.loads(res.text)

#     # Worker Client 개수 체크
#     def syncClinetCount(self):
#         result = True
#         # 연결된 Command 정보 추출
#         commandList = {}
#         method = "POST"
#
#         apiUrl = config.INNER_API + "/worker/command/list"
#         resCommand = requestUrl(method=method, url=apiUrl)
#         if resCommand.status_code == 200:
#             resCommandJson = json.loads(resCommand.text)
#             if resCommandJson["result"]:
#                 commandList = resCommandJson['data']
#         for command in commandList:
#             try:
#                 j = {"token":commandList[command]}
#                 commandUrl = "http://" + command + ":" + str(Init.getCommandPort()) + "/order/check/clients"
#                 resCommand = Utils.requestUrl(method=method, url=commandUrl, json=j)
#             except Exception as ex:
#                 commandDelUrl = "http://"+command+":"+str(Init.getCommandPort()) + "/worker/command/del"
#                 print(ex)
#         return result
#
#     # Worker Client 개수 동기화
#     def getClientList(self):
#         clients = {}
#         method = "POST"
#         apiUrl = config.INNER_API + "/worker/client/get/clients"
#         resClient = requestUrl(method=method, url=apiUrl)
#         if resClient.status_code == 200:
#             resClientJson = json.loads(resClient.text)
#             clients = resClientJson['data']
#         return clients
#
#     # Worker Client 개수 동기화
#     def syncClientDeviceList(self):
#         result = True
#         # 연결된 Command 정보 추출
#         commandList = {}
#         method = "POST"
#         apiUrl = config.INNER_API + "/worker/command/list"
#         resCommand = requestUrl(method=method, url=apiUrl)
#         if resCommand.status_code == 200:
#             resCommandJson = json.loads(resCommand.text)
#             if resCommandJson["result"]:
#                 commandList = resCommandJson['data']
#         for command in commandList:
#             try:
#                 j = {"token": commandList[command]}
#                 commandUrl = "http://" + command + ":" + str(Init.getCommandPort()) + "/order/check/clients/device"
#                 resCommand = requestUrl(method=method, url=commandUrl, json=j)
#             except Exception as ex:
#                 commandDelUrl = "http://" + command + ":" + str(Init.getCommandPort()) + "/worker/command/del"
#                 print(ex)
#         return result
#
#     # Worker Client 개수 동기화
#     def getClientDeviceList(self):
#         clients = {}
#         method = "POST"
#         apiUrl = config.INNER_API + "/worker/client/get/clients/device"
#         resClient = requestUrl(method=method, url=apiUrl)
#         if resClient.status_code == 200:
#             resClientJson = json.loads(resClient.text)
#             clients = resClientJson['data']
#         return clients
#
#     # Worker Command 개수 체크
#     def getCommandList(self):
#         commands = {}
#         method = "POST"
#         apiUrl = Init.apiPath() + "/worker/command/list"
#         resCommand = requestUrl(method=method, url=apiUrl)
#         if resCommand.status_code == 200:
#             resCommandJson = json.loads(resCommand.text)
#             commands = resCommandJson['data']
#         return commands
#
#     # Worker Command 동기화
#     def syncCommands(self):
#         delCommands = []
#         commands = {}
#         method = "POST"
#         apiUrl = Init.apiPath() + "/worker/command/list"
#         resCommand = requestUrl(method=method, url=apiUrl)
#         if resCommand.status_code == 200:
#             resCommandJson = json.loads(resCommand.text)
#             if resCommandJson["result"]:
#                 commands = resCommandJson['data']
#         for command in commands:
#             try:
#                 j = {"token": commands[command]}
#                 commandChkUrl = "http://"+command+":"+str(Init.getCommandPort()) + "/command/check/connect"
#                 resCommandChk = requestUrl(method=method, url=commandChkUrl, json=j)
#                 if resCommandChk.status_code == 200:
#                     resCommandChkJson = json.loads(resCommand.text)
#                     if not resCommandJson["result"]:
#                         delCommands.append(command)
#             except Exception as ex:
#                 delCommands.append(command)
#
#         if len(delCommands) > 0:
#             apiCommandDelUrl = Init.apiPath() + "/worker/command/delete"
#             j = { "ip":delCommands }
#             resApiCommandDel = Utils.requestUrl(method=method, url=apiCommandDelUrl, json=j)
#
#         for command in delCommands:
#             del commands[command]
#         return commands
