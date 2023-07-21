from fileinput import filename
import json
from tkinter import EXCEPTION
from turtle import update


# to make a new bus stop and store the data in json format if has never been visited
# if visited before, will exist in traveller obj list of visited stops, then access the json file to read/update
class Bus_Stop():

    """
                         //map 0 reserved for checking if exist (legacy) - can just check if element BusStopCode exists in list
    BusStopCode = int    //map 1
    Direction = int      //map 2
    Distance = float     //map 3
    StopSequence = int   //map 4
    IDofBus = list       //map 5
    TimesVisited = int   //map 6
    Description = str    //map 7 - Bus Stop Name


    """
    
    BusStopCode = None 
    Direction = None
    Distance = None
    StopSequence = None
    IDofBus = None
    TimesVisited = None
    Description = None

    ## update functions
    def update_busstopcode(self, bsc):
        self.BusStopCode = int(bsc)

    def update_direction(self, direc):
        self.Direction = int(direc)

    def update_distance(self, distfromint):
        self.Distance = float(distfromint)

    def update_stopsequence(self, seq):
        self.StopSequence = int(seq)

    def update_IDofBus(self, busid):
        self.IDofBus = list(busid)

    #additional visits can be added using the map
    def update_timesvisited(self, visited):
        self.TimesVisited = int(visited)

    def update_description(self, desc):
        self.Description = str(desc)

    #might not need, should be able to directly edit the json file? not sure need finish up the rest first
    #def update_additionalvisit(self, bsc):
    #    pass

    # variables already converted to their proper types in action function before this is called
    def update_addstopdatafile(self):
        if not[x for x in (self.BusStopCode, self.Direction, self.Distance, self.StopSequence, self.IDofBus, self.TimesVisited, self.Description) if x is None]:
            stoptoadd_jsondata = {
            "BusStopCode": self.BusStopCode,
            "Direction": self.Direction,
            "Distance": self.Distance,
            "StopSequence": self.StopSequence,
            "IDofBus": self.IDofBus,
            "TimesVisited": self.TimesVisited,
            "Description": self.Description
            }

            #may need to rename file name to search in future?
            #or make super file
            makenewfilename = str(self.BusStopCode)+"_busstop_data.json"
            with open(makenewfilename, 'w') as outfile:
                json.dump(stoptoadd_jsondata, outfile, sort_keys=False, indent=4, ensure_ascii=False)
            print("Created new stop file "+makenewfilename+"!\n")

        else:
            raise ValueError("Error, Missing Parameter when updating stop to map")
        
    ## action functions

    # action superfunction
    def action_obtainvaluesforupdatefnthenaddtomap(self, bsc, direc, distfromint, seq, busid, visited, desc):
        self.update_busstopcode(bsc)
        self.update_direction(direc)
        self.update_distance(distfromint)
        self.update_stopsequence(seq)
        self.update_noofbus(busid)
        self.update_timesvisited(visited)
        self.update_description(desc)
        self.update_addstopdatafile()
        self.action_clearinternalvalues()
        return

    # clears values to reuse object
    def action_clearinternalvalues(self):
        self.BusStopCode = None
        self.Direction = None
        self.Distance = None
        self.StopSequence = None
        self.noofbus = None
        self.TimesVisited = None
        self.Description = None
        return

    ## initialization and destruction
    def __init__(self, bsc=None, direc=None, distfromint=None, seq=None, busid=None, visited=None, desc=None):
        print("Made a new Bus Stop")

    def __del__(self):
        print("Reached Destructor")
        print("Bus Stop added to map/list/json, deleting this stop, refer to map for values")
