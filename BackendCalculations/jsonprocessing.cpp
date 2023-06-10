#include <iostream>
#include <fstream>


#include "jsonprocessingfunctions.h"


Json::Value get_jsonfileretriever(std::string filename) {

	std::ifstream file(filename);							// reads json file under file
	Json::Reader reader;									// creates json reader
	Json::Value completeJsonData;							// json stored in completeJsonData
	reader.parse(file, completeJsonData);					// to use completeJsonData[keyword] 
	return  completeJsonData;
}

float get_busstopcode(Json::Value JsonData) {
	Json::StreamWriterBuilder builder;
	builder.settings_["indentation"] = "";
	std::string jsontostring = Json::writeString(builder, JsonData["value"][1][0]);
	float busstopcode = std::stof(jsontostring);

	return busstopcode;
	
}

////
////// retrieves direction of bus (1 or 2) // bus_route_info jsonfile.value[
////float getdirection() {
////	float direction;
////	return direction;
////}
//
////// retrieves distance from interchange to current stop
////float getdistance() {
////
////}
////
////// retrieves stop number from interchange
////float getstopsequence() {
////
////}
//
////// retrieves 
////int getnoofbus() {
////
////}
////
////// retrieves id of bus that pickup/dropoff from this stop
////int businstop() {
////
////}
//
////void addbustobusstop(int position_5numcode, int noofbus) { // to sort through the json to find the busses that belong to the bus stop 
////	for (int i = 0; i < noofbus; i++) {
////
////	}
////}
//
//std::string getDescription() {
//	std::string description;
//	return description;
//}


//
//void jsonretriever() {
//
//}