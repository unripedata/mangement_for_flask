# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect, session
from common.auth.session import Session
from common.menu import menuCreateHtml
from common.worker import Server, Client
from setting.config import config

conf = config
bp_web_index = Blueprint("bp_web_index", __name__)

'''
메인 화면
Main screen
author: 이재영 (Jae Young Lee)
'''

@bp_web_index.route("/")
def index_view():
    if not Session().checkSession()['result']:
        return redirect(url_for("bp_web_sign.signin_view"))

    menuHtml = menuCreateHtml("/")
    serverCnt = len(Server().getList())
    clientCnt = 0
    servers = Client().getList()
    for server in servers:
        clientCnt = clientCnt + len(servers[server])

    return render_template(conf.TEMPLATE_NAME + '/main/index/index.html', menuHtml=menuHtml, clientCnt=clientCnt, serverCnt=serverCnt)