import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

if __name__=="__main__":
    headers = {'AccountKey' : 'V3Vgr4XCSiCOCLGwxt6QbQ==',
               'accept' : 'application/json'  
               }


    uri = 'http://datamall2.mytransport.sg/'
    path = 'ltaodataservice/BusServices' 
    x = '123455' #busstop number

    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=' + x)
    target.geturl()
    method = 'GET'
    body = ''      
    
    h = http.Http()

    response, content = h.request (
        target.geturl(),
        method,
        body,
        headers,
       # params = {"BusStopCode" : desu}
        )

    jsonObj = json.loads(content)
    jsonprintingxd = json.dumps(jsonObj, sort_keys=True, indent = 4)
    print (jsonprintingxd)

    with open("bus_routes.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)



