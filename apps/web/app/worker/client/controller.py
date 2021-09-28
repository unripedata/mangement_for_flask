# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect, session
from common.auth.session import Session
from common.menu import menuCreateHtml
from common.worker import Server, Client
# from common.worker.command import Command

import json
from setting.config import config

conf = config
bp_worker_client = Blueprint("bp_worker_client", __name__)

'''
Worker Client 서버 관련
author: 이재영 (Jae Young Lee)
'''

@bp_worker_client.route("/list", methods =['POST'])
def index_view():
    # if not Session().checkSession()['result']:
    res = {
        'result':True,
        'data': json.dumps(Client().getList())
    }
    return res