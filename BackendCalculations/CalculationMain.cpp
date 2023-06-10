#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <map>
#include <utility>


//#include "jsonprocessingfunctions.h" // to use json processing functions from jsonprocessing.cpp
//#include "businfocalc.h"			 // to use calculations from BusCalculations.cpp

#include "BusStopClass.h"
#include "TravellerClass.h"
#include "jsonprocessingfunctions.h"

// for Bus_Stop class mapping
// mapofbusstopinfo < position_5numcode, key>
// key = 0 - check if exist if == 1
/* MAP START */
std::map<std::pair<int, int>, float> mapofbusstopinfo;
std::map<std::pair<int, int>, int> mapofbusid_eachstop;
std::map<std::pair<int, int>, std::string> mapofbusstopnames;

/* Map Update Functions*/
void update_additionalvisit(int BusStopCode) {
	mapofbusstopinfo[{BusStopCode, 6}] += 1;
}


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


int main() {
	//bool allvisited = false;

	//Bus_Stop thisisastop;
	//Traveller persononbus;
	//float BusStopCode, Direction, Distance, StopSequence, NumberOfBus, TimesVisited;
	//std::string DescriptionOfStop;

	//std::string fileneededtojson = "bus_route_info_0.json";

	//std::cout << get_jsonfileretriever(fileneededtojson);


	Bus_Stop thisisastop;
	Traveller persononbus;
	float bsc, dir, dist, ss, nob, tv;
	std::string name;

	//stop 1 - simulates get values from json files
	std::cout << "enter stopcode 75009\n";
	std::cin >> bsc;
	thisisastop.update_busstopcode(bsc);
	std::cout << "enter direction 1\n";
	std::cin >> dir;
	thisisastop.update_direction(dir);
	std::cout << "enter distance 0\n";
	std::cin >> dist;
	thisisastop.update_distance(dist);
	persononbus.update_TotalDistanceTravelled(dist);
	std::cout << "enter stopseq 1\n";
	std::cin >> ss;
	thisisastop.update_stopsequence(ss);
	std::cout << "enter nofbus 30\n";
	std::cin >> nob;
	thisisastop.update_noofbus(nob);
	std::cout << "enter timesvisited 1\n";
	std::cin >> tv;
	thisisastop.update_timesvisited(tv);
	persononbus.update_addstopvisited();
	std::cout << "enter name Tampines Int\n";
	std::cin.ignore();
	std::getline(std::cin, name, '\n');
	thisisastop.update_description(name);

	thisisastop.update_addstoptomap();


	for (int i = 0; i < 7; i++) {
		std::cout << i << "bus stop map value: " << mapofbusstopinfo[{bsc, i}] << std::endl;
	}

	for (int j = 0; j < 2; j++) {
		std::cout << j << "bus name map value: " << mapofbusstopnames[{bsc, j}] << std::endl;
	}

	std::cout << "person visited: " << persononbus.StopsVisited << "stops" << std::endl;
	std::cout << "person travelled: " << persononbus.TotalDistanceTravelled << " km" << std::endl;

	std::string filename = "bus_route_info_0";
	std::cout << "busstopcode: " << get_busstopcode(get_jsonfileretriever(filename));

	return 0;
}