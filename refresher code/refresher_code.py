import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

## for api http://datamall2.mytransport.sg/ 
headers = {'AccountKey' : '4BXSLAQ5T+C4NJ6TA9/qjA==',
           'accept' : 'application/json'  
          }


## function to gather bus stop data
def getbusstopdata(pageno):
    skippgno = str(pageno*500)

    #page 1
    if skippgno == 0:
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusStops')
        target.geturl()
        method = 'GET'
        body = ''

        h = http.HTTP()

        response, content = h.request(
            target.geturl(),
            method,
            body,
            headers
            )

        jsonObj = json.loads(content)

        with open("bus_stop_no_info_refresh.json","w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    #page > 1
    else:
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip='+skippgno)
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
        jsonObj = json.loads(content)

        with open("bus_stop_no_info_refresh_" + str(pageno) + ".json","w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)






if __name__ == "__main__":
    #run to refresh json 
    for i in range(0,11):
        getbusstopdata(i)



