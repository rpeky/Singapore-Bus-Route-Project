#include<iostream>
#include<fstream>
#include<string>
#include<utility>
#include<stdexcept>
#include<json/json.h>
#include<json/config.h>
#include"jsonstuff.h"

//Json::Value jsonretriever(std::string filename) {
//
//	//std::string keyedword;
//
//	std::ifstream file(filename); // reads json file under file
//	Json::Reader reader; // creates json reader
//	Json::Value stufffromfile; // json stored in completeJsonData
//	reader.parse(file, stufffromfile); // to use completeJsonData[keyword] 
//	return stufffromfile;
//}

//float get_busstopcode(Json::Value jsonfile) {
//	std::string stringtoconvert = std::stof(jsonfile[""]
//	return 
//}


//loat direction


int main() {

	std::cout << "test start\n";
	std::string nameoffile = "bus_route_info_25000.json";
	Json::Value root;
	Json::Reader reader;

	std::ifstream f(nameoffile);
	std::cout << "parsing f file\n";
	if (!f)
	{
		std::string errReason("Cannot open the settings file '");

		errReason += nameoffile;
		errReason += "'";

		throw std::domain_error(errReason);
	}
	std::cout << "finished parsing ifstream\n";

	bool parsingSuccessful = reader.parse(f, root);

	std::cout << "json parsing successful\n";

	if (!parsingSuccessful)
	{
		// report to the user the failure and their locations in the document.
		std::cout << "Failed to parse configuration\n"
			<< reader.getFormattedErrorMessages();
	}
	else
	{
		std::cout << "Works\n";
	}

	std::cout << "Json value should have data\n";
	//std::ifstream f(nameoffile);
	//f >> root;
	Json::Value::Members names = root.getMemberNames();
	std::cout << "Json value membernames in names\n";
	return 0;

	//std::cout << names.size();

	//for (int index = 0; index < names.size(); ++index)
	//{
	//	std::cout << "passthrough " + index;
	//	std::string key = names[index];
	//	std::cout << key;
	//	std::string value = root[key].asString();
	//	std::cout << value;
	//	//std::string value = root[key].asString();
	//	//std::cout << root[key] << std::endl;
	//}
	//std::string tempval_Bus_Stop_Code = root[0][0].asString();
	//std::cout << tempval_Bus_Stop_Code;

	

	//std::cout << "test";
	//std::string nameoffile = "bus_reoute_info_0.json";
	//std::cout << "test";
	//std::cout << jsonretriever(nameoffile); // has error
	//std::cout << "test";
	//return 0;



}
