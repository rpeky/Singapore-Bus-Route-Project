import BusStopClass
import TravellerClass
import JsonProcessingFunctions
import BusCalculations
import json
import os.path

def create_BusStopobj():
    thisisastop = BusStopClass.Bus_Stop()
    return thisisastop

def create_Travellerobj():
    persononbus = TravellerClass.Traveller()
    return persononbus

def check_ifBusArrivalsData_exist(busstopcode):
    return os.path.isfile(str(busstopcode)+'_BusArrivalRequest_BusStop_data.json')

#checks if folders exist, edit as more files are needed
def check_osfolder():
    listoffoldersshouldexist = ['BusRoutesRequest_data', 'BusServicesRequest_data', 'BusStopsRequest_data', \
                                'BusArrivalRequest_data', 'ProcessedBusStopData']
    
    for i in listoffoldersshouldexist:
        if(os.path.isdir(i)):
            pass
        else:
            os.mkdir(i)