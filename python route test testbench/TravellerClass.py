class Traveller():

	"""
	TotalDistanceTravelled = float
	StopsVisited = int
	currentbusno = str
	Stored_Dist = float
	AllStopsVisited = bool
	OnBus = bool
	"""

	TotalDistanceTravelled = 0
	StopsVisited = 0
	currentbusno = ""
	Stored_Dist = 0
	AllStopsVisited = False
	OnBus = False

	# update functions
	def update_addstopvisited(self):
		self.StopsVisited+=1
		return

	def update_TotalDistanceTravelled(self, dist):
		self.TotalDistanceTravelled += (dist - self.Stored_Dist)
		self.Stored_Dist = dist
		return

	def update_alightbus(self):
		OnBus = False
		return

	def update_takebus(self):
		OnBus = True
		return

	def update_newbus(self, newbusno):
		self.currentbusno = newbusno
		return

    # decision functions
	def decision_stayonbus(self):
		pass
	
	def decision_leavebus(self):
		return self.update_alightbus()
	
	def decision_takebus(self):
		return self.update_takebus()

	#implies not on bus, will return decision_takebus() and update_bus
	def decision_choosebus(self):
		pass

	# check functions
	def check_completedallstops(self):
		pass

	def check_onbus_or_onstop(self):
		return self.OnBus

	def check_nextbus(self):
		pass



	def __init__(self, TotalDistanceTravelled = 0, StopsVisited = 0, currentbusno = "", Stored_Dist = 0, AllStopsVisited = False, OnBus = False):
		print("New Traveller made")

	def __del__(self):
		print("Reached Destructor")
		print("Traveller did it! He visited all the bus stops")













