#include <iostream>
#include <fstream>
#include <json.h>

#include "jsonprocessingfunctions.h"


int jsonretriever(std::string filename, std::string keyword) {
	
	//std::string keyedword;

	std::ifstream file(filename); // reads json file under file
	Json::Reader reader; // creates json reader
	Json::Value completeJsonData; // json stored in completeJsonData
	reader.parse(file, completeJsonData); // to use completeJsonData[keyword] 
}

// retrieves direction of bus (1 or 2)
int getdirection() { 
	int direction;
	return direction;
}

// retrieves distance from interchange to current stop
int getdistance() {  
	int distance;
	return distance;
}

// retrieves stop number from interchange
int getstopsequence() {
	int sequence;

	return sequence;
}

//// retrieves 
//int getnoofbus() {
//
//}
//
//// retrieves id of bus that pickup/dropoff from this stop
//int businstop() {
//
//}

int addbustobusstop(int position_5numcode, int noofbus) { // to sort through the json to find the busses that belong to the bus stop 
	int busno;
	return busno;
}

std::string getDescription() {
	std::string description;
	return description;
}


//
//void jsonretriever() {
//
//}