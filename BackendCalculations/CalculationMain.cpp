#include <iostream>

void placeholder;

class Bus_Stop {

public:
	std::string Description;
	int BusStopCode;
	int Direction;
	int Distance;
	int StopSequence;
};



class Traveller {
public:
	int CurrentPosition_5numstopcode;
	int TotalDistanceTravelled;
	int StopsVisited;

	void newstop();
	void adddistance(int Curr_dist, int Stored_dist);
	
};

void Traveller::newstop() {
	StopsVisited++;
}

void Traveller::adddistance(int Curr_dist, int Stored_dist){
	TotalDistanceTravelled += (Curr_dist - Stored_dist);
}


int main() {





	//bool All_visited = false;
	//int position_5numcode; // end goal is to make this a variable to test all bus stops
	//int distance = 0;
	//int stops_visited = 0;
	//int DistNew = 0;
	//int DistStored = 0;


	//while (All_visited != true) {
	//	position_5numcode = ;
	//	distance += (DistNew - DistStored);
	//	stops_visited += 1;

	//}

}