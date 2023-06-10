#include "BusStopClass.h"

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