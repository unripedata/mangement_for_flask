#!/usr/local/bin/python3
#-*- encoding: utf-8 -*-
import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from setting.config import config

from app.api.check.controller import bp_common_check
from app.web.sign.controller import bp_web_sign
from app.web.index.controller import bp_web_index
from app.worker.client.controller import bp_worker_client
from app.worker.server.controller import bp_worker_server

# from app.index.controller.signController import bp_index_sign
# from app.index.controller.errorController import bp_index_error
# # from app.menu.setting.auth.controller.mainController import bp_menu_setting_auth_main
# # from app.menu.page.client.device.controller.mainController import bp_menu_page_client_device_main
# # from app.worker.command.controller.commandController import bp_client_command
# # from app.worker.client.controller.clientController import bp_worker_client

def run():
    conf = config
    app = Flask(__name__, template_folder=conf.TEMPLATE, static_folder=conf.STATIC)

    app.register_blueprint(bp_web_sign, url_prefix="/")
    app.register_blueprint(bp_web_index, url_prefix="/")

    app.register_blueprint(bp_common_check, url_prefix="/api/check")
    app.register_blueprint(bp_worker_client, url_prefix="/worker/client")
    app.register_blueprint(bp_worker_server, url_prefix="/worker/server")

    # # app.register_blueprint(bp_index_error, url_prefix="/")
    # app.register_blueprint(bp_client_command, url_prefix="/worker/command")
    # app.register_blueprint(bp_worker_client, url_prefix="/worker/client")
    # app.register_blueprint(bp_menu_page_client_device_main, url_prefix="/client/device")
    # app.register_blueprint(bp_menu_setting_auth_main, url_prefix="/setting")

    app.config['SECRET_KEY'] = conf.SECRET_KEY
    csrf = CSRFProtect()
    csrf.init_app(app)

    app.run(host=conf.HOST, port=conf.PORT, debug=conf.DEBUG)




