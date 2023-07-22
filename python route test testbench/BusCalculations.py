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

