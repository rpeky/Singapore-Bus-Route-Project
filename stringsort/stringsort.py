import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

headers = {'AccountKey' : 'V3Vgr4XCSiCOCLGwxt6QbQ==',
           'accept' : 'application/json'  
          }

def busstopcodedata():
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode=83139') 
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
    print(json.dumps(jsonObj, sort_keys=True, indent = 4))
    with open("bus_stop_code_data.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)


        #2d array/list storage format
        #list[a][b]
        #where a = bus no
        #b0 = current bus stop
        #b1 = next bus stop
        #b2 = previous bus stop  

if __name__ == "main":
    print(busstopcodedata())

         

    