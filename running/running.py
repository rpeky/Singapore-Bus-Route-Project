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
    
    target = urlparse(uri+path_bsc+stopcode) #+path_sn+service_no  +'ServiceNo=12'
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
   
    with open("bus_routes.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)


def busstopsget(busn):
    #http://datamall2.mytransport.sg/ltaodataservice/BusStops
    uri = 'http://datamall2.mytransport.sg/'
    path = 'ltaodataservice/BusStops='
    
    target = urlparse(uri+path+busn)
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
   
    with open("bus_stops.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

def busroute():
    #http://datamall2.mytransport.sg/ltaodataservice/BusRoutes

    target = urlparse("http://datamall2.mytransport.sg/ltaodataservice/BusRoutes")
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
   
    with open("bus_routes.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)




if __name__=="__main__":
    sc = '85091'
    #sn = '12'
    print(busstopcodedata(sc))
    
    #x = '01239' #busstop number
    #printxd = busroute()
    #print(printxd)






   #y = '12'
   #printingxd = busstopsget(y)
   #print(printingxd)



     
    

    



