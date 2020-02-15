import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

headers = {'AccountKey' : '4BXSLAQ5T+C4NJ6TA9/qjA==',
           'accept' : 'application/json'  
          }

#def busroutesfn(skipno):
#    skippos = str(skipno*500)
#    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?$skip='+skippos)
#    target.geturl()
#    method = 'GET'
#    body = ''

#    h = http.Http()

#    response, content = h.request(
#        target.geturl(),
#        method,
#        body,
#        headers
#        )

#    jsonObj = json.loads(content)
#    print(json.dumps(jsonObj, sort_keys=True, indent=4))

#    with open("rotueinfo"+skipno+".json","w") as outfile:
#        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

#def listofbusstopsinroutes():




#def savebusrouteunderbusname():




if __name__ == "__main__":
    busroutesfn()
    print("done :)")
    
    
    
    
  












