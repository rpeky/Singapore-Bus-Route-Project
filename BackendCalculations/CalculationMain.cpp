#include <iostream>
#include <map>
#include <utility>

#include "jsonprocessingfunctions.h" // to use json processing functions from jsonprocessing.cpp
#include "businfocalc.h"			 // to use calculations from BusCalculations.cpp
#include "BusStopClass.h"
#include "TravellerClass.h"

/* MAP START */
// for Bus_Stop class mapping
// mapofbusstopinfo < position_5numcode, key>
// key = 0 - check if exist if == 1

std::map<std::pair<int, int>, float> mapofbusstopinfo; 
std::map<std::pair<int, int>, int> mapofbusid_eachstop;
std::map<std::pair<int, int>, std::string> mapofbusstopnames;

/* Bus Stop Class Functions*/
void Bus_Stop::update_addstoptomap() {
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

void Bus_Stop::update_busstopcode(float stopcode_5num) {
	BusStopCode = stopcode_5num;
}

void Bus_Stop::update_direction(float dir) {
	Direction = dir;
}

void Bus_Stop::update_distance(float distfromint) {
	Distance = distfromint;
}

void Bus_Stop::update_stopsequence(float seq) {
	StopSequence = seq;
}

void Bus_Stop::update_noofbus(float busno) {
	noofbus = busno;
}

void Bus_Stop::update_timesvisited(float visited) {
	TimesVisited = visited;
}

void Bus_Stop::update_description(std::string desc) {
	Description = desc;
}

Bus_Stop::Bus_Stop() {
	BusStopCode = 0;
	Direction = 0;
	Distance = 0;
	StopSequence = 0;
	noofbus = 0;
	TimesVisited = 0;
	Description = "";
	std::cout << "Creating new bus stop" << std::endl;
}

Bus_Stop::~Bus_Stop() {
	std::cout << "Bus Stop added to map, deleting this stop, refer to map for values" << std::endl;
}

/* Traveller Class Functions*/
void Traveller::update_addstopvisited() {
	StopsVisited++;
}

void Traveller::update_TotalDistanceTravelled(float dist) {
	float currstopdist = dist;
	TotalDistanceTravelled += (dist - Stored_Dist);
	Stored_Dist = dist;
}

Traveller::Traveller() {
	TotalDistanceTravelled = 0;
	StopsVisited = 0;
	currentbusno = 0;
	Stored_Dist = 0;
	std::cout << "Creating new Traveller to take the bus" << std::endl;
}

Traveller::~Traveller() {
	std::cout << "Traveller did it! He visited all the bus stops" << std::endl;
}

/* Map Update Functions*/
void update_additionalvisit(int BusStopCode) {
	mapofbusstopinfo[{BusStopCode, 6}] += 1;
}


int main() {
	bool allvisited = false;

	Bus_Stop thisisastop;
	Traveller persononbus;
	float BusStopCode, Direction, Distance, StopSequence, NumberOfBus, TimesVisited;
	std::string DescriptionOfStop;


	return 0;
}