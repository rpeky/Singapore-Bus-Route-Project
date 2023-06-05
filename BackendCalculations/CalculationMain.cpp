#include <iostream>
#include <map>
#include <utility>

#include "jsonprocessingfunctions.h" // to use jsonprocessing functions from jsonprocessing.cpp


// mapofbusstopinfo < position_5numcode, key>
// key = 0 - check if exist if == 1
// 


std::map<std::pair<int,int>, int> mapofbusstopinfo; 


// bus stop properties
class Bus_Stop {

public:
	// mapofbusstopinfo pair left values
	// 0 left for checking if map exist
	int BusStopCode;		 //map 1
	int Direction;			 //map 2
	int Distance;			 //map 3
	int StopSequence;        //map 4
	int TimesVisited;		 //map 5
	int noofbus;			 //map 6


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
		mapofbusstopinfo[{position_5numcode, 0}] = 1;
		mapofbusstopinfo[{position_5numcode, 1}] = position_5numcode;
		mapofbusstopinfo[{position_5numcode, 2}] = getdirection();
		mapofbusstopinfo[{position_5numcode, 3}] = getdistance();
		mapofbusstopinfo[{position_5numcode, 4}] = getstopsequence();

	};

	// add 1 everytime this busstop is visited
	void Addvisit() {
		TimesVisited++;
	};

};


class Traveller {
public:
	int CurrentPosition_5numstopcode;
	int TotalDistanceTravelled;	
	int StopsVisited;
	int currentbusno;
	
private:
	void Addvisit();
	void adddistance(int Curr_dist, int Stored_dist);
	void takebus();
	void leavebus();
	void nextbusdecision();
	
};

void Traveller::Addvisit() {
	StopsVisited++;

}

void Traveller::adddistance(int Curr_dist, int Stored_dist){
	TotalDistanceTravelled += (Curr_dist - Stored_dist);
}

void Traveller::takebus() {

}

void Traveller::leavebus() {

}

void Traveller::nextbusdecision() {

}



int main() {





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