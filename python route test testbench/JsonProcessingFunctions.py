import json
from poplib import POP3
import urllib
import urllib.request
from urllib.parse import urlparse
import httplib2 as http 
import os
from collections import OrderedDict
from multiprocessing import Process

#Functions to generate Bus Stop data
# Stuff to obtain
    #BusStopCode = str    //map 1 changed to string beacuse int cant start with 0 error
    #Direction = int      //map 2
    #Distance = float     //map 3
    #StopSequence = int   //map 4
    #IDofBus = list       //map 5
    #TimesVisited = int   //map 6
    #Description = str    //map 7 - Bus Stop Name

#to blank out in final commit(?) not sure if its against user agreement if its on github
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
    #create file to read in future in BusArrivalRequest folder
    filename = str(BusStopCode)+"_BusArrivalRequest_BusStop_data.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusArrivalRequest_data')
    full_path = os.path.join(newdir, filename)
    with open(full_path, "w") as outfile:
        json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

##API 2.2 Bus Services Request
#can use to find home interchange and destination for specific bus
def generate_BusServicesData_returnsStopJsonData(skips):
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
        filename = "0_BusServicesRequest_data.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'BusServicesRequest_data')
        full_path = os.path.join(newdir, filename)
        with open(full_path, "w") as outfile:
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
        filename = str(skips)+"_BusServicesRequest_data.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'BusServicesRequest_data')
        full_path = os.path.join(newdir, filename)
        with open(full_path, "w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

##API 2.3 Bus Routes Request
def generate_BusRoutesData_returnsStopJsonData(skips):
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
        filename = "0_BusRoutesRequest_data.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'BusRoutesRequest_data')
        full_path = os.path.join(newdir, filename)
        with open(full_path, "w") as outfile:
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
        filename = str(skips)+"_BusRoutesRequest_data.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'BusRoutesRequest_data')
        full_path = os.path.join(newdir, filename)
        with open(full_path, "w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)

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
        filename = "0_BusStopsRequest_bus_stop_info.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'BusStopsRequest_data')
        full_path = os.path.join(newdir, filename)

        with open(full_path, "w") as outfile:
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
        filename = str(skips)+"_BusStopsRequest_bus_stop_info.json"
        cwd = os.getcwd()
        newdir = os.path.join(cwd, 'BusStopsRequest_data')
        full_path = os.path.join(newdir, filename)
        with open(full_path, "w") as outfile:
            json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)


#generates all needed files, run at start to update
def generate_all_BusStopsRequest_info_jsonfile():
    for i in range(11):
        generate_BusStopsRequest_togetallbusstop(i)
    return

def generate_all_BusServicesRequest_info_jsonfile():
    for i in range(2):
        generate_BusServicesData_returnsStopJsonData(i)
    return

def generate_all_BusRoutesRequest_info_jsonfile():
    for i in range(51):
        generate_BusRoutesData_returnsStopJsonData(i)
    return

def generate_all_BusArrivalRequest_info_jsonfile():
    listofstopsallstops = return_everyBusStop_busstopsrequest()
    for i in listofstopsallstops:
        generate_BusArrivalData_returnsBusServiceID(i)
    return

def generate_allfourAPIrequestdata_intojsonfile():
    p1=Process(target=generate_all_BusStopsRequest_info_jsonfile())
    p2=Process(target=generate_all_BusServicesRequest_info_jsonfile())
    p3=Process(target=generate_all_BusRoutesRequest_info_jsonfile())
    p4=Process(target=generate_all_BusArrivalRequest_info_jsonfile())

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    return


def generate_individualbusroute_fromProcessedData():
    pass

#loads json obj from json file
    #filetypes expect identifier, followed by int of suffix needed

    #_subject_          _index_                                                             _file name template_                            _folder name_               _additional comments_
    #error              - 0 unexpected error // for matching api index with load index      errorindex                                      errorindex  
    
    ## API data

    #arrivals           - 1 API 2.1 Bus Arrival Request                                     _BusArrivalRequest_BusStop_data.json            BusArrivalRequest_data      
    #services           - 2 API 2.2 Bus Services Request                                    _BusServicesRequest_data.json                   BusServicesRequest_data
    #routes             - 3 API 2.3 Bus Routes Request                                      _BusRoutesRequest_data.json                     BusRoutesRequest_data
    #stops              - 4 API 2.4 Bus Stops Request                                       _BusStopsRequest_bus_stop_info.json             BusStopsRequest_data
    
    ## Processed / self made data
    #composite          - 5 Bus Stop Data generated from processing API data                _busstop_data.json                              ProcessedBusStopData
    #mapdata            - 6 Working Map Data Traveller will use                             _workingmapdata.json                             WorkingMapData              Identifier will take in None            
    #indvbusroute       - 7 Individual route each bus takes                                 _busserviceroute.json                           ProcessedServiceRouteData   

#to update whenever new folders/files are added
def open_jsondatafile_returnsjsonobj(identifier, indextoload):
    jsondatafilenamingsuffix = [\
                                'errorindex', \
                                '_BusArrivalRequest_BusStop_data.json', \
                                '_BusServicesRequest_data.json', \
                                '_BusRoutesRequest_data.json', \
                                '_BusStopsRequest_bus_stop_info.json', \
                                '_busstop_data.json', \
                                '_workingmapdata.json',\
                                '_busserviceroute.json'\
                                ]
    listoffoldersshouldexist = [\
                                'errorindex', \
                                'BusArrivalRequest_data', \
                                'BusServicesRequest_data', \
                                'BusRoutesRequest_data', \
                                'BusStopsRequest_data', \
                                'ProcessedBusStopData', \
                                'WorkingMapData',\
                                'ProcessedServiceRouteData'\
                                 ]
    filename = str(identifier)+str(jsondatafilenamingsuffix[int(indextoload)])
    cwd = os.getcwd()
    newdir = os.path.join(cwd, listoffoldersshouldexist[int(indextoload)])
    full_path = os.path.join(newdir, filename)
    f = open(full_path)
    jsonobj = json.load(f)
    return jsonobj


##Search functions
#Works, able to obtain Bus ID (Services) from Bus Stop
def search_jsonobj_busstop_busidinstop_returnslistofid(jsonobjtoload):
    listofbusid = []
    for i in jsonobjtoload['Services']:
        listofbusid.append(i['ServiceNo'])
    return listofbusid

#will comb through the \busroutes\ dataset to find busstopcode
def search_jsonobj_busroutes_busstopcode_returnslistofbsc(jsonobjtoload):
    listofbsc = []
    for i in jsonobjtoload['value']:
        listofbsc.append(i['BusStopCode'])
    return listofbsc

#will comb through the /busstops/ dataset to find busstopcode
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
def search_jsononj_busstopcodeindexpos_BusStopsRequest_returnsindexpos(jsonobjtoload, busstopcode):
    indexpos = None
    for i in jsonobjtoload['value']:
        if(i['BusStopCode']==str(busstopcode)):
            #print('Found Index!')
            indexpos = i
            return indexpos
        else:
            #print('Index not in file'+str(i))
            indexpos = None
    return indexpos

#search and returns Description of Bus Stop (name of stop) from known json obj - BusStopsRequest
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

#search and returns Direction 1 or 2 of bus stop from known json obj - BusRoutesRequest
def search_jsonobj_forDirection_returnsIntDirection(jsonobjtoload, i):
    if(i == None):
        return None

    else:
        for d in jsonobjtoload['value']:
            if(d==i):
                direc = i['Direction']
                #print('found direction')
            else:
                pass
        return direc

#search and returns Stop Sequence of bus stop from known json obj - BusRoutesRequest
def search_jsonobj_forStopSequence_returnsIntStopSequence(jsonobjtoload, i):
    if(i == None):
        return None

    else:
        for d in jsonobjtoload['value']:
            if(d==i):
                sseq = i['StopSequence']
                #print('found stop sequence')
            else:
                pass
        return int(sseq)

#search and returns Distanceof bus stop from known json obj - BusRoutesRequest
def search_jsonobj_forDistance_returnsFloatDistance(jsonobjtoload, i):
    if(i == None):
        return None

    else:
        for d in jsonobjtoload['value']:
            if(d==i):
                dist = i['Distance']
                #print('found distance')
            else:
                pass
        return dist

# super return, call once to get the Description (name) of Bus Stop
def return_DescriptionforBusStop(busstopcode):
    for j in range(11):
        #print('opening page: '+str(j))
        jsob = open_jsondatafile_returnsjsonobj(j, 4)
        inpos = search_jsononj_busstopcodeindexpos_BusStopsRequest_returnsindexpos(jsob, busstopcode)  
        if(inpos!=None):
            desc = search_jsonobj_forDesscription_returnsStrDescription(jsob, inpos)
            return desc
    
# super return, call once to get Bus Services (IDofBus) of Bus Stop
def return_BusServicesforBusStop(busstopcode):
    jsob = open_jsondatafile_returnsjsonobj(busstopcode, 1)
    return search_jsonobj_busstop_busidinstop_returnslistofid(jsob)

# super return, call once to get Direction (1 or 2) of Bus Stop
def return_DirectionforBusStop(busstopcode):
    for i in range(51):
        #print('going through file '+str(i))
        jsob = open_jsondatafile_returnsjsonobj(i, 3)
        inpos = search_jsononj_busstopcodeindexpos_BusStopsRequest_returnsindexpos(jsob, busstopcode)        
        if(inpos!=None):
            direc = search_jsonobj_forDirection_returnsIntDirection(jsob, inpos)
            return direc

# super return, call once to get Stop Sequence of Bus Stop
def return_StopSequenceforBusStop(busstopcode):
    for i in range(51):
        #print('going through file '+str(i))
        jsob = open_jsondatafile_returnsjsonobj(i, 3)
        inpos = search_jsononj_busstopcodeindexpos_BusStopsRequest_returnsindexpos(jsob, busstopcode)        
        if(inpos!=None):
            sseq = search_jsonobj_forStopSequence_returnsIntStopSequence(jsob, inpos)
            return sseq

# super return, call once to get Distance from interchange of Bus Stop
def return_DistancefromINTforBusStop(busstopcode):
    for i in range(51):
        #print('going through file '+str(i))
        jsob = open_jsondatafile_returnsjsonobj(i, 3)
        inpos = search_jsononj_busstopcodeindexpos_BusStopsRequest_returnsindexpos(jsob, busstopcode)        
        if(inpos!=None):
            dst = search_jsonobj_forDistance_returnsFloatDistance(jsob, inpos)
            return dst

#both return_everyBusStop_busstopsrequest and return_everyBusStop_busroutesrequest
#from busstopsrequest
def return_everyBusStop_busstopsrequest():
    listofAllBusStops = []
    for i in range(11):
        jsob = open_jsondatafile_returnsjsonobj(i, 4)
        listofAllBusStops += search_jsonobj_busstops_busstopcode_returnslistofbsc(jsob)

    fixedlist = list(OrderedDict.fromkeys(listofAllBusStops))

    return list(fixedlist)

#from busroutesrequest #equivalent means 5083 bus stops total
def return_everyBusStop_busroutesrequest():
    listofAllBusStops=[]
    for i in range(51):
        jsob = open_jsondatafile_returnsjsonobj(i, 3)
        listofAllBusStops += search_jsonobj_busstops_busstopcode_returnslistofbsc(jsob)

    fixedlist = list(OrderedDict.fromkeys(listofAllBusStops))

    return list(fixedlist)

# returns list of serviceno from json obj
def search_jsonobj_busservices_serviceno_returnslistofserviceno(jsonobjtoload):
    listofbusid = []
    for i in jsonobjtoload['value']:
        listofbusid.append(i['ServiceNo'])
    return listofbusid

#from busservicesrequest, returns all bus service no
def return_everybusserviceno_givesalist():
    listofAllBusServices=[]
    for _ in range(2):
        jsob=open_jsondatafile_returnsjsonobj(_,2)
        listofAllBusServices+=search_jsonobj_busservices_serviceno_returnslistofserviceno(jsob)
    return sorted(list(set(listofAllBusServices)))

#search from busroutesrequest
def findpagesthisbusisin(busno):
    pgs=[]
    for _ in range(51):
        jsob=open_jsondatafile_returnsjsonobj(_,3)
        for i in jsob['value']:
            if(i['ServiceNo']==str(busno)):
                pgs.append(_)
                break
            else:
                pass    
    return pgs

#will return 2 set of routes, int 1 to int 2 then int 2 to int 1, combine to form one interchange loop if possible (general case, need check if theres bus that dosent follow this)
def generate_individualroutesforbus_frombusroutesrequest(busserviceno):
    routelist1=[]
    routelist2=[]
    pgs=findpagesthisbusisin(busserviceno)
    
    #checkwhich direction exists
    route1exist,route2exist=False,False
    for _ in range(2):
        jsob=open_jsondatafile_returnsjsonobj(_,2)
        for i in jsob['value']:
            if(i['ServiceNo']==busserviceno and i['Direction']==1):
                route1exist=True
            if(i['ServiceNo']==busserviceno and i['Direction']==1):
                route2exist=True
    if(route1exist==True):
        for pgno in pgs:
            jsob=open_jsondatafile_returnsjsonobj(pgno,3)
            for i in jsob['value']:
                if(i['Direction']==1 and i['ServiceNo']==busserviceno):
                    routelist1.append(i['BusStopCode'])
                else:
                    pass   
    if(route2exist==True):
        for pgno in pgs:
            jsob=open_jsondatafile_returnsjsonobj(pgno,3)
            for i in jsob['value']:
                if(i['Direction']==2 and i['ServiceNo']==busserviceno):
                    routelist2.append(i['BusStopCode'])
                else:
                    pass 
    combinedroute=[routelist1,routelist2]
    filename = busserviceno+"_busserviceroute.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'ProcessedServiceRouteData')
    full_path = os.path.join(newdir, filename)
    with open(full_path, "w") as outfile:
        json.dump(combinedroute, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return


def generate_AllRoutesforEveryBus_returnsjsonfile():
    busserviceslist=return_everybusserviceno_givesalist()
    for bus in busserviceslist:
        generate_individualroutesforbus_frombusroutesrequest(str(bus))
    return

def generate_Neighbour_returnslistofneighbours(busstopcode):

    if(busstopcode=='59008'):
        neighbours.append('59008')
        return neighbours

    neighbours=[]
    busstopinfo=return_BusServicesforBusStop(busstopcode)



    print(busstopcode)
    for bus in busstopinfo:
        #skip if bus number=75A because depreciated, should not be included in 12109 bus stop arrival data
        if(bus=='75A'):
            continue
        else:
            #route info can contain 1 set, 1 compliment set or 2 sets of list
            routeinfo=open_jsondatafile_returnsjsonobj(bus, 7)
            #check which list active, if one in use easiest case, remove last stop because points to nowhere)
            l1active = True if (len(routeinfo[0])>0 and routeinfo[0][-1]!=busstopcode and busstopcode in routeinfo[0])else False
            l2active = True if (len(routeinfo[1])>0 and routeinfo[1][-1]!=busstopcode and busstopcode in routeinfo[1])else False
            #check which list in use since every stop other than interchange is in either one of list (diected or loop)
            if(l1active):
                adjstopindex = int(routeinfo[0].index(busstopcode)) + 1
                neighbours.append(routeinfo[0][adjstopindex])
            if(l2active):
                adjstopindex = int(routeinfo[1].index(busstopcode)) + 1
                neighbours.append(routeinfo[1][adjstopindex])  
    #remove duplicates
    return list(set(neighbours))

def generate_Adjacencylistforallbusstop_returnsdictofneighbours_returnsjsonofsuperadjlist():
    listofAllBusStops = return_everyBusStop_busstopsrequest()
    superdictadjlist={}
    for busstop in listofAllBusStops:
        if(busstop == '59008'):
            neighbourlist=generate_Neighbour_returnslistofneighbours(busstop)
            dfromint=return_DistancefromINTforBusStop(busstop)
            superdictadjlist[busstop]={\
                'neighbours': '59091',\
                'distfromint': dfromint, \
                'timesvisited': 0
                }
            
        else:
            neighbourlist=generate_Neighbour_returnslistofneighbours(busstop)
            dfromint=return_DistancefromINTforBusStop(busstop)
            superdictadjlist[busstop]={\
                'neighbours': neighbourlist,\
                'distfromint': dfromint, \
                'timesvisited': 0
                }
    filename = "MC_Noneworkingmapdata.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'WorkingMapData')
    full_path = os.path.join(newdir, filename)
    with open(full_path, "w") as outfile:
        json.dump(superdictadjlist, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    return 


#def mergedict(d1,d2):
#    res ={**d1,**d2}
#    return dict(res)

#def generate_SuperBusStopDataGraphDatabase():
#    listofAllBusStops = return_everyBusStop_busstopsrequest()
#    superdatabasedict={}
#    print(listofAllBusStops)
#    for i, busstop in enumerate(listofAllBusStops):

#        print('---------------------------------------------------')
#        if(i==0):
#            jsobdictstop=dict(open_jsondatafile_returnsjsonobj(busstop,5))
#            superdatabasedict = jsobdictstop.copy()
#            print(superdatabasedict)
#            print('+++++++++++++++++++++++++++++++++++++++')
#        else:
#            jsobdictstop=dict(open_jsondatafile_returnsjsonobj(busstop,5))
#            tempdict=mergedict(superdatabasedict,jsobdictstop)
#            print(superdatabasedict)
#            print('+++++++++++++++++++++++++++++++++++++++')
#            superdatabasedict = tempdict
#            print(superdatabasedict)
#            print('+++++++++++++++++++++++++++++++++++++++')

#    filename = "superdatadict.json"
#    cwd = os.getcwd()
#    newdir = os.path.join(cwd, 'WorkingMapData')
#    full_path = os.path.join(newdir, filename)
#    with open(full_path, "w") as outfile:
#        json.dump(superdatabasedict, outfile, sort_keys=True, indent=4, ensure_ascii=False)

#    return 