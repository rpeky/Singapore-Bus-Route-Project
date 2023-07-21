import json
from unittest import skip
import urllib
import urllib.request
from urllib.parse import urlparse

import httplib2 as http 

#Functions to generate Bus Stop data
# Stuff to obtain
    #BusStopCode = str    //map 1 changed to string beacuse int cant start with 0 error
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
        target = urlparse('http://datamall2.mytransport.sg/ltaodataservice/BusServices?$skip='+skippos)
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
    for i in range(2):
        generate_BusServicesData_returnsUnsure(i)
        print('done with generate_all_BusServicesRequest_info_jsonfile #'+str(i))
    return

def generate_all_BusRoutesRequest_info_jsonfile():
    for i in range(51):
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
    for i in jsonobjtoload['value']:
        listofbsc.append(i['BusStopCode'])
    return listofbsc

#will comb through the busstops dataset to find busstopcode
def search_jsonobj_busstops_busstopcode_returnslistofbsc(jsonobjtoload):
    listofbsc = []
    for i in jsonobjtoload['value']:
        listofbsc.append(i['BusStopCode'])
    return listofbsc

#find index position of busstopcode from either BusRoutesRequest or BusStopsRequest jsonfiles, return list of index positions containing this busstopcode
def search_jsononj_busstopcodeindexpos_BusRoutesRequestORBusStopsRequest_returnslistofindexpos(jsonobjtoload, busstopcode):
    listofindexpos = []
    for i in jsonobjtoload['value']:
        if(i['BusStopCode']==str(busstopcode)):
            listofindexpos.append(int(i))
        else:
            listofindexpos = None
    return listofindexpos

#find index position of busstopcode from Bus Arrivals, index of Bus Stop 
def search_jsononj_busstopcodeindexpos_BusStopsRequest_returnslistofindexpos(jsonobjtoload, busstopcode):
    indexpos = None
    for i in jsonobjtoload['value']:
        if(i['BusStopCode']==str(busstopcode)):
            #print('Found Index!')
            indexpos = i
            return indexpos
            break
        else:
            #print('Index not in file'+str(i))
            indexpos = None
    return indexpos


#returns Description of Bus Stop (name of stop) from known json obj - BUsStopsRequest
def search_jsonobj_forDesscription_returnsStrDescription(jsonobjtoload, i):
    if(i == None):
        return None

    else:
        for d in jsonobjtoload['value']:
            if(d==i):
                desc = i['Description']
            else:
                pass
        return desc

#returns Direction 1 or 2 of bus stop from known json obj - BusRoutesRequest
def search_jsonobj_forDirection_returnsIntDirection(jsonobjtoload, indexpos):
    direction = jsonobjtoload['value'][indexpos]['Direction']
    return int(direction)

#returns Distance from interchange of bus stop from known json obj - BusRoutesRequest
def search_jsonobj_forDistance_returnsFloatDirection(jsonobjtoload, indexpos):
    Distance = jsonobjtoload['value'][indexpos]['Distance']
    return float(Distance)

#returns Stop sequence from interchange of bus stop from known json obj - BusRoutesRequest
def search_jsonobj_forStopSequence_returnsIntStopSequence(jsonobjtoload, indexpos):
    StopSequence = jsonobjtoload['value'][indexpos]['Distance']
    return int(StopSequence)

# call once to get the Description (name) of Bus Stop
def return_DescriptionforBusStop(busstopcode):
    cont = True
    while(cont==True):
        for j in range(11):
            #print('opening page: '+str(j))
            jsob = open_jsondatafile_returnsjsonobj(j, 4)
            inpos = search_jsononj_busstopcodeindexpos_BusStopsRequest_returnslistofindexpos(jsob, busstopcode)
            desc = search_jsonobj_forDesscription_returnsStrDescription(jsob, inpos)
            if(desc!=None):
                cont = False
                return desc
                
    return desc

#from busstopsrequest
def return_everyBusStop_busstopsrequest():
    listofAllBusStops = []
    for i in range(11):
        jsob = open_jsondatafile_returnsjsonobj(i, 4)
        listofAllBusStops += search_jsonobj_busstops_busstopcode_returnslistofbsc(jsob)

    return listofAllBusStops

#from busroutesrequest --> need to check if there is more busroutes data, appears to be missing info
def return_everyBusStop_busroutesrequest():
    listofAllBusStops=[]
    for i in range(51):
        jsob = open_jsondatafile_returnsjsonobj(i, 3)
        listofAllBusStops += search_jsonobj_busstops_busstopcode_returnslistofbsc(jsob)

    return listofAllBusStops


