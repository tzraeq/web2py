# -*- coding: utf-8 -*-

import json
import ConfigParser
from com.baoze.tenxcloud import config
from com.baoze.tenxcloud import api

def index():
    regions = db().select(db.region.ALL)

    return dict(regions=regions)
def port():
    region = request.args[0]
    service = request.args[1]
    port = request.args[2]

    #return api.getMappedPort(region,service,port)
    rows = db((db.portMapping.port==int(port))&(db.service.name==service)&(db.region.name==region)).select(db.portMapping.url)
    if len(rows) > 0:
		return api.getMappedPortFromServiceUrl(rows[0]["url"])
    else:
		return "0"

def refresh():
    regions = []
    regionsDict = api.getRegions()
    if api.KEY_REGIONS in regionsDict:
        db(db.region).delete()
        for region in regionsDict[api.KEY_REGIONS]:
            regionName = region[api.KEY_REGION_NAME]
            regionId = db.region.insert(name=regionName,displayName=region[api.KEY_REGION_DISPLAY_MAME],status=region[api.KEY_REGION_STATUS])
            servicesDict = api.getServices(str(regionName))
            if api.KEY_SERVICES in servicesDict:
                services = servicesDict[api.KEY_SERVICES];
                if(len(services) > 0):
                    for service in services:
                        serviceId = db.service.insert(name=service[api.KEY_SERVICE_NAME],region=regionId)
                        for portMapping in service[api.KEY_PORT_MAPPING]:
                            db.portMapping.insert(protocol=portMapping[api.KEY_PROTOCOL],url=portMapping[api.KEY_SERVICE_URL],port=portMapping[api.KEY_CONTAINER_PORT],service=serviceId)
    return "ok"
