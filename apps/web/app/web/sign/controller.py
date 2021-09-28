# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, session
import json
import logging

from common.utils import Utils
from setting.config import config

conf = config
bp_web_sign = Blueprint("bp_web_sign", __name__)

@bp_web_sign.route("/signin")
def signin_view():
    return render_template(conf.TEMPLATE_NAME + '/main/index/auth/signIn.html')

@bp_web_sign.route("/signin.do", methods =['POST'])
def signin_ajax():
    req = request.json
    result = {"result": False}
    j = {
        'token': config.TOKEN,
        'account': req
    }
    method = 'POST'
    url = conf.INNER_API + '/auth/signin'

    resApiLogin = Utils.requestUrl(method=method, url=url, json=j)
    loginJson = json.loads(resApiLogin.text)
    if resApiLogin.status_code == 200:
        if loginJson['session']:
            session['sessionKey'] = loginJson['session']
            result["result"] = True
    else:
        result['code'] = loginJson['code']
        result['msg'] = loginJson['msg']
    return json.dumps(result)

@bp_web_sign.route("/signout.do", methods =['POST'])
def signout_ajax():
    result = {"result": False, "msg": "로그아웃에 실패하였습니다."}
    j = {
        'token': config.TOKEN,
        "session":session["sessionKey"]
    }
    method = "POST"

    url = conf.INNER_API +"/auth/signout"
    resSignout = Utils.requestUrl(method=method, url=url, json=j)

    if resSignout.status_code == 200:
        loginJson = json.loads(resSignout.text)
        if loginJson["result"]:
            result["result"] = True
            del result["msg"]
    return json.dumps(result);