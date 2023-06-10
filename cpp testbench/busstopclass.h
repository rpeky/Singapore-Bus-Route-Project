#pragma once
#include<iostream>

class Bus_Stop {

public:
	// mapofbusstopinfo pair key identities {00000 - 5 number bus stop id, 1/2/3/4/5/6/7/8 - which map value needed}
	// 0 left for checking if map exist
	float BusStopCode;		 //map 1
	float Direction;		 //map 2
	float Distance;			 //map 3
	float StopSequence;      //map 4
	float noofbus;			 //map 5
	float TimesVisited;		 //map 6
	std::string Description; //Bus Stop name (e.g. Opp Bugis Stn Exit C)

	Bus_Stop();
	~Bus_Stop();

	void update_addstoptomap();
	void update_busstopcode(float stopcode_5num);
	void update_direction(float dir);
	void update_distance(float distfromint);
	void update_stopsequence(float seq);
	void update_noofbus(float busno);
	void update_timesvisited(float visited);
	void update_description(std::string desc);

};