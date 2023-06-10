#include "TravellerClass.h"

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
