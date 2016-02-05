# -*- coding: utf-8 -*-

import pycurl
import json
import config
from io import BytesIO

def require(url):
        e = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, url)
        curl.setopt(pycurl.HTTPHEADER,['username:'+config.USERNAME,'Authorization: token '+config.TOKEN])
        curl.setopt(pycurl.WRITEFUNCTION, e.write)
        curl.setopt(pycurl.SSL_VERIFYPEER, 0)
        curl.setopt(pycurl.SSL_VERIFYHOST, 0)
        curl.perform()
        curl.close()

        return json.loads(e.getvalue())

def getServices(region):
    return require("https://api.tenxcloud.com/%s/regions/%s/services" % (config.APIVERSION,region))

def getService(region,service):
    return require("https://api.tenxcloud.com/%s/regions/%s/services/%s" % (config.APIVERSION,region,service))

def getInstances(region,service):
    return require("https://api.tenxcloud.com/%s/regions/%s/services/%s/instances" % (config.APIVERSION,region,service))

def getMappedPort(region,service,port):
    url = getMappedUrl(region,service,port)
    return url.split(":")[1]

def getMappedUrl(region,service,port):
    ser = getService(region,service)
    url = None
    portMappings = ser["port_mapping"]
    for portMapping in portMappings :
        if(int(port) == portMapping["container_port"]):
            url = portMapping["service_url"]
            break
    return url