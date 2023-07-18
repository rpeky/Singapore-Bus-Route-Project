# import other .py files (for classes/functions)
import BusStopClass
import TravellerClass
import JsonProcessingFunctions
import BusCalculations

#import json

if __name__ == "__main__":
    thisisastop = BusStopClass.Bus_Stop()
    persononbus = TravellerClass.Traveller()
    initialstop = 85039

    persononbus.update_addstopvisited()
    persononbus.update_addstopvisited()
    persononbus.update_addstopvisited()

    stop = persononbus.StopsVisited
    print(stop)
    #apofbusstopinfo = {}


    
