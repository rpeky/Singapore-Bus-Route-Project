import BusStopClass
import TravellerClass
import JsonProcessingFunctions
import DataValidationCheckFunctions
import json
import os
import time

def create_BusStopobj():
    thisisastop = BusStopClass.Bus_Stop()
    return thisisastop

def create_Travellerobj():
    persononbus = TravellerClass.Traveller()
    return persononbus

#def main():
#    starttime=time.process_time()
#    DataValidationCheckFunctions.check_osfolder()



#    print(time.process_time()-starttime)

#if __name__ == "__main__":
#    pass