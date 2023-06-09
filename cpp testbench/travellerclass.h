#pragma once
#include<iostream>

class Traveller {
public:

	//int CurrentPosition_5numstopcode; //must give initial bus stop code
	float TotalDistanceTravelled = 0;
	int StopsVisited = 0; //initial stops visited is 0
	int currentbusno = 0;
	float Stored_Dist = 0; //initial distance travelled is 0

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