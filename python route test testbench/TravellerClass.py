class Traveller():
	"""
	TotalDistanceTravelled = float
	StopsVisited = int
	currentbusno = str
	Stored_Dist = float

	"""

	TotalDistanceTravelled = None
	StopsVisited = None
	currentbusno = None
	Stored_Dist = None

	def update_addstopvisited(self):
		StopsVisited+=1

	def update_TotalDistanceTravelled(self, dist):
		TotalDistanceTravelled += (dist - Stored_Dist)
		Stored_Dist = dist

	def __init__(self, TotalDistanceTravelled = 0, StopsVisited = 0, currentbusno = None, Stored_Dist = 0):
		print("New Traveller made")










