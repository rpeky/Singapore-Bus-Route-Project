#include <iostream>
#include <map>
#include <utility>

#include "jsonprocessingfunctions.h" // to use json processing functions from jsonprocessing.cpp
#include "businfocalc.h"			 // to use calculations from BusCalculations.cpp

/* MAP START */
// for Bus_Stop class mapping
// mapofbusstopinfo < position_5numcode, key>
// key = 0 - check if exist if == 1
// 

std::map<std::pair<int, int>, float> mapofbusstopinfo; 
std::map<std::pair<int, int>, int> mapofbusid_eachstop;
std::map<std::pair<int, int>, std::string> mapofbusstopnames;

/* MAP END */


/* CLASS START */
// bus stop properties
class Bus_Stop {

public:
	// mapofbusstopinfo pair key identities {00000 - 5 number bus stop id, 1/2/3/4/5/6/7/8 - which map value needed}
	// 0 left for checking if map exist
	float BusStopCode;		 //map 1
	float Direction;		 //map 2
	float Distance;			 //map 3
	float StopSequence;      //map 4
	float noofbus;			 //map 5
	float TimesVisited;		 //map 6

	std::string Description; //Bus Stop name (e.g. Opp Bugis Stn Exit C)

	//public update functions - tested in testbench works
	void update_busstopcode(int stopcode_5num) {
		BusStopCode = stopcode_5num;
	}

	void update_direction(int dir) {
		Direction = dir;
	}

	void update_distance(float distfromint) {
		Distance = distfromint;
	}

	void update_stopsequence(int seq) {
		StopSequence = seq;
	}

	void update_noofbus(int busno) {
		noofbus = busno;
	}

	void update_timesvisited(int visited) {
		TimesVisited = visited;
	}

	void update_description(std::string desc) {
		Description = desc;
	}

	void update_addstoptomap() { // to figure out if this should be private or public, and how to get input from the json files
		// getinfo() json functions
		/*will use hard values here to test map*/

		mapofbusstopinfo[{BusStopCode, 0}] = 1;
		mapofbusstopinfo[{BusStopCode, 1}] = BusStopCode;
		mapofbusstopinfo[{BusStopCode, 2}] = Direction;
		mapofbusstopinfo[{BusStopCode, 3}] = Distance; //*10
		mapofbusstopinfo[{BusStopCode, 4}] = StopSequence;
		mapofbusstopinfo[{BusStopCode, 5}] = noofbus;
		mapofbusstopinfo[{BusStopCode, 6}] = TimesVisited;
		mapofbusstopnames[{BusStopCode, 0}] = "1";
		mapofbusstopnames[{BusStopCode, 1}] = Description;

	}

	//private:

	//// check if exists on map (self explainatory)
	//void checkifmapofstopexists_meansvisitedbefore() {
	//																		// stop exists in map -> add a visit
	//	if (mapofbusstopinfo[{BusStopCode,0}] == 1) {					/*check if entry exists in map first --> to update and do to add in git commit message to do*/
	//		Addvisit();
	//	}
	//																		// stop does not exist in map -> generate stop in map
	//	else {																
	//		addstoptomap(BusStopCode);
	//	}

	//};

	// add info to map 
	//void addstoptomap(int position_5numcode) {

	//	Direction = getdirection();
	//	Distance = getdistance();
	//	StopSequence = getstopsequence();
	//	noofbus = getnoofbus();
	//	TimesVisited = 1;

	//	mapofbusstopinfo[{position_5numcode, 0}] = 1;
	//	mapofbusstopinfo[{position_5numcode, 1}] = position_5numcode;
	//	mapofbusstopinfo[{position_5numcode, 2}] = Direction;
	//	mapofbusstopinfo[{position_5numcode, 3}] = Distance;
	//	mapofbusstopinfo[{position_5numcode, 4}] = StopSequence;
	//	mapofbusstopinfo[{position_5numcode, 5}] = noofbus;
	//	mapofbusstopinfo[{position_5numcode, 6}] = TimesVisited;



	//	Description = getDescription();

	//	mapofbusstopnames[{position_5numcode, 1}] = Description;


	//	for (int i = 0; i < noofbus; i++) {
	//		mapofbusid_eachstop[{position_5numcode, i}] = addbustobusstop(position_5numcode, noofbus);
	//	}

	//};

	// add 1 everytime this busstop is visited, refresh value of times visited
	//void Addvisit() {
	//	TimesVisited++;
	//	mapofbusstopinfo[{BusStopCode, 6}] = TimesVisited;
	//};

	//// look up all the bus that go to this stop
	//void Displaybusinstop() { 
	//	for (int i = 0; i < noofbus; i++) {
	//		
	//	}
	//	
	//}

	//// return description of bus stop
	//std::string Displaybusstop_description() {
	//	return mapofbusstopnames[{BusStopCode, 1}];
	//}

};

void update_additionalvisit(int BusStopCode) { // adds a visit to the stop if revisited
	float visits = mapofbusstopinfo[{BusStopCode, 6}];
	visits++;
	mapofbusstopinfo[{BusStopCode, 6}] = visits;
}


class Traveller {
public:
	int CurrentPosition_5numstopcode; //must give initial bus stop code
	int TotalDistanceTravelled;	
	int StopsVisited= 0; //initial stops visited is 0
	int currentbusno;
	int Stored_Dist = 0; //initial distance travelled is 0
	
private:
	void Addvisit() {
		StopsVisited++;
	}
	void adddistance() {
		int disttoadd = distance_travelled_tothisstop(Stored_Dist);
		TotalDistanceTravelled += disttoadd;
	}

	void newstop_makedecision() {

	}

	void stayonbus() {
		Addvisit();
	}

	void leavebus() {

	}

	void takebus() {

	}

	void idle_atstop_nextbusdecision() {

	}
	
};


/* CLASS END */


int main() {
	bool allvisited = false;

	Bus_Stop thisisastop;
	float bsc, dir, dist, ss, nob, tv;
	std::string name;
















	//bool All_visited = false;
	//int position_5numcode; // end goal is to make this a variable to test all bus stops
	//int distance = 0;
	//int stops_visited = 0;
	//int DistNew = 0;
	//int DistStored = 0;


	//while (All_visited != true) {
	//	position_5numcode = ;
	//	distance += (DistNew - DistStored);
	//	stops_visited += 1;

	//}

}