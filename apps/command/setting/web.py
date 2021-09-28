#!/usr/local/bin/python3
#-*- encoding: utf-8 -*-
from flask import Flask
from flask_restx import Api

from setting import config
from app.api.client import worker_client

def run():
    app = Flask(__name__)
    api = Api(
        app,
        version='dev_0.1',
        title='Integrated Worker Server API',
        description='작업 명령 서버',
        terms_url="/",
        contact="unripedata@gmail.com",
        license="MIT",
        url_scheme='http'
    )
    api.add_namespace(worker_client, '/worker/client')
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG, use_reloader=False)
    # api.add_namespace(command_check, '/command/check')
    # api.add_namespace(command_check, '/client/check')
    # api.add_namespace(order_worker_client_clientOrder_check, '/order/client')
    # api.add_namespace(ra_command_sync_client_device, '/save/client/device')