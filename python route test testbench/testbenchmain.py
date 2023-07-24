# import other .py files (for classes/functions)
from doctest import UnexpectedException
from typing import OrderedDict
import BusStopClass
import TravellerClass
import JsonProcessingFunctions
import BusCalculations
import json
import os.path
#to contain every bus stop  (total stops in sg = )
mapofbusstopinfo = dict()

#will destroy itself when not needed
def create_BusStopobj():
    thisisastop = BusStopClass.Bus_Stop()
    return thisisastop

#will destroy itself when not needed
def create_Travellerobj():
    persononbus = TravellerClass.Traveller()
    return persononbus

#def recurse_openjsondatafile(indexp, identifier, indextoload):
#    pass

def check_ifBusArrivalsData_exist(busstopcode):
    filename = str(busstopcode)+'_BusArrivalRequest_BusStop_data.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'BusArrivalRequest_data')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)

def check_ifProcessedBusStopData_exist(busstopcode):
    filename = str(busstopcode)+'_busstop_data.json'
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'ProcessedBusStopData')
    full_path = os.path.join(newdir, filename)
    return os.path.isfile(full_path)

def generate_BusStopData_processedjson_firstvisit(thisisastop, busstopcode):
    #to add

    #BusStopCode = None     -> initial stop             //done
    #Direction = None       -> bus_route_info           //done
    #Distance = None        -> bus_route_info           //initial distance is zero
    #StopSequence = None    -> bus_route_info           //done
    #IDofBus = None         -> bus_arrivals             //done
    #TimesVisited = None    -> 0                        //done set to zero, increase using traveller obj for first visit
    #Description = None     -> bus_stop_no              //done
    if(check_ifProcessedBusStopData_exist(busstopcode)!=True):

        print(str(busstopcode)+'_busstop_data.json does not exists')

        if(check_ifBusArrivalsData_exist(busstopcode)!=True):
            print(str(busstopcode)+'_BusArrivalRequest_BusStop_data.json does not exists')
            JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(busstopcode)

        BusStopCode = str(busstopcode)
        Direction = JsonProcessingFunctions.return_DirectionforBusStop(busstopcode)
        Distance = JsonProcessingFunctions.return_DistancefromINTforBusStop(busstopcode)
        StopSequence = JsonProcessingFunctions.return_StopSequenceforBusStop(busstopcode)
        IDofBus = JsonProcessingFunctions.return_BusServicesforBusStop(busstopcode)
        TimesVisited = 0
        Description = JsonProcessingFunctions.return_DescriptionforBusStop(busstopcode)

        #bsc, direc, distfromint, seq, busid, visited, desc
        print("First stop json data file created, stop added to map")
        return thisisastop.action_obtainvaluesforupdatefnthenaddtomap(BusStopCode, Direction, Distance, StopSequence, IDofBus, TimesVisited, Description)

    elif(check_ifProcessedBusStopData_exist(busstopcode)!=True):
        print(str(busstopcode)+'_busstop_data.json exists, skip \n')

    else:
        pass
        #raise UnexpectedException("Unexpected Error")

    #generate BusArrivals data of initial stop to get list of bus services if not existing

    



def generate_All_BusStopData_processedjson_firstvisit(busob):
    listofAllBusStops = JsonProcessingFunctions.return_everyBusStop_busroutesrequest()
    for i in sorted(listofAllBusStops):
        print(i)
        generate_BusStopData_processedjson_firstvisit(busob, i)

#probably need to define what maptouse contains?
def convert_mapintojson(maptouse):
    makenewfilename = "workingmapdata.json"
    cwd = os.getcwd()
    newdir = os.path.join(cwd, 'WorkingMapData')
    full_path = os.path.join(newdir, makenewfilename)
    with open(full_path, 'w') as outfile:
        json.dump(maptouse, outfile, sort_keys=False, indent=4, ensure_ascii=False)
    print("Map converted")
    return

import os

#checks if folders exist, edit as more files are needed
def check_osfolder():
    listoffoldersshouldexist = ['BusRoutesRequest_data', 'BusServicesRequest_data', 'BusStopsRequest_data', \
                                'BusArrivalRequest_data', 'ProcessedBusStopData', 'WorkingMapData']
    
    for i in listoffoldersshouldexist:
        if(os.path.isdir(i)):
            pass
        else:
            os.mkdir(i)



if __name__ == "__main__":
    print("Starting")

    #check_osfolder()
    #print("Done making folders")
    #JsonProcessingFunctions.generate_all_BusStopsRequest_info_jsonfile()
    #print("Done generate_all_BusStopsRequest_info_jsonfile")
    #JsonProcessingFunctions.generate_all_BusServicesRequest_info_jsonfile()
    #print("Done generate_all_BusServicesRequest_info_jsonfile")
    #JsonProcessingFunctions.generate_all_BusRoutesRequest_info_jsonfile()
    #print("Done generate_all_BusRoutesRequest_info_jsonfile")
    #JsonProcessingFunctions.generate_all_BusArrivalRequest_info_jsonfile()
    #print("Done generate_all_BusArrivalRequest_info_jsonfile")

    bob = create_BusStopobj()
    generate_All_BusStopData_processedjson_firstvisit(bob)
    #print(sorted(JsonProcessingFunctions.return_everyBusStop_busroutesrequest()))
    print('Done')

    print('Ending')

    
        #testdic = {'a':'test1','b':[1,2,3,4,5],'c':'abcde'}
    #filename = 'testfile.json'
    #cwd = os.getcwd()
    #listoffoldersshouldexist = ['BusRoutesRequest_data', 'BusServicesRequest_data', 'BusStopsRequest_data', \
    #                            'BusArrivalRequest_data', 'ProcessedBusStopData']
    #newdir = os.path.join(cwd,'ProcessedBusStopData')
    #full_path = os.path.join(newdir, filename)
    #with open(full_path, 'w') as outfile:
    #    json.dump(testdic, outfile, sort_keys=True, indent=4, ensure_ascii=False)
    
    #JsonProcessingFunctions.generate_all_BusStopsRequest_info_jsonfile()
    #JsonProcessingFunctions.generate_all_BusServicesRequest_info_jsonfile()
    #JsonProcessingFunctions.generate_all_BusRoutesRequest_info_jsonfile()
    #listofstopsallstops = JsonProcessingFunctions.return_everyBusStop_busstopsrequest()
    #for i in listofstopsallstops:
    #    print('Creating BusArrivalData' + i)
    #    JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(i)



    #JsonProcessingFunctions.generate_all_BusStopsRequest_info_jsonfile()
    #JsonProcessingFunctions.generate_all_BusServicesRequest_info_jsonfile()
    #JsonProcessingFunctions.generate_all_BusRoutesRequest_info_jsonfile()

    #listofstopsallstops = JsonProcessingFunctions.return_everyBusStop_busstopsrequest()
    #print(sorted(listofstopsallstops))
    #print(len(listofstopsallstops))

    #listofstopsallstops2 = JsonProcessingFunctions.return_everyBusStop_busroutesrequest()
    #print(sorted(listofstopsallstops2))
    #print(len(listofstopsallstops2))
    #print(JsonProcessingFunctions.return_DescriptionforBusStop(85039))
    #print(JsonProcessingFunctions.return_DirectionforBusStop(85039))
    #print(JsonProcessingFunctions.return_StopSequenceforBusStop(85039))
    #JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(85049)
    #JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(85059)
    #JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(85019)
    #JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(85029)
    #JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(85091)
    #tob = create_Travellerobj()
    #bob = create_BusStopobj()
    #generate_BusStopData_processedjson(bob, 85039)
    #generate_BusStopData_processedjson(bob, 85049)
    #generate_BusStopData_processedjson(bob, 85059)
    #generate_BusStopData_processedjson(bob, 85019) 
    #generate_BusStopData_processedjson(bob, 85029)
    #generate_BusStopData_processedjson(bob, 85091)

    #print(type(JsonProcessingFunctions.open_jsondatafile_returnsjsonobj(85091 , 5)))

    #print(JsonProcessingFunctions.return_BusServicesforBusStop(85039))
