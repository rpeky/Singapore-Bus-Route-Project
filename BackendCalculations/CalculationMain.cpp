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

std::map<std::pair<int, int>, int> mapofbusstopinfo; 
std::map<std::pair<int, int>, int> mapofbusid_eachstop;
std::map<std::pair<int, int>, std::string> mapofbusstopnames;

/* MAP END */


/* CLASS START */
// bus stop properties
class Bus_Stop {

public:
	// mapofbusstopinfo pair key identities {00000 - 5 number bus stop id, 1/2/3/4/5/6/7/8 - which map value needed}
	// 0 left for checking if map exist
	int BusStopCode;		 //map 1
	int Direction;			 //map 2
	int Distance;			 //map 3
	int StopSequence;        //map 4
	int noofbus;			 //map 5
	int TimesVisited;		 //map 6

	std::string Description; //Bus Stop name (e.g. Opp Bugis Stn Exit C)

	


private:
	// check if exists on map (self explainatory)
	void checkifmapofstopexists_meansvisitedbefore(int position_5numcode) {
																			// stop exists in map -> add a visit
		if (mapofbusstopinfo[{position_5numcode,0}] == 1) {					
			Addvisit();
		}
																			// stop does not exist in map -> generate stop in map
		else {																
			addstoptomap(position_5numcode);
		}

	};

	// add info to map 
	void addstoptomap(int position_5numcode) {

		Direction = getdirection();
		Distance = getdistance();
		StopSequence = getstopsequence();
		noofbus = getnoofbus();
		TimesVisited = 1;

		mapofbusstopinfo[{position_5numcode, 0}] = 1;
		mapofbusstopinfo[{position_5numcode, 1}] = position_5numcode;
		mapofbusstopinfo[{position_5numcode, 2}] = Direction;
		mapofbusstopinfo[{position_5numcode, 3}] = Distance;
		mapofbusstopinfo[{position_5numcode, 4}] = StopSequence;
		mapofbusstopinfo[{position_5numcode, 5}] = noofbus;
		mapofbusstopinfo[{position_5numcode, 6}] = TimesVisited;



		Description = getDescription();

		mapofbusstopnames[{position_5numcode, 1}] = Description;


		for (int i = 0; i < noofbus; i++) {
			mapofbusid_eachstop[{position_5numcode, i}] = addbustobusstop(position_5numcode, noofbus);
		}

	};

	// add 1 everytime this busstop is visited, refresh value of times visited
	void Addvisit() {
		TimesVisited++;
		mapofbusstopinfo[{BusStopCode, 6}] = TimesVisited;
	};

	// look up all the bus that go to this stop
	void Displaybusinstop() { 
		for (int i = 0; i < noofbus; i++) {
			
		}
		
	}

	std::string Displaybusstop_description() {
		return mapofbusstopnames[{BusStopCode, 1}];
	}

};


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

	Traveller persononbus;
	
	Bus_Stop stop12345;




	while (allvisited != true) {

	}













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