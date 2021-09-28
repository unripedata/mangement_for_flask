# -*- coding: utf-8 -*-
from flask import Blueprint, request
from common.utils import Utils
from common.worker import Server, Client

import json
from setting.config import config

conf = config
bp_worker_server = Blueprint("bp_worker_server", __name__)

'''
Worker Client 서버 관련
author: 이재영 (Jae Young Lee)
'''
@bp_worker_server.route("/connect", methods =['GET'])
def index_view():
    res = ''
    req = request.json
    chkKey = ['token']

    if not Utils.isDicHasKey(req, chkKey):
        return res
    if not Utils.isDicKeyValueNull(req, chkKey):
        return res

    servers = Client().getList()
    cnt = 0
    for ip in servers:
        if cnt <= len(servers[ip]):
            cnt, res = len(servers[ip]), ip
    return res