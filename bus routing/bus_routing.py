import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

headers = {'AccountKey' : '4BXSLAQ5T+C4NJ6TA9/qjA==',
           'accept' : 'application/json'  
          }

def getbusstop():
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusStops')
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
    print(json.dumps(jsonObj, sort_keys=True, indent=4))

    with open("bus_stop_no_info.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

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

    jsonObj = json.loads(content)
    #print(json.dumps(jsonObj, sort_keys=True, indent=4))

    with open("bus_arrivals.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

def busanddestination(): #file name   -->  bus_arrivals.json
    with open("bus_arrivals.json") as f:
        data = json.load(f)

    x = 0
    for i in data['Services']:
        print(data['Services'][x]['ServiceNo'])
        print(data['Services'][x]['NextBus']['DestinationCode'])
        x+=1

def allbusanddestination():
    with open("bus_stop_no_info.json") as f:
        busstopinfo = json.load(f)

    i = 0
    temp_bus_stop_code = ''
    for a in busstopinfo['value']:
        temp_bus_stop_code = busstopinfo['value'][i]['BusStopCode']
        print(temp_bus_stop_code)
        print("\n")
        bus_stop_bus_info(temp_bus_stop_code)
        busanddestination()
        print("\n\n\n")
        i+=1




if __name__ == "__main__":
    allbusanddestination()
    
    
    
    
  











