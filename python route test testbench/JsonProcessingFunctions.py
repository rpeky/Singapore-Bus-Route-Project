import json
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

#Functions to generate Bus Stop data
# Stuff to obtain
    #BusStopCode = int    //map 1
    #Direction = int      //map 2
    #Distance = float     //map 3
    #StopSequence = int   //map 4
    #IDofBus = list       //map 5
    #TimesVisited = int   //map 6
    #Description = str    //map 7 - Bus Stop Name

headers = {'AccountKey' : '4BXSLAQ5T+C4NJ6TA9/qjA==',
           'accept' : 'application/json'  
          }

##API 2.1 Bus Arrival Request
#can use to obtain bus stop data, just put all the bus stop codes into a list and recall function
#use during daytime when there are active bus
def generate_BusArrivalData_returnsBusServiceID(BusStopCode):
    #make sure the int BusStopCode becomes a string
    target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2?BusStopCode='+str(BusStopCode))
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
    #create file to read in future
    with open(str(BusStopCode)+"_BusArrivalRequest_BusStop_data.json","w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    return

##API 2.2 Bus Services Request
def generate_BusServicesData_returnsUnsure(skips):
    skippos = str(skips*500)
    if skippos == 0:
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusServices')
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
        #create file to read in future
        with open("0_BusServicesRequest_data.json","w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    else:
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusServices?skip='+skippos)
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
        #create file to read in future
        with open(str(skips)+"_BusServicesRequest_data.json","w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

##API 2.3 Bus Routes Request
def generate_BusRoutesData_returnsUnsure(skips):
    skippos = str(skips*500)
    if skippos == 0:
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes')
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
        #create file to read in future
        with open("0_BusRoutesRequest_data.json","w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    else:
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusRoutes?skip='+skippos)
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
        #create file to read in future
        with open(str(skips)+"_BusRoutesRequest_data.json","w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return

##API 2.4 Bus Stops Request
#obtain Description from BusStopCode here
def generate_BusStopsRequest_togetallbusstop(skips): #need to loop 10 times (0 to range(11)) but check 11th element in case  #bus_stop_no_info.json
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

        with open("0_BusStopsRequest_bus_stop_info.json","w") as outfile:
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
        #create file to read in future
        with open(str(skips)+"_BusStopsRequest_bus_stop_info.json","w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return

def generate_all_BusStopsRequest_info_jsonfile():
    for i in range(11):
        generate_BusStopsRequest_togetallbusstop(i)
        print('done with generate_all_BusStopsRequest_info_jsonfile #'+str(i))
    return

def generate_all_BusServicesRequest_info_jsonfile():
    for i in range(1):
        generate_BusServicesData_returnsUnsure(i)
        print('done with generate_all_BusServicesRequest_info_jsonfile #'+str(i))
    return

def generate_all_BusRoutesRequest_info_jsonfile():
    for i in range(1):
        generate_BusRoutesData_returnsUnsure(i)
        print('done with generate_all_BusRoutesRequest_info_jsonfile #'+str(i))
    return

#loads json obj from json file
def open_jsondatafile_returnsjsonobj(identifier, indextoload):
    #filetypes expect int
    #error    - 0 unexpected error // for matching api index with load index
    #arrivals - 1 API 2.1 Bus Arrival Request
    #services - 2 API 2.2 Bus Services Request
    #routes   - 3 API 2.3 Bus Routes Request
    #stops    - 4 API 2.4 Bus Stops Request

    jsondatafilenamingsuffix = ['errorindex', '_BusArrivalRequest_BusStop_data.json', '_BusServicesRequest_data.json', \
                                '_BusRoutesRequest_data.json', '_BusStopsRequest_bus_stop_info.json' ]

    filename = str(identifier)+str(jsondatafilenamingsuffix[int(indextoload)])
    f = open(filename)
    jsonobj = json.load(f)
    return jsonobj


##Search functions
#Works, able to obtain Bus ID (Services) from Bus Stop
def search_jsonobj_busstop_busidinstop_returnslistofid(jsonobjtoload):
    listofbusid = []
    for i in jsonobjtoload['Services']:
        listofbusid.append(i['ServiceNo'])
    return listofbusid

#will comb through the busroutes dataset to find busstopcode
def search_jsonobj_busroutes_busstopcode_returnslistofbsc(jsonobjtoload):
    listofbsc = []
    for i in jsonobjtoload['Value']:
        listofbsc.append(i['BusStopCode'])
    return listofbsc


