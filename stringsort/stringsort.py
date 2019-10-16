import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

headers = {'AccountKey' : 'V3Vgr4XCSiCOCLGwxt6QbQ==',
           'accept' : 'application/json'  
          }


def busstopcodedata(stopcode):
    #, service_no
    #http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2
    uri = 'http://datamall2.mytransport.sg/'
    path_bsc = 'ltaodataservice/BusArrivalv2?BusStopCode='
    #path_sn = ',ServiceNo='
    
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=83139') #+path_sn+service_no  +'ServiceNo=12'
    target.geturl()
    method = 'GET'
    body = ''      
    
    h = http.Http()

    response, content = h.request (
        target.geturl(),
        method,
        body,
        headers
        )

    jsonObj = json.loads(content)
    jsonprintingxd = json.dumps(jsonObj, sort_keys=True, indent = 4)
    print (jsonprintingxd)
   
    with open("bus_routesstringsort.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

        #2d array/list storage format
        #list[a][b]
        #where a = bus no
        #b0 = current bus stop
        #b1 = next bus stop
        #b2 = previous bus stop  

if __name__ == "main":
    busstop = '85091'
    x = busstopcodedata(busstop)
    print(x)


    print()
    
         

    