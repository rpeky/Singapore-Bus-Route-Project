#include <iostream>
#include <fstream>
#include <json.h>

#include "jsonprocessingfunctions.h"


int jsonretriever() {
	std::string filename;
	std::string keyword;

	std::ifstream file(filename); // reads json file under file
	Json::Reader reader; // creates json reader
	Json::Value completeJsonData; // json stored in completeJsonData
	reader.parse(file, completeJsonData); // to use completeJsonData[keyword] 
}

int getdirection() {
	int direction;
	return direction;
}

int getdistance() {
	int distance;
	return distance;
}

int getstopsequence() {
	int sequence;
	return sequence;
}

int getnoofbus() {

}