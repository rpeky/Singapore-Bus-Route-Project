class Graph():
    """
    dictadjlist={a:[],b:[],[]...}

    """
    def get_adjlistvalues(self, node, neighbours):
        self.dictadjlist.update({str(node):list(neighbours)})

    def __init__(self):
        self.dictadjlist={}
        print("OwO its a graph")


    def __del__(self):
        print("goodbye graph")




