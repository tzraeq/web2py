# -*- coding: utf-8 -*-

import json

from com.baoze.tenxcloud import api

def index():
    regions = [];
    regionsDict = api.getRegions()
    if api.KEY_REGIONS in regionsDict:
        for region in regionsDict[api.KEY_REGIONS]:
            regionName = region[api.KEY_REGION_NAME]
            servicesDict = api.getServices(str(regionName))
            if api.KEY_SERVICES in servicesDict:
                services = servicesDict[api.KEY_SERVICES];
                if(len(services) > 0):
                    regionObj = {"name":regionName,"displayName":region[api.KEY_REGION_DISPLAY_MAME],"services":[]}
                    regions.append(regionObj)
                    for service in services:
                        serviceObj = {"name":service[api.KEY_SERVICE_NAME],"ports":[]}
                        regionObj["services"].append(serviceObj)
                        for portMapping in service[api.KEY_PORT_MAPPING]:
                            pm = {"protocol":portMapping[api.KEY_PROTOCOL],"url":portMapping[api.KEY_SERVICE_URL],"port":portMapping[api.KEY_CONTAINER_PORT]}
                            serviceObj["ports"].append(pm)

    return dict(regions=regions)

def port():
    region = request.args[0]
    service = request.args[1]
    port = request.args[2]

    return api.getMappedPort(region,service,port)