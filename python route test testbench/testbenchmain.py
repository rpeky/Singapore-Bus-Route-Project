# import other .py files (for classes/functions)
import BusStopClass
import TravellerClass
import JsonProcessingFunctions
import BusCalculations
import json

#def find_busstop_from_route(stop):
#    #go through every route_info file until BusStopCode matches stop, return index, 
#    indexpos
#    return indexpos

#def find_busstop_from_info(stop):
#    #go through every route_info file until BusStopCode matches stop, return index, 
#    indexpos
#    return indexpos

#def find_busstop_from_route(stop):
#    #go through every route_info file until BusStopCode matches stop, return index, 
#    indexpos
#    return indexpos

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

def recurse_openjsondatafile(indexp, identifier, indextoload):
    pass


def generate_initialBusStopData(thisisastop, initialstop):
    #to add

    #BusStopCode = None     -> initial stop             //done
    #Direction = None       -> bus_route_info           //
    #Distance = None        -> bus_route_info           //initial distance is zero
    #StopSequence = None    -> bus_route_info           //
    #IDofBus = None         -> bus_arrivals             //done
    #TimesVisited = None    -> 1                        //done
    #Description = None     -> bus_stop_no              //

    #generate BusArrivals data of initial stop to get list of bus services 
    JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(initialstop)
    BusArrivalsjsondata = JsonProcessingFunctions.open_jsondatafile_returnsjsonobj(initialstop, 1)


    BusStopCode = initialstop 
    Direction = None
    Distance = 0.0
    StopSequence = None
    IDofBus = None
    TimesVisited = 1
    Description = JsonProcessingFunctions.return_DescriptionforBusStop(initialstop)

    #bsc, direc, distfromint, seq, busid, visited, desc
    thisisastop.action_obtainvaluesforupdatefnthenaddtomap(BusStopCode, Direction, Distance, StopSequence. IDofBus, TimesVisited, Description)
    print("First stop json data file created, stop added to map")
    return

#probably need to define what maptouse contains?
def convert_mapintojson(maptouse):
    makenewfilename = "mapdata.json"
    with open(makenewfilename, 'w') as outfile:
        json.dump(maptouse, outfile, sort_keys=False, indent=4, ensure_ascii=False)
    print("Map converted")
    return

# import os

if __name__ == "__main__":
    print("Starting")

    JsonProcessingFunctions.generate_all_BusStopsRequest_info_jsonfile()
    JsonProcessingFunctions.generate_all_BusServicesRequest_info_jsonfile()
    JsonProcessingFunctions.generate_all_BusRoutesRequest_info_jsonfile()

    listofstopsallstops = JsonProcessingFunctions.return_everyBusStop_busstopsrequest()
    print(listofstopsallstops)
    print(len(listofstopsallstops))

    listofstopsallstops2 = JsonProcessingFunctions.return_everyBusStop_busroutesrequest()
    print(listofstopsallstops2)
    print(len(listofstopsallstops2))

    print('Ending')





    

