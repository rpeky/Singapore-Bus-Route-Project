import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

headers = {'AccountKey' : '4BXSLAQ5T+C4NJ6TA9/qjA==',
           'accept' : 'application/json'  
          }

#can use to obtain bus stop data, just put all the bus stop codes into a list and recall function
def bus_stop_bus_info(busstopno):
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode='+busstopno)
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

    for bus in content['Services']:
        print(json.dumps(bus, sort_keys=True, indent=4))

    print('hi0')
    jsonObj = json.loads(content)
    print('hi1')
    print(json.dumps(jsonObj, sort_keys=True, indent=4))
    print('hi2')
    

    with open("bus_arrivals.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    #with open('bus_arrivals.json') as f:
    #    data = json.load(f)

    #print(data["ServiceNo"])

#def getfile(fname):
#    with open(fname) as f:
#        data = json.load(f)

#    for bus in data:
#        print(ServiceNo['ServiceNo'],)




    




if __name__ == "__main__":
    #tempstrbusno can be a list
    tempstrbusno = '85091'
    bus_stop_bus_info(tempstrbusno)

    #getfile('bus_arrivals.json')
    
    #servicenoget('bus_arrivals.json')












