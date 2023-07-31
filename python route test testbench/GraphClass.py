import JsonProcessingFunctions

class Graph():
    # dictadjlist can take from super json file with all adj list
    def __init__(self):
        self.dictadjlist=JsonProcessingFunctions.open_jsondatafile_returnsjsonobj(None,6)
        self.numstops=5083
        self.visited = set()
        self.tour=[]
        print("OwO its a graph")

    def searchtilltheendoftime(self, startstop):
        currstop = startstop
        self.tour.append(currstop)
        self.visited.add(currstop)

        while len(self.visited) < self.numstops:
            #neareststop=None
            #smallestdist=float('inf')
            ##need add condition to backtrack if fail, currently goes in one circle for 85039
            #for neighbour in self.dictadjlist[currstop]["neighbours"]:
            #    if(neighbour not in self.visited):
            #        distbetstops=self.get_distancebetweenstop(currstop,neighbour)
            #        if(distbetstops<smallestdist):
            #            neareststop=neighbour
            #            smallestdist=distbetstops
            #currstop=neareststop
            self.tour.append(currstop)
            self.visited.add(currstop)
        
        self.tour.append(startstop)


    def get_distancebetweenstop(self, busstopnode, searchstop):
        dist = self.dictadjlist[searchstop]["distfromint"]-self.dictadjlist[busstopnode]["distfromint"]
        return dist

    def get_tour(self):
        return self.tour

    def __del__(self):
        print("goodbye graph")




