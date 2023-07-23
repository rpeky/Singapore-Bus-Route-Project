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

	TotalDistanceTravelled = 0
	TotalStopsVisited = 0
	currentbusno = ""
	currentstopno = ""
	#Stored_Dist = 0
	AllStopsVisited = False
	OnBus = False
	StopsVisited = []
	#tracker is for me to print to follow the actions irl - will track every action
	Tracker = []



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

	#can take from 
	def check_availiablebus(self):
		pass

	def check_currentstop(self):
		return int(self.StopsVisited[self.TotalStopsVisited])

	## search functions
	





	def __init__(self, TotalDistanceTravelled = 0, StopsVisited = 0, currentbusno = "", currentstopno = "", Stored_Dist = 0, AllStopsVisited = False, OnBus = False):
		print("New Traveller made")

	def __del__(self):
		print("Reached Destructor")
		print("Traveller did it! He visited all the bus stops")
