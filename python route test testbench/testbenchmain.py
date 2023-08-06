# import other .py files (for classes/functions)
import BusStopClass
import TravellerClass
import JsonProcessingFunctions
#import BusCalculations
import DataValidationCheckFunctions
import json
import os
import time
#from multiprocessing import Process
#import GraphClass

#to contain every bus stop  (total stops in sg = )
#mapofbusstopinfo = dict()

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
    #Neighbour = None       -> _busserviceroute        //done
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


if __name__ == "__main__":
    starttime=time.process_time()
    print("Starting")
    JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(95161)
    #JsonProcessingFunctions.generate_allfourAPIrequestdata_intojsonfile()
    #tob=create_Travellerobj()
    #tob.searchtillendoftime_v2('85039')
    #tob.searchtillendoftime_v1('85039')
    #print(tob.gettour())
    #print(len(tob.gettour()))
    #print(tob.getsetvisited())
    #print(len(tob.getsetvisited()))
    #print(tob.superset)
    #JsonProcessingFunctions.generate_BusRoutesData_returnsStopJsonData_testv2(10)
    #JsonProcessingFunctions.generate_Adjacencylistforallbusstop_returnsdictofneighbours_returnsjsonofsuperadjlist()
    #DataValidationCheckFunctions.check_osfolder()
    #startstop=str(85091)
    #print(startstop)
    #graph=GraphClass.Graph()
    #graph.searchtilltheendoftime(startstop)
    #print('tour: ', graph.get_tour())
    #graph=GraphClass.Graph()
    #print(graph.returndir())
    #l1=['99999','92365','24242','48484']
    #l2=[0,1,1,0]
    #l3=[1.3,2.2,5.7,0.2]
    #a=min(zip(l2,l3,l1))
    #print(a[2])

    print(time.process_time()-starttime)

    

