# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect, request
from common.auth.session import Session
from common.auth.menu import Menu
from common.worker.command import Command
from common.utils import Utils
from common.init import Init
import json

template_path = Init.tempPath()
api_path = Init.apiPath()
bp_menu_page_client_device_main = Blueprint("menu_page_client_device_main", __name__, template_folder="/templates")

'''
디바이스 화면
Device screen
author: 이재영 (Jae Young Lee)
'''
@bp_menu_page_client_device_main.route("/")
def menu_page_client_device_view():
    # 세션 여부 체크
    userInfo = Session().checkSession()
    if not userInfo["result"]:
        return redirect(url_for("index_sign.signin_view"))

    menu = Menu()
    # 메뉴 권한 확인
    isMenuAuth = menu.isAuth("/client/device", userInfo["data"])
    if not isMenuAuth["result"]:
        return redirect(url_for("index_index.index_view"))
    menuHtml = menu.list("/client/device", userInfo["data"])

    apiUrl = Init.apiPath() + "/user/authority"
    resAuthority = Utils.requestUrl(method="GET", url=apiUrl)
    if resAuthority.status_code == 200:
        resAuthorityJson = json.loads(resAuthority.text)
    if resAuthorityJson["result"]:
        authoritys = resAuthorityJson["data"]
    else:
        authoritys = None
    return render_template(template_path + '/main/menu/pages/client/device.html', menuHtml=menuHtml, authoritys=authoritys)

'''
클라이언트 서버 정보
Clinet Server Info
author: 이재영 (Jae Young Lee)
'''
@bp_menu_page_client_device_main.route("/get/list", methods =['POST'])
def menu_page_client_device_get_list():
    if not Session().checkSession():
        return redirect(url_for('index_sign.signin_view'))
    j = request.json
    command = Command()
    clients = command.getClientDeviceList()
    result = {}
    if j['ip']:
        result[j['ip']] =  clients[j['ip']]
    else:
        result = clients
    result = {"result": True, "data":result}
    return json.dumps(result)

'''
클라이언트 서버 정보
Clinet Server Info
author: 이재영 (Jae Young Lee)
'''
@bp_menu_page_client_device_main.route("/sync", methods=['POST'])
def menu_page_client_device_sync():
    if not Session().checkSession():
        return redirect(url_for('index_sign.signin_view'))
    command = Command()
    command.syncClientDeviceList()
    result = {"result": True}
    return json.dumps(result)


