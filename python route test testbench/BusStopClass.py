from fileinput import filename
import json


# to make a new bus stop and store the data in json format if has never been visited
# if visited before, will exist in traveller obj list of visited stops, then access the json file to read/update
class Bus_Stop():

    """
    BusStopCode = int    //map 1
    Direction = int      //map 2
    Distance = float     //map 3
    StopSequence = int   //map 4
    noofbus = int        //map 5
    TimesVisited = int   //map 6
    Description = str    //map 7 - Bus Stop Name

    """
    
    BusStopCode = None 
    Direction = None
    Distance = None
    StopSequence = None
    noofbus = None
    TimesVisited = None
    Description = None

    # update functions
    def update_busstopcode(self, bsc):
        self.BusStopCode = int(bsc)

    def update_direction(self, direc):
        self.Direction = int(direc)

    def update_distance(self, distfromint):
        self.Distance = float(distfromint)

    def update_stopsequence(self, seq):
        self.StopSequence = int(seq)

    def update_noofbus(self, busno):
        self.noofbus = int(busno)

    def update_timesvisited(self, visited):
        self.TimesVisited = int(visited)

    def update_description(self, desc):
        self.Description = str(desc)

    def update_additionalvisit(self, bsc):
        pass

    def update_addstoptomap(self):
        if not[x for x in (self.BusStopCode, self.Direction, self.Distance, self.StopSequence, self.noofbus, self.TimesVisited, self.Description) if x is None]:
            stoptoadd_jsondata = {
            "BusStopCode": self.BusStopCode,
            "Direction": self.Direction,
            "Distance": self.Distance,
            "StopSequence": self.StopSequence,
            "noofbus": self.noofbus,
            "TimesVisited": self.TimesVisited,
            "Description": self.Description
            }
            makenewfilename = "busstop_"+self.BusStopCode+"_data.json"
            with open(makenewfilename, 'w') as outfile:
                json.dump(stoptoadd_jsondata, outfile, sort_keys=False, indent=4, ensure_ascii=False)
            print("Created new stop file "+makenewfilename+"!\n")

        else:
            print("Error, Missing Parameter when updating stop to map")
        

    def __init__(self, bsc=None, direc=None, distfromint=None, seq=None, busno=None, visited=None, desc=None):
        print("Made a new Bus Stop")

    def __del__(self):
        print("Reached Destructor")
        print("Bus Stop added to map/list/json, deleting this stop, refer to map for values")




    





