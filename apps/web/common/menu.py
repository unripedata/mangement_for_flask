# -*- coding: utf-8 -*-
import json
from setting.config import config
from common.utils import Utils
from flask import session

def menuCreateHtml(url: str):
    navHtml = ''
    list = None
    method = "POST"
    apiUrl = config.INNER_API + "/sys/imw/menu"
    j = {
        "token": config.TOKEN,
        "session": session["sessionKey"]
    }

    resMenu = Utils.requestUrl(method=method, url=apiUrl, json=j)
    if resMenu.status_code == 200:
        resMenuJson = json.loads(resMenu.text)
        list = resMenuJson['data']

    if list:
        for i in range(len(list)):
            m = list[i]
            if m['depth'] == 1:
                navHtml = navHtml + """<li class="sidebar-header">
                        %s
                    <li> 
                """ % (m["name"])
                for j in range((i+1), len(list)):
                    m2 = list[j]
                    if m["id"] == m2["pid"]:
                        if m2["url"] is not None:
                            if m2["url"] == url:
                                active = ' active'
                            else:
                                active = ''
                            navHtml = navHtml + """<li class="sidebar-item%s">
                                <a class="sidebar-link" href="%s">
                                    <i class="align-middle" data-feather="sliders"></i> <span class="align-middle">%s</span>
                                </a>
                            </li>
                            """ % (active, m2["url"], m2["name"])
                        else:
                            show = ""
                            nav2Html = ""
                            for k in range((j+1), len(list)):
                                m3 = list[k]
                                if m2["id"] == m3["pid"]:
                                    if m3["url"] == url:
                                        active = " active"
                                        show = " show"
                                    else:
                                        active = ""
                                    nav2Html = nav2Html+""" <li class="sidebar-item%s"><a class="sidebar-link" href="%s">%s</a></li>""" % (active, m3["url"], m3["name"])
                            navHtml = navHtml + """<li class="sidebar-item">
                                <a href="#nav-%s" data-toggle="collapse" class="sidebar-link collapsed">
                                    <i class="align-middle" data-feather="users"></i> <span class="align-middle">%s</span>
                                </a>
                                <ul id="nav-%s" class="sidebar-dropdown list-unstyled collapse%s" data-parent="#sidebar">
                            """ % (m2["name"], m2["name"], m2["name"], show)
                            navHtml = navHtml + nav2Html
                            navHtml = navHtml + """
                                </ul>
                            </li>
                            """
            else:
                continue
    return navHtml


