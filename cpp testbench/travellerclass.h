#pragma once
#include<iostream>

class Traveller {
public:

	//int CurrentPosition_5numstopcode; //must give initial bus stop code
	float TotalDistanceTravelled;
	int StopsVisited; //initial stops visited is 0
	int currentbusno;
	float Stored_Dist; //initial distance travelled is 0
	bool AllStopsVisited;

	Traveller();
	~Traveller();

	void update_addstopvisited();
	void update_TotalDistanceTravelled(float dist);
	void decision_tomake();

private:

	void decision_stayonbus() {

	}

	void decision_leavebus() {
		
	}
	
	void decision_choosebus() {

	}

};