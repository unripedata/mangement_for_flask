# -*- coding: utf-8 -*-
from flask import Blueprint, request
from setting.config import config
from common.utils import Utils

conf = config
bp_common_check = Blueprint("bp_common_check", __name__)


@bp_common_check.route("/ip", methods=['GET'])
def index_view():
    req = request.json
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return ip
