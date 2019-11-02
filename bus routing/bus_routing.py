import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

headers = {'AccountKey' : '4BXSLAQ5T+C4NJ6TA9/qjA==',
           'accept' : 'application/json'  
          }

def getbusstop(skips): #need to loop 12 times   #bus_stop_no_info.json
    skippos = str(skips*500)
    if skippos == 0:
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
        #print(json.dumps(jsonObj, sort_keys=True, indent=4))

        with open("bus_stop_no_info.json","w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    else:
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusStops?$skip='+skippos)
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
        #print(data['Services'][x]['ServiceNo'])
        #print(data['Services'][x]['NextBus']['DestinationCode'])
        filetowrite.write(data['Services'][x]['ServiceNo'])
        filetowrite.write("\n")
        filetowrite.write(data['Services'][x]['NextBus']['DestinationCode'])
        filetowrite.write("\n")
        x+=1

def allbusanddestination():

    for t in range(0,12):
        print("loop #"+str(t))        
        getbusstop(t)
        with open("bus_stop_no_info.json") as f:
            busstopinfo = json.load(f)
        i=0
        print("output to file #"+str(t))
        temp_bus_stop_code = ''
        for a in busstopinfo['value']:
            temp_bus_stop_code = busstopinfo['value'][i]['BusStopCode']
            filetowrite.write(temp_bus_stop_code)
            filetowrite.write("\n")
            #print(temp_bus_stop_code)
            #print("\n")
            bus_stop_bus_info(temp_bus_stop_code)
            busanddestination()
            filetowrite.write("\n\n\n")
            #print("\n\n\n")
            i+=1

    return 0
    
    


    




if __name__ == "__main__":
    filetowrite = open('busstop_busno_destination.txt', 'w')
    allbusanddestination()
    filetowrite.close()
    print("done :)")
    
    
    
    
  












