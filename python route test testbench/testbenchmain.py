# import other .py files (for classes/functions)
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
    return os.path.isfile(str(busstopcode)+'_BusArrivalRequest_BusStop_data.json')


def generate_BusStopData_processedjson(thisisastop, initialstop):
    #to add

    #BusStopCode = None     -> initial stop             //done
    #Direction = None       -> bus_route_info           //
    #Distance = None        -> bus_route_info           //initial distance is zero
    #StopSequence = None    -> bus_route_info           //
    #IDofBus = None         -> bus_arrivals             //done
    #TimesVisited = None    -> 1                        //done
    #Description = None     -> bus_stop_no              //

    #generate BusArrivals data of initial stop to get list of bus services if not existing
    if(check_ifBusArrivalsData_exist(initialstop)!=True):
        JsonProcessingFunctions.generate_BusArrivalData_returnsBusServiceID(initialstop)
    
    #BusArrivalsjsondata = JsonProcessingFunctions.open_jsondatafile_returnsjsonobj(initialstop, 1)


    BusStopCode = initialstop 
    Direction = JsonProcessingFunctions.return_DirectionforBusStop(initialstop)
    Distance = JsonProcessingFunctions.return_DistancefromINTforBusStop(initialstop)
    StopSequence = JsonProcessingFunctions.return_StopSequenceforBusStop(initialstop)
    IDofBus = JsonProcessingFunctions.return_BusServicesforBusStop(initialstop)
    TimesVisited = 1
    Description = JsonProcessingFunctions.return_DescriptionforBusStop(initialstop)

    #bsc, direc, distfromint, seq, busid, visited, desc
    print("First stop json data file created, stop added to map")
    return thisisastop.action_obtainvaluesforupdatefnthenaddtomap(BusStopCode, Direction, Distance, StopSequence, IDofBus, TimesVisited, Description)


#probably need to define what maptouse contains?
def convert_mapintojson(maptouse):
    makenewfilename = "mapdata.json"
    with open(makenewfilename, 'w') as outfile:
        json.dump(maptouse, outfile, sort_keys=False, indent=4, ensure_ascii=False)
    print("Map converted")
    return

import os

#checks if folders exist, edit as more files are needed
def check_osfolder():
    listoffoldersshouldexist = ['BusRoutesRequest_data', 'BusServicesRequest_data', 'BusStopsRequest_data', \
                                'BusArrivalRequest_data', 'ProcessedBusStopData']
    
    for i in listoffoldersshouldexist:
        if(os.path.isdir(i)):
            pass
        else:
            os.mkdir(i)



if __name__ == "__main__":
    print("Starting")

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





    print('Ending')

    




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
