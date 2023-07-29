import json
import JsonProcessingFunctions

class Traveller():

	"""
	TotalDistanceTravelled = float
	TotalStopsVisited = int
	currentbusno = str
	Stored_Dist = float
	AllStopsVisited = bool
	OnBus = bool
	StopsVisited = list (of stops(int))
	Tracker = list (of strings describing every action)
	"""

	## update functions
	def update_addstopvisited(self):
		self.TotalStopsVisited+=1
		return

	#get dist calculated from bus stop
	def update_TotalDistanceTravelled(self, dist):
		self.TotalDistanceTravelled += dist
		return

	def update_alightbus(self):
		self.OnBus = False
		return

	def update_takebus(self):
		self.OnBus = True
		return

	def update_newbus(self, newbusno):
		self.currentbusno = newbusno
		return

	def update_newstop(self, newstopno):
		self.currentstopno = newstopno
		return

	def update_newstopvisited_addstop(self, bsc):
		self.StopsVisited.append(bsc)
		return

	def update_addactiontotracker(self, action):
		self.Tracker.append(action)
		return

    ## decision functions
	def decision_stayonbus(self):
		pass
	
	def decision_leavebus(self):
		return self.update_alightbus()
	
	def decision_takebus(self):
		return self.update_takebus()

	# need logic to choose bus based on availiable bus - last bus taken
	def decision_choosebus(self):
		if(self.OnBus==True):
			raise ValueError("Not Supposed to be on the bus and choosing a bus! Something went wrong somewhere")
		else:
			pass



	## check functions
	def check_completedallstops(self):
		#known constant total stops is 5082, and dict removes duplicates, so compare number of stops visited to total
		if(len(self.StopsVisited==5082)):
			self.AllStopsVisited = True
		else:
			pass

	def check_onbus_or_onstop(self):
		return self.OnBus

	#returns list of bus in bus stop
	def check_availiablebus_returnslistofbus(self):
		jsob = JsonProcessingFunctions.open_jsondatafile_returnsjsonobj(self.currentstopno, 5)
		return list(jsob['IDofBus'])

	def check_currentstop(self):
		return int(self.StopsVisited[self.TotalStopsVisited])

	## search functions
	
	def __init__(self):
		self.TotalDistanceTravelled = 0
		self.TotalStopsVisited = 0
		self.currentbusno = ""
		self.currentstopno = ""
		self.AllStopsVisited = False
		self.OnBus = False
		self.StopsVisited = []
		self.Tracker = []
		self.Stored_Dist = 0
		print("New Traveller made")

	def __del__(self):
		print("Reached Destructor")
		print("Traveller did it! He visited all the bus stops")
