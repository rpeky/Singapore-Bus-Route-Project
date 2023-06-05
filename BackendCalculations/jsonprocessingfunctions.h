#pragma once
#include <iostream>
#include <fstream>
#include <json.h>

int jsonretriever(std::string filename, std::string keyword);
int getdirection();
int getdistance();
int getstopsequence();
int getnoofbus();
std::string getDescription();