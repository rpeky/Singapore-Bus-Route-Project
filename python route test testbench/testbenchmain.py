# import other .py files (for classes/functions)
import BusStopClass
import TravellerClass
import JsonProcessingFunctions
import BusCalculations
import json

def temp_jsonfile_arrivals():
    f = open('bus_arrivals.json')
    jsonobj = json.loads(f)
    return jsonobj

def temp_jsonfile_route():
    f = open('')
    jsonobj = json.loads(f)
    return jsonobj

def temp_jsonfile_info():
    f = open('')
    jsonobj = json.loads(f)
    return jsonobj

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



def generate_initialBusStopData(thisisastop, initialstop):
    #to add

    #BusStopCode = None     -> initial stop        //done
    #Direction = None       -> bus_route_info           //
    #Distance = None        -> bus_route_info           //
    #StopSequence = None    -> bus_route_info           //
    #IDofBus = None         -> bus_arrivals             //
    #TimesVisited = None    -> 1                        //done
    #Description = None     -> bus_stop_no              //

    initialdata_arrivalsdata = JsonProcessingFunctions.generate_jsonobj_bus_stop_bus_info(initialstop)
    IDofBus = None


    BusStopCode = initialstop 

    
    Description = None

    
    for i in len(initialdata_arrivalsdata["Services"][0]['ServiceNo']):
        IDofBus.apend(initialdata_arrivalsdata['Services'][0]['ServiceNo'])

    TimesVisited = 1


    #bsc, direc, distfromint, seq, busid, visited, desc
    thisisastop.action_obtainvaluesforupdatefnthenaddtomap(BusStopCode, Direction, Distance, StopSequence. IDofBus, TimesVisited, Description)
    print("First stop json data file created, stop added to map")
    return

#will destroy itself when not needed
def create_BusStopobj():
    thisisastop = BusStopClass.Bus_Stop()
    return thisisastop

#will destroy itself when not needed
def create_Travellerobj():
    persononbus = TravellerClass.Traveller()
    return persononbus

#to contain every bus stop  (total stops in sg = )
mapofbusstopinfo = dict()

def convert_mapintojson(maptouse):
    makenewfilename = "mapdata.json"
    with open(makenewfilename, 'w') as outfile:
        json.dump(maptouse, outfile, sort_keys=False, indent=4, ensure_ascii=False)
    print("Map converted")
    return


if __name__ == "__main__":
    
    thisisastop = create_BusStopobj()
    persononbus = create_Travellerobj()
    
    #initialstop = int(input("Enter Initial Stop:\n"))
    initialstop = None #insert test value




