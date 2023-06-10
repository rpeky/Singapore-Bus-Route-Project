#pragma once
#include<iostream>
#include<map>

// for Bus_Stop class mapping
// mapofbusstopinfo < position_5numcode, key>
// key = 0 - check if exist if == 1
/* MAP START */
std::map<std::pair<int, int>, float> mapofbusstopinfo;
std::map<std::pair<int, int>, int> mapofbusid_eachstop;
std::map<std::pair<int, int>, std::string> mapofbusstopnames;