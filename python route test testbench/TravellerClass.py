import json
import JsonProcessingFunctions
import os
import shutil
from copy import deepcopy

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
	def __init__(self):
		#self.TotalDistanceTravelled = 0
		#self.TotalStopsVisited = 0
		#self.currentbusno = ""
		#self.currentstopno = ""
		self.AllStopsVisited = False
		#self.OnBus = False
		self.StopsVisited = set()
		self.tour = []
		self.Stored_Dist = 0
		self.copynecessarydata()
		self.dictadjlist=JsonProcessingFunctions.open_jsondatafile_returnsjsonobj('WC',6)
		self.memodict=dict()


		print("New Traveller made, traveller trapped in graph owo")
	

	#Creates working copy to work on
	def copynecessarydata(self):
		print('copying data')
		cwd=os.getcwd()
		foldertoextract=os.path.join(cwd, 'WorkingMapData')
		filetocopy=os.path.join(foldertoextract, 'MC_Noneworkingmapdata.json')
		copyname=os.path.join(foldertoextract, 'WC_workingmapdata.json')
		shutil.copyfile(filetocopy,copyname)
		return

	#attempt 1, likely wont return to original stop, or give the bus taken to whichever stop, to add these functions in future
	def searchtillendoftime_v1(self, startstop):
		#set first stop
		currstop = startstop
		self.tour.append(currstop)
		self.StopsVisited.add(currstop)
		self.dictadjlist[currstop]['timesvisited']+=1
		self.TotalStopsVisited=1
		passcheck=0

		while(self.AllStopsVisited==False):
			print('------------------------------------------------------')
			print(passcheck)
			print('currentstop:{}'.format(currstop))
			passcheck+=1

			#if too inefficient
			if(len(self.tour)>500000):
				print('==============================================')
				print('over 1000 stops passed, something probably went wrong')
				print("check working copy json")
				del self.memodict

				break
			
			choice=None
			neareststop=self.dictadjlist[currstop]['neighbours']

			#resolves one destination stops
			if(len(neareststop)==1):
				print('only one stop to traverse')
				stopcompareindex=str(currstop)+str(neareststop[0])
				disttonextstop=self.dictadjlist[neareststop[0]]['distfromint']-self.dictadjlist[currstop]['distfromint']
				timesvisited=self.dictadjlist[neareststop[0]]['timesvisited']

				tempdistvisitdict={stopcompareindex:{'dist':float(disttonextstop),'visits':int(timesvisited)}}

				currstop=neareststop[0]
				self.tour.append(currstop)
				self.StopsVisited.add(currstop)
				self.memodict.update(tempdistvisitdict)
				self.dictadjlist[currstop]['timesvisited']+=1
				self.memodict[stopcompareindex]['visits']+=1
				#print(self.memodict)
				self.check_completedallstops()
				


			#every other case
			elif(len(neareststop)>1):

				#helps to make decision later on
				distchecklist=[]
				timesvisitedlist=[]

				#decision making

				#checks for visits and distance, prioritise low visits then distance, then first stop in list that matches these params
				#can be done using zip then compare min of visits, if same itll compare min of distance, stopname is a rider
				#stores these checks for future visits to decide
				for stop in neareststop:
					#create relationship index
					stopcompareindex=str(currstop)+str(stop)
					


					#if visited before, should be tracked in memodict, just pull out data
					if (stopcompareindex in self.memodict):
						print(stopcompareindex, 'exist')
						#memodc=self.memodict[stopcompareindex].copy()
						distchecklist.append(self.memodict[stopcompareindex]['dist'])
						timesvisitedlist.append(self.memodict[stopcompareindex]['visits'])

					else:
						print(stopcompareindex,' does not exist, making data for ',stopcompareindex)
						#self.memodict[stopcompareindex]={'dist': 0,'visits': 0}
						#need to write a new function that takes distfromint from same bus route, has negative distance difference otherwise
						disttonextstop=self.dictadjlist[stop]['distfromint']-self.dictadjlist[currstop]['distfromint']
						timesvisited=self.dictadjlist[stop]['timesvisited']

						distchecklist.append(float(disttonextstop))
						timesvisitedlist.append(int(timesvisited))
						tempdistvisitdict={stopcompareindex:{'dist':float(disttonextstop),'visits':int(timesvisited)}}
						self.memodict.update(tempdistvisitdict)
						#print(self.memodict)

				print('////////////////////////////////')
				print(timesvisitedlist)
				print(distchecklist)
				print(neareststop)

				#index				0				1				2
				choice=min(zip(timesvisitedlist,distchecklist,neareststop))
				print(choice)
				stopcompareindex=str(currstop)+str(choice[2])
				currstop=str(choice[2])

				self.tour.append(currstop)
				self.StopsVisited.add(currstop)
				self.dictadjlist[currstop]['timesvisited']+=1
				self.memodict[stopcompareindex]['visits']+=1
				#self.TotalDistanceTravelled+=choice[1]
				#self.TotalStopsVisited+=1

				self.check_completedallstops()


			else:
				print(len(self.StopsVisited))
				print(self.tour)
				self.check_completedallstops()
				raise Exception('Something went wrong, go back and fix it')

		return
			
	def gettour(self):
		return self.tour

	def getsetvisited(self):
		return self.StopsVisited

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
		if(len(self.StopsVisited)==5082):
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





	def __del__(self):
		print("Reached Destructor")
		print("Traveller did it! He visited all the bus stops")
