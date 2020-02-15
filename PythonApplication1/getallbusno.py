import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

headers = {'AccountKey' : '4BXSLAQ5T+C4NJ6TA9/qjA==',
           'accept' : 'application/json'  
          }

## $skip=x function for api call is broken ==> see plan b
def busroute(skips):
    if skips == 0:
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?') 
        target.geturl()
        method = 'GET'
        body = ''

        h = http.Http()

        response, content = h.request(
            target.geturl(),
            method,
            body,
            headers
            )
    
        jsonobj = json.loads(content)
        #print(json.dumps(content, sort_keys=True, indent=4))

        with open("bus_route_info_0.json","w") as outfile:
            json.dump(jsonobj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

        print("done")

    else:
        skippos = str(skips*500)
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip='+skippos)
        target.geturl()
        method = 'GET'
        body = ''

        h = http.Http()

        response, content = h.request(
            target.geturl(),
            method,
            body,
            headers
            )

        jsonobj = json.loads(content)
       #print(json.dumps(jsonObj, sort_keys=True, indent=4))
        json.loads(content)
        with open("bus_route_info_"+skippos+".json","w") as outfile:
            json.dump(jsonobj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

        print("done")





if __name__ == "__main__":
    for number in range(100):
        busroute(number)

    print("done :)") 