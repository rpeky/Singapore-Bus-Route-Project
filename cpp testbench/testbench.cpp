#include<iostream>
#include<fstream>
#include<map>
#include<utility>
#include<string>

#include<json.h>

/* MAP START */
// for Bus_Stop class mapping
// mapofbusstopinfo < position_5numcode, key>
// key = 0 - check if exist if == 1
// 

std::map<std::pair<int, int>, float> mapofbusstopinfo;
//std::map<std::pair<int, int>, int> mapofbusid_eachstop;
std::map<std::pair<int, int>, std::string> mapofbusstopnames;

class busstop {

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

	void update_addstoptomap() {
		// getinfo() json functions
		/*will use hard values here to test map*/

		mapofbusstopinfo[{BusStopCode, 0}] = 1;
		mapofbusstopinfo[{BusStopCode, 1}] = BusStopCode;
		mapofbusstopinfo[{BusStopCode, 2}] = Direction;
		mapofbusstopinfo[{BusStopCode, 3}] = Distance; //*10
		mapofbusstopinfo[{BusStopCode, 4}] = StopSequence;
		mapofbusstopinfo[{BusStopCode, 5}] = noofbus;
		mapofbusstopinfo[{BusStopCode, 6}] = TimesVisited;
		mapofbusstopnames[{BusStopCode, 0}] = "1";
		mapofbusstopnames[{BusStopCode, 1}] = Description;

	} 

	void update_busstopcode(int stopcode_5num) {
		BusStopCode = stopcode_5num;
	}

	void update_direction(int dir) {
		Direction = dir;
	}

	void update_distance(float distfromint) {
		Distance = distfromint;
	}

	void update_stopsequence(int seq) {
		StopSequence = seq;
	}

	void update_noofbus(int busno) {
		noofbus = busno;
	}

	void update_timesvisited(int visited) {
		TimesVisited = visited;
	}

	void update_description(std::string desc) {
		Description = desc;
	}

private: 




};

void update_additionalvisit(int BusStopCode) {
	float visits = mapofbusstopinfo[{BusStopCode, 6}];
	visits++;
	mapofbusstopinfo[{BusStopCode, 6}] = visits;
}



//class Traveller {
//public:
//	int CurrentPosition_5numstopcode; //must give initial bus stop code
//	int TotalDistanceTravelled;
//	int StopsVisited = 0; //initial stops visited is 0
//	int currentbusno;
//	int Stored_Dist = 0; //initial distance travelled is 0
//
//private:
//
//};

int main() {

	//test values
	//"BusStopCode": "75009",
	//	"Direction" : 1,
	//	"Distance" : 0,
	//	"Operator" : "SBST",
	//	"SAT_FirstBus" : "0500",
	//	"SAT_LastBus" : "2300",
	//	"SUN_FirstBus" : "0500",
	//	"SUN_LastBus" : "2300",
	//	"ServiceNo" : "10",
	//	"StopSequence" : 1,
	//	"WD_FirstBus" : "0500",
	//	"WD_LastBus" : "2300"

	busstop thisisastop;
	float bsc, dir, dist, ss, nob, tv;
	std::string name;
	//stop 1
	std::cout << "enter stopcode 75009\n";
	std::cin >> bsc;
	thisisastop.update_busstopcode(bsc);
	std::cout << "enter direction 1\n";
	std::cin >> dir;
	thisisastop.update_direction(dir);
	std::cout << "enter distance 0\n";
	std::cin >> dist;
	thisisastop.update_distance(dist);
	std::cout << "enter stopseq 1\n";
	std::cin >> ss;
	thisisastop.update_stopsequence(ss);
	std::cout << "enter nofbus 30\n";
	std::cin >> nob;
	thisisastop.update_noofbus(nob);
	std::cout << "enter timesvisited 1\n";
	std::cin >> tv;
	thisisastop.update_timesvisited(tv);
	std::cout << "enter name Tampines Int\n";
	std::cin.ignore();
	std::getline(std::cin, name, '\n');
	thisisastop.update_description(name);

	thisisastop.update_addstoptomap();

	for (int i = 0; i < 7; i++) {
		std::cout << i<< "bus stop map value: " << mapofbusstopinfo[{bsc, i}] << std::endl;
	}

	for (int j = 0; j < 2; j++) {
		std::cout << j<< "bus name map value: " << mapofbusstopnames[{bsc, j}] << std::endl;
	}
	//"BusStopCode": "76059",
	//	"Direction" : 1,
	//	"Distance" : 0.6,
	//	"Operator" : "SBST",
	//	"SAT_FirstBus" : "0502",
	//	"SAT_LastBus" : "2302",
	//	"SUN_FirstBus" : "0502",
	//	"SUN_LastBus" : "2302",
	//	"ServiceNo" : "10",
	//	"StopSequence" : 2,
	//	"WD_FirstBus" : "0502",
	//	"WD_LastBus" : "2302"
	//stop 2
	std::cout << "enter stopcode 76059\n";
	std::cin >> bsc;
	thisisastop.update_busstopcode(bsc);
	std::cout << "enter direction 2\n";
	std::cin >> dir;
	thisisastop.update_direction(dir);
	std::cout << "enter distance 0.6\n";
	std::cin >> dist;
	thisisastop.update_distance(dist);
	std::cout << "enter stopseq 2\n";
	std::cin >> ss;
	thisisastop.update_stopsequence(ss);
	std::cout << "enter nofbus 15\n";
	std::cin >> nob;
	thisisastop.update_noofbus(nob);
	std::cout << "enter timesvisited 1\n";
	std::cin >> tv;
	thisisastop.update_timesvisited(tv);
	std::cout << "enter name Opp Our Tampines Hub\n";
	std::cin.ignore();
	std::getline(std::cin, name, '\n');
	thisisastop.update_description(name);

	thisisastop.update_addstoptomap();

	for (int i = 0; i < 7; i++) {
		std::cout << i << "bus stop map value: " << mapofbusstopinfo[{bsc, i}] << std::endl;
	}

	for (int j = 0; j < 2; j++) {
		std::cout << j << "bus name map value: " << mapofbusstopnames[{bsc, j}] << std::endl;
	}

	std::cout << "secondvisittostoptest" << std::endl;
	update_additionalvisit(76059);
	std::cout << "stop1 visits: " << mapofbusstopinfo[{75009, 6}] << std::endl << "stop2 visits: " << mapofbusstopinfo[{76059, 6}]; 



	return 0;




}