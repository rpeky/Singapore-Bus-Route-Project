#include <iostream>
#include <fstream>
#include <utility>

#include "businfocalc.h"
#include "jsonprocessingfunctions.h"



int distance_travelled_tothisstop(int stored_dist){ // all dist *10 to remove decimal for int purpose -- final distance to /10  {
	int curr_dist = getdistance();
	int disttoadd = curr_dist - stored_dist;
	return disttoadd;
}

