#include <stdio.h>
#include <iostream>
#include <map>
#include <json/json.h>

//this time struc instead of class

std::map<std::pair<int, int>, float> mapofbusstopinfo_DistanceStorage;
std::map<std::pair<int, int>, int> mapofbusid_eachstop;
std::map<std::pair<int, int>, std::string> mapofbusstopnames;

struct BusStop {
	int BusStopCode;
	int Direction;
	float Distance;
	int StopSequence;
	int NoofBus;
	int TimesVisited;
	std::string Description;
};

void update_addstoptomap(int BusStopCode, int Direction, int StopSequence, int NoofBus, int TimesVisited, float Distance, std::string Description) {
	mapofbusid_eachstop[{BusStopCode, 0}] = 1;
	mapofbusid_eachstop[{BusStopCode, 1}] = BusStopCode;
	mapofbusid_eachstop[{BusStopCode, 2}] = Direction;
	mapofbusid_eachstop[{BusStopCode, 3}] = StopSequence;
	mapofbusid_eachstop[{BusStopCode, 4}] = NoofBus;
	mapofbusid_eachstop[{BusStopCode, 5}] = TimesVisited;

	mapofbusstopinfo_DistanceStorage[{BusStopCode, 0}] = 1;
	mapofbusstopinfo_DistanceStorage[{BusStopCode, 1}] = Distance;

	mapofbusstopnames[{BusStopCode, 0}] = '1';
	mapofbusstopnames[{BusStopCode, 1}] = Description;

}


int main() {
	
	int BusStopCode = 123456;
	int Direction = 1;
	float Distance = 0.123;
	int StopSequence =0;
	int NoofBus= 100;
	int TimesVisited = 1;
	std::string Description = "generic interchange";

	BusStop InterchangeStop;
	InterchangeStop.BusStopCode = BusStopCode;
	InterchangeStop.Direction = Direction;
	InterchangeStop.Distance = Distance;
	InterchangeStop.StopSequence = StopSequence;
	InterchangeStop.NoofBus = NoofBus;
	InterchangeStop.TimesVisited = TimesVisited;
	InterchangeStop.Description = Description;

	std::cout << InterchangeStop.BusStopCode << std::endl
		<< InterchangeStop.Direction << std::endl
		<< InterchangeStop.Distance << std::endl
		<< InterchangeStop.StopSequence << std::endl
		<< InterchangeStop.NoofBus << std::endl
		<< InterchangeStop.TimesVisited << std::endl
		<< InterchangeStop.Description << std::endl;

	update_addstoptomap(BusStopCode, Direction, StopSequence, NoofBus, TimesVisited, Distance, Description);

	for (int i = 0; i < 6; i++) {
		std::cout << mapofbusid_eachstop[{BusStopCode, i}] << std::endl;
	}

	for (int i = 0; i < 2; i++) {
		std::cout << mapofbusstopinfo_DistanceStorage[{BusStopCode, i}] << std::endl;
	}

	for (int i = 0; i < 2; i++) {
		std::cout << mapofbusstopnames[{BusStopCode, i}] << std::endl;
	}






	return 0;
}