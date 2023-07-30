# import other .py files (for classes/functions)
import BusStopClass
import TravellerClass
import JsonProcessingFunctions
import BusCalculations
import json
import os
import time
from multiprocessing import Process

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
    #BusStopCode = None     -> initial stop             //done
    #Direction = None       -> bus_route_info           //done
    #Distance = None        -> bus_route_info           //done initial distance is zero
    #StopSequence = None    -> bus_route_info           //done
    #IDofBus = None         -> bus_arrivals             //done
    #TimesVisited = None    -> 0                        //done set to zero, increase using traveller obj for first visit
    #Description = None     -> bus_stop_no              //done
    #Neighbour = None       -> to make bus route list to find adjacent stops
    if(check_ifProcessedBusStopData_exist(busstopcode)!=True):

        #print(str(busstopcode)+'_busstop_data.json does not exists')

        if(check_ifBusArrivalsData_exist(busstopcode)!=True):
            #print(str(busstopcode)+'_BusArrivalRequest_BusStop_data.json does not exists')
            JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(busstopcode)

        BusStopCode = str(busstopcode)
        Direction = JsonProcessingFunctions.return_DirectionforBusStop(busstopcode)
        Distance = JsonProcessingFunctions.return_DistancefromINTforBusStop(busstopcode)
        StopSequence = JsonProcessingFunctions.return_StopSequenceforBusStop(busstopcode)
        IDofBus = JsonProcessingFunctions.return_BusServicesforBusStop(busstopcode)
        TimesVisited = 0
        Description = JsonProcessingFunctions.return_DescriptionforBusStop(busstopcode)
        Neighbour = JsonProcessingFunctions.generate_Neighbour_returnslistofneighbours(busstopcode)

        #bsc, direc, distfromint, seq, busid, visited, desc
        #print("First stop json data file created, stop added to map")
        return thisisastop.action_obtainvaluesforupdatefnthenaddtomap(BusStopCode, Direction, Distance, StopSequence, IDofBus, TimesVisited, Description, Neighbour)

    elif(check_ifProcessedBusStopData_exist(busstopcode)!=True):
        print(str(busstopcode)+'_busstop_data.json exists, skip \n')

    else:
        pass
        #raise UnexpectedException("Unexpected Error")

    #generate BusArrivals data of initial stop to get list of bus services if not existing

def generate_All_BusStopData_processedjson_firstvisit(busob):
    listofAllBusStops = JsonProcessingFunctions.return_everyBusStop_busroutesrequest()
    for i in sorted(listofAllBusStops):
        generate_BusStopData_processedjson_firstvisit(busob, i)
    return

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

def update_BusStopDataAdjstoplist_neighbour():
    pass

#checks if folders exist, edit as more files are needed
def check_osfolder():
    listoffoldersshouldexist = ['BusRoutesRequest_data', 'BusServicesRequest_data', 'BusStopsRequest_data', \
                                'BusArrivalRequest_data', 'ProcessedBusStopData', 'WorkingMapData', \
                                'ProcessedServiceRouteData']
    
    for i in listoffoldersshouldexist:
        if(os.path.isdir(i)):
            pass
        else:
            os.mkdir(i)

if __name__ == "__main__":
    starttime=time.process_time()
    print("Starting")

    check_osfolder()
    print('checked folder')
    bob=create_BusStopobj()
    generate_All_BusStopData_processedjson_firstvisit(bob)
    #print(JsonProcessingFunctions.findpagesthisbusisin('75A'))
    #print(JsonProcessingFunctions.return_everybusserviceno_givesalist())
    #print(JsonProcessingFunctions.return_BusServicesforBusStop('12109'))
    print('Ending')
    print(time.process_time()-starttime)

    

