import json
from flask import session
from setting.config import config
from common.utils import Utils


class Session:
    def checkSession(self):
        result = {"result": False}
        if "sessionKey" not in session:
            return result
        else:
            result = {"result": False}
            method = "POST"
            url = config.INNER_API+"/auth/check/session"
            j = {
                "token": config.TOKEN,
                "session": session["sessionKey"]
            }
            res = Utils.requestUrl(method=method, url=url, json=j)
            if res.status_code == 200:
                result = json.loads(res.text)
            else:
                del session["sessionKey"]
            return result

