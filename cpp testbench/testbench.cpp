//#include<iostream>
//#include<fstream>
//#include<map>
//#include<utility>
//#include<string>
//
//#include<json/json.h>
//
//#include"busstopclass.h"
//#include"travellerclass.h"
//
///* MAP START */
//// for Bus_Stop class mapping
//// mapofbusstopinfo < position_5numcode, key>
//// key = 0 - check if exist if == 1
//// 
//
//std::map<std::pair<int, int>, float> mapofbusstopinfo;
////std::map<std::pair<int, int>, int> mapofbusid_eachstop;
//std::map<std::pair<int, int>, std::string> mapofbusstopnames;
//
///* Bus Stop Class Functions*/
//void Bus_Stop::update_addstoptomap() {
//	// getinfo() json functions
//	/*will use hard values here to test map*/
//
//	mapofbusstopinfo[{BusStopCode, 0}] = 1;
//	mapofbusstopinfo[{BusStopCode, 1}] = BusStopCode;
//	mapofbusstopinfo[{BusStopCode, 2}] = Direction;
//	mapofbusstopinfo[{BusStopCode, 3}] = Distance;
//	mapofbusstopinfo[{BusStopCode, 4}] = StopSequence;
//	mapofbusstopinfo[{BusStopCode, 5}] = noofbus;
//	mapofbusstopinfo[{BusStopCode, 6}] = TimesVisited;
//	mapofbusstopnames[{BusStopCode, 0}] = "1";
//	mapofbusstopnames[{BusStopCode, 1}] = Description;
//
//}
//
//void Bus_Stop::update_busstopcode(float stopcode_5num) {
//	BusStopCode = stopcode_5num;
//}
//
//void Bus_Stop::update_direction(float dir) {
//	Direction = dir;
//}
//
//void Bus_Stop::update_distance(float distfromint) {
//	Distance = distfromint;
//}
//
//void Bus_Stop::update_stopsequence(float seq) {
//	StopSequence = seq;
//}
//
//void Bus_Stop::update_noofbus(float busno) {
//	noofbus = busno;
//}
//
//void Bus_Stop::update_timesvisited(float visited) {
//	TimesVisited = visited;
//}
//
//void Bus_Stop::update_description(std::string desc) {
//	Description = desc;
//}
//
//Bus_Stop::Bus_Stop() {
//	BusStopCode = 0;
//	Direction = 0;
//	Distance = 0;
//	StopSequence = 0;
//	noofbus = 0;
//	TimesVisited = 0;
//	Description = "";
//	std::cout << "Creating new bus stop" << std::endl;
//}
//
//Bus_Stop::~Bus_Stop() {
//	std::cout << "Bus Stop added to map, deleting this stop, refer to map for values" << std::endl;	 
//}
//
///* Traveller Class Functions*/
//void Traveller::update_addstopvisited() {
//	StopsVisited++;
//}
//
//void Traveller::update_TotalDistanceTravelled(float dist) {
//	float currstopdist = dist;
//	TotalDistanceTravelled += (dist - Stored_Dist);
//	Stored_Dist = dist;
//}
//
//void Traveller::decision_tomake() { 
//	 
//}
//
//Traveller::Traveller() {
//	TotalDistanceTravelled = 0;
//	StopsVisited = 0;
//	currentbusno = 0;
//	Stored_Dist = 0;
//	AllStopsVisited = false;
//	std::cout << "Creating new Traveller to take the bus" << std::endl;
//}
//
//Traveller::~Traveller() {
//	std::cout << "Traveller did it! He visited all the bus stops" << std::endl;
//}
//
///* Map Update Functions*/
//void update_additionalvisit(int BusStopCode) {
//	mapofbusstopinfo[{BusStopCode, 6}] += 1;
//}
//
//int main() {
//
//	//test values
//	//"BusStopCode": "75009",
//	//	"Direction" : 1,
//	//	"Distance" : 0,
//	//	"Operator" : "SBST",
//	//	"SAT_FirstBus" : "0500",
//	//	"SAT_LastBus" : "2300",
//	//	"SUN_FirstBus" : "0500",
//	//	"SUN_LastBus" : "2300",
//	//	"ServiceNo" : "10",
//	//	"StopSequence" : 1,
//	//	"WD_FirstBus" : "0500",
//	//	"WD_LastBus" : "2300"
//
//	Bus_Stop thisisastop;
//	Traveller persononbus;
//	float bsc, dir, dist, ss, nob, tv;
//	std::string name;
//
//	//stop 1 - simulates get values from json files
//	std::cout << "enter stopcode 75009\n";
//	std::cin >> bsc;
//	thisisastop.update_busstopcode(bsc);
//	std::cout << "enter direction 1\n";
//	std::cin >> dir;
//	thisisastop.update_direction(dir);
//	std::cout << "enter distance 0\n";
//	std::cin >> dist;
//	thisisastop.update_distance(dist);
//	persononbus.update_TotalDistanceTravelled(dist);
//	std::cout << "enter stopseq 1\n";
//	std::cin >> ss;
//	thisisastop.update_stopsequence(ss);
//	std::cout << "enter nofbus 30\n";
//	std::cin >> nob;
//	thisisastop.update_noofbus(nob);
//	std::cout << "enter timesvisited 1\n";
//	std::cin >> tv;
//	thisisastop.update_timesvisited(tv);
//	persononbus.update_addstopvisited();
//	std::cout << "enter name Tampines Int\n";
//	std::cin.ignore();
//	std::getline(std::cin, name, '\n');
//	thisisastop.update_description(name);
//
//	thisisastop.update_addstoptomap();
//
//
//
//	for (int i = 0; i < 7; i++) {
//		std::cout << i<< "bus stop map value: " << mapofbusstopinfo[{bsc, i}] << std::endl;
//	}
//
//	for (int j = 0; j < 2; j++) {
//		std::cout << j<< "bus name map value: " << mapofbusstopnames[{bsc, j}] << std::endl;
//	}
//
//	std::cout << "person visited: " << persononbus.StopsVisited << "stops" << std::endl;
//	std::cout << "person travelled: " << persononbus.TotalDistanceTravelled << " km" << std::endl;
//
//	return 0;
//
//
//
//
//}
//
//
//
//
//// additional stuff
////
//////"BusStopCode": "76059",
//////	"Direction" : 1,
//////	"Distance" : 0.6,
//////	"Operator" : "SBST",
//////	"SAT_FirstBus" : "0502",
//////	"SAT_LastBus" : "2302",
//////	"SUN_FirstBus" : "0502",
//////	"SUN_LastBus" : "2302",
//////	"ServiceNo" : "10",
//////	"StopSequence" : 2,
//////	"WD_FirstBus" : "0502",
//////	"WD_LastBus" : "2302"
//////stop 2
////std::cout << "enter stopcode 76059\n";
////std::cin >> bsc;
////thisisastop.update_busstopcode(bsc);
////std::cout << "enter direction 1\n";
////std::cin >> dir;
////thisisastop.update_direction(dir);
////std::cout << "enter distance 0.6\n";
////std::cin >> dist;
////thisisastop.update_distance(dist);
////persononbus.update_TotalDistanceTravelled(dist);
////std::cout << "enter stopseq 2\n";
////std::cin >> ss;
////thisisastop.update_stopsequence(ss);
////std::cout << "enter nofbus 15\n";
////std::cin >> nob;
////thisisastop.update_noofbus(nob);
////std::cout << "enter timesvisited 1\n";
////std::cin >> tv;
////thisisastop.update_timesvisited(tv);
////persononbus.update_addstopvisited();
////std::cout << "enter name Opp Our Tampines Hub\n";
////std::cin.ignore();
////std::getline(std::cin, name, '\n');
////thisisastop.update_description(name);
////
////thisisastop.update_addstoptomap();
////
////
////
////for (int i = 0; i < 7; i++) {
////	std::cout << i << "bus stop map value: " << mapofbusstopinfo[{bsc, i}] << std::endl;
////}
////
////for (int j = 0; j < 2; j++) {
////	std::cout << j << "bus name map value: " << mapofbusstopnames[{bsc, j}] << std::endl;
////}
////
//////std::cout << "secondvisittostoptest" << std::endl;
//////update_additionalvisit(75009);
//////std::cout << "stop1 visits: " << mapofbusstopinfo[{75009, 6}] << std::endl << "stop2 visits: " << mapofbusstopinfo[{76059, 6}]; 
////std::cout << "person visited: " << persononbus.StopsVisited << " stops" << std::endl;
////std::cout << "person travelled: " << persononbus.TotalDistanceTravelled << " km" << std::endl;
////
//////"BusStopCode": "76069",
//////	"Direction" : 1,
//////	"Distance" : 1.1,
//////	"Operator" : "SBST",
//////	"SAT_FirstBus" : "0504",
//////	"SAT_LastBus" : "2304",
//////	"SUN_FirstBus" : "0503",
//////	"SUN_LastBus" : "2304",
//////	"ServiceNo" : "10",
//////	"StopSequence" : 3,
//////	"WD_FirstBus" : "0504",
//////	"WD_LastBus" : "2304"
////
////
////std::cout << "enter stopcode 76069\n";
////std::cin >> bsc;
////thisisastop.update_busstopcode(bsc);
////std::cout << "enter direction 1\n";
////std::cin >> dir;
////thisisastop.update_direction(dir);
////std::cout << "enter distance 1.1\n";
////std::cin >> dist;
////thisisastop.update_distance(dist);
////persononbus.update_TotalDistanceTravelled(dist);
////std::cout << "enter stopseq 3\n";
////std::cin >> ss;
////thisisastop.update_stopsequence(ss);
////std::cout << "enter nofbus 15\n";
////std::cin >> nob;
////thisisastop.update_noofbus(nob);
////std::cout << "enter timesvisited 1\n";
////std::cin >> tv;
////thisisastop.update_timesvisited(tv);
////persononbus.update_addstopvisited();
////std::cout << "enter name Blk 147\n";
////std::cin.ignore();
////std::getline(std::cin, name, '\n');
////thisisastop.update_description(name);
////
////thisisastop.update_addstoptomap();
////
////
////
////for (int i = 0; i < 7; i++) {
////	std::cout << i << "bus stop map value: " << mapofbusstopinfo[{bsc, i}] << std::endl;
////}
////
////for (int j = 0; j < 2; j++) {
////	std::cout << j << "bus name map value: " << mapofbusstopnames[{bsc, j}] << std::endl;
////}
////
////std::cout << "person visited: " << persononbus.StopsVisited << " stops" << std::endl;
////std::cout << "person travelled: " << persononbus.TotalDistanceTravelled << " km" << std::endl;
