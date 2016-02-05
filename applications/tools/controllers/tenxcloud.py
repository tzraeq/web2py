# -*- coding: utf-8 -*-

import json

from com.baoze.tenxcloud import api

def index():
    return dict(message="hello from tenxcloud.py")

def port():
    region = request.args[0]
    service = request.args[1]
    port = request.args[2]

    return api.getMappedPort(region,service,port)