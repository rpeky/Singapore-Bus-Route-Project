#include <iostream>
#include <map>
#include <utility>

#include "jsonprocessingfunctions.h" // to use json processing functions from jsonprocessing.cpp
#include "businfocalc.h"			 // to use calculations from BusCalculations.cpp
#include "BusStopClass.h"
/* MAP START */
// for Bus_Stop class mapping
// mapofbusstopinfo < position_5numcode, key>
// key = 0 - check if exist if == 1
// 

std::map<std::pair<int, int>, float> mapofbusstopinfo; 
std::map<std::pair<int, int>, int> mapofbusid_eachstop;
std::map<std::pair<int, int>, std::string> mapofbusstopnames;

/* MAP END */

/* Bus Stop Class Functions*/
void busstop::update_addstoptomap() {
	// getinfo() json functions
	/*will use hard values here to test map*/

	mapofbusstopinfo[{BusStopCode, 0}] = 1;
	mapofbusstopinfo[{BusStopCode, 1}] = BusStopCode;
	mapofbusstopinfo[{BusStopCode, 2}] = Direction;
	mapofbusstopinfo[{BusStopCode, 3}] = Distance;
	mapofbusstopinfo[{BusStopCode, 4}] = StopSequence;
	mapofbusstopinfo[{BusStopCode, 5}] = noofbus;
	mapofbusstopinfo[{BusStopCode, 6}] = TimesVisited;
	mapofbusstopnames[{BusStopCode, 0}] = "1";
	mapofbusstopnames[{BusStopCode, 1}] = Description;

}

void busstop::update_busstopcode(float stopcode_5num) {
	BusStopCode = stopcode_5num;
}

void busstop::update_direction(float dir) {
	Direction = dir;
}

void busstop::update_distance(float distfromint) {
	Distance = distfromint;
}

void busstop::update_stopsequence(float seq) {
	StopSequence = seq;
}

void busstop::update_noofbus(float busno) {
	noofbus = busno;
}

void busstop::update_timesvisited(float visited) {
	TimesVisited = visited;
}

void busstop::update_description(std::string desc) {
	Description = desc;
}

void update_additionalvisit(int BusStopCode) {
	mapofbusstopinfo[{BusStopCode, 6}] += 1;

}


void update_additionalvisit(int BusStopCode) {
	mapofbusstopinfo[{BusStopCode, 6}] += 1;
}


class Traveller {
public:

	float TotalDistanceTravelled = 0;
	int StopsVisited = 0; //initial stops visited is 0
	int currentbusno = 0;
	float Stored_Dist = 0; //initial distance travelled is 0

	void update_addstopvisited() {
		StopsVisited++;
	}

	void update_TotalDistanceTravelled(float dist) {
		float currstopdist = dist;
		TotalDistanceTravelled += (dist - Stored_Dist);
		Stored_Dist = dist;
	}

private:

	
};


/* CLASS END */


int main() {
	bool allvisited = false;

	Bus_Stop thisisastop;
	Traveller persononbus;
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