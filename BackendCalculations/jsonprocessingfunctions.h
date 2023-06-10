#pragma once
#include <iostream>
#include <fstream>
#include <json/json.h>

Json::Value get_jsonfileretriever(std::string filename);
float get_busstopcode(Json::Value JsonData);
//float getdirection();
//float getdistance();
//float getstopsequence();
//float getnoofbus();
//void addbustobusstop(int position_5numcode, int noofbus);
//std::string getDescription();