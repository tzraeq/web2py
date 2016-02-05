# -*- coding: utf-8 -*-

import pycurl
import json
import config
from io import BytesIO

KEY_REGIONS = "regions"
KEY_REGION_NAME = "name"
KEY_REGION_DISPLAY_MAME = "display_name"

KEY_SERVICES = "services"
KEY_SERVICE_REGION = "region"
KEY_SERVICE_NAME = "name"

KEY_PORT_MAPPING = "port_mapping"
KEY_CONTAINER_PORT = "container_port"
KEY_SERVICE_URL = "service_url"
KEY_PROTOCOL = "protocol"

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

def getRegions():
    return require("https://api.tenxcloud.com/%s/regions" % (config.APIVERSION))

def getServices(region):
    return require("https://api.tenxcloud.com/%s/regions/%s/services" % (config.APIVERSION,region))

def getService(region,service):
    return require("https://api.tenxcloud.com/%s/regions/%s/services/%s" % (config.APIVERSION,region,service))

def getInstances(region,service):
    return require("https://api.tenxcloud.com/%s/regions/%s/services/%s/instances" % (config.APIVERSION,region,service))

def getMappedPortFromServiceUrl(url):
    return url.split(":")[1]

def getMappedPort(region,service,port):
    url = getMappedUrl(region,service,port)
    return getMappedPortFromServiceUrl(url)

def getMappedUrl(region,service,port):
    ser = getService(region,service)
    url = None
    portMappings = ser[KEY_PORT_MAPPING]
    for portMapping in portMappings :
        if(int(port) == portMapping[KEY_CONTAINER_PORT]):
            url = portMapping[KEY_SERVICE_URL]
            break
    return url
