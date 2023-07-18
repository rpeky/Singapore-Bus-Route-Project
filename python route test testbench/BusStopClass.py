class Bus_Stop():

    """
    BusStopCode = int 
    Direction = int
    Distance = float
    StopSequence = int
    noofbus = int
    TimesVisited = int
    Description = str

    """
    
    BusStopCode = None 
    Direction = None
    Distance = None
    StopSequence = None
    noofbus = None
    TimesVisited = None
    Description = None

    
    def update_busstopcode(self, bsc):
        self.BusStopCode = bsc

    def update_direction(self, dir):
        self.Direction = dir

    def update_distance(self, distfromint):
        self.Distance = distfromint

    def update_stopsequence(self, seq):
        self.StopSequence = seq

    def update_noofbus(self, busno):
        self.noofbus = busno

    def update_timesvisited(self, visited):
        self.TimesVisited = visited

    def update_description(self, desc):
        self.Description = desc



    def __init__(self, bsc=None, dir=None, distfromint=None, seq=None, busno=None, visited=None, desc=None):
        print("Made a new Bus Stop")




    





