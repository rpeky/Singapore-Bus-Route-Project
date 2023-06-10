#include<iostream>
#include<fstream>
#include<json/json.h>
#include"jsonstuff.h"

Json::Value jsonretriever(std::string filename) {

	//std::string keyedword;

	std::ifstream file(filename); // reads json file under file
	Json::Reader reader; // creates json reader
	Json::Value stufffromfile; // json stored in completeJsonData
	reader.parse(file, stufffromfile); // to use completeJsonData[keyword] 
	return stufffromfile;
}

//float get_busstopcode(Json::Value jsonfile) {
//	std::string stringtoconvert = std::stof(jsonfile[""]
//	return 
//}


//loat direction


int main() {
	std::cout << "test";
	std::string nameoffile = "bus_reoute_info_0.json";
	std::cout << "test";
	std::cout << jsonretriever(nameoffile); // has error
	std::cout << "test";
	return 0;



}
