#import requests


#headers = {'AccountKey' : '4BXSLAQ5T+C4NJ6TA9/qjA==',
#           'accept' : 'application/json'  
#          }



#def busroute():
#    url = 'http://datamall2.mytransport.sg/ltaodataservice/BusRoutes'
#    jsonobj = requests.get(url).json()
#    with open("busroutejsonfile123123.json","w") as outfile:
#        json.dump(jsonobj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

#    #if(skips > 0):
#    #    jsonobj = requests.get(url+urladditions).json()
#    #    with open("busroutejsonfile.json","w") as outfile:
#    #        json.dump(jsonobj, outfile, sort_keys=True, indent=4, ensure_ascii=False)





#if __name__ == "__main__":
#    #for number in range(50):
#    busroute()
#    print("done :)") 




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
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes$skip=500') 
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

        with open("bus_stop_no_info123123.json","w") as outfile:
            json.dump(jsonobj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    else:
        skippos = str(skips*500)
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes$skip='+skippos)
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
        with open("bus_stop_no_info"+skippos+".json","w") as outfile:
            json.dump(jsonobj, outfile, sort_keys=True, indent=4, ensure_ascii=False)





if __name__ == "__main__":

    busroute(0)
    print("done :)") 