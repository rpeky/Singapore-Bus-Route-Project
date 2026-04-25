import json
import os
import requests
import pprint
import datetime

API_KEY = "V3Vgr4XCSiCOCLGwxt6QbQ=="

#for authentication
headers = {
	'AccountKey': API_KEY,
	'accept': 'application/json'
}	

stop_codes_list = json.loads(open("stop_codes.json").read())

stop_codes = set()

for code in stop_codes_list:
	stop_codes.add(code)

def time_to_min(bustimestring_tuple): #does not handle special cases when the arrival time will cross midnight
	bustimestring = bustimestring_tuple[0]
	if bustimestring == "": #check if correct condition, not sure
		return "No Estimate Available"
	datetimestring = str(datetime.datetime.utcnow())
	hourdiff = int(bustimestring[11:13]) - int(datetimestring[11:13]) - 8 #converting hours difference from UTC to UTC+8
	mindiff = int(bustimestring[14:16]) - int(datetimestring[14:16])
	secdiff = int(bustimestring[17:19]); - int(datetimestring[17:19])
	arrivaltime_sec = hourdiff*60*60 + mindiff*60 + secdiff #arrival time in seconds
	arrivaltime_min = int(arrivaltime_sec/60) #arrival time in minutes, rounded down
	if (arrivaltime_min <= 0):
		return ("Arriving",bustimestring_tuple[1])
	return (str(arrivaltime_min) + " min",bustimestring_tuple[1])



def single_arrival_data(stop_name,selected_bus):
	stop_name_to_code = json.loads(open('stop_name_to_code.json').read())
	data = requests.get(
		url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2",
		headers = headers,
		params = {"BusStopCode" : stop_name_to_code[stop_name]}
	).json()['Services']

	nextbus = ""
	nextbus2 = ""
	nextbus3 = ""

	for bus in data:
		if bus['ServiceNo'] == str(selected_bus): #change to tuples, for feature and load
			load = bus['NextBus']['Load']
			load2 = bus['NextBus']['Load']
			load3 = bus['NextBus']['Load']

			nextbus = (bus['NextBus']['EstimatedArrival'],"Seats Available" if load == 'SEA' else ("Standing Available" if load == "SDA" else "Limited Standing"))
			nextbus2 = (bus['NextBus2']['EstimatedArrival'],"Seats Available" if load2 == 'SEA' else ("Standing Available" if load2 == "SDA" else "Limited Standing"))
			nextbus3 = (bus['NextBus3']['EstimatedArrival'],"Seats Available" if load3 == 'SEA' else ("Standing Available" if load3 == "SDA" else "Limited Standing"))

			nextbus,nextbus2,nextbus3 = time_to_min(nextbus),time_to_min(nextbus2),time_to_min(nextbus3)
			if nextbus != "No Estimate Available":
				nextbus = nextbus[0] + ", " + nextbus[1]
			if nextbus2 != "No Estimate Available": 
				nextbus2 = nextbus2[0] + ", " + nextbus2[1]
			if nextbus3 != "No Estimate Available":
				nextbus3 = nextbus3[0] + ", " + nextbus3[1]

	return nextbus,nextbus2,nextbus3

def all_arrival_data(stop_code): #only for stop code inputs

	data = requests.get(
	url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2",
	headers = headers,
	params = {"BusStopCode" : stop_code}
	).json()['Services']

	nextbus = ""
	nextbus2 = ""
	nextbus3 = ""
	ans = ""

	for bus in data:
		load = bus['NextBus']['Load']
		load2 = bus['NextBus']['Load']
		load3 = bus['NextBus']['Load']

		nextbus = (bus['NextBus']['EstimatedArrival'],"Seats Available" if load == 'SEA' else ("Standing Available" if load == "SDA" else "Limited Standing"))
		nextbus2 = (bus['NextBus2']['EstimatedArrival'],"Seats Available" if load2 == 'SEA' else ("Standing Available" if load2 == "SDA" else "Limited Standing"))
		nextbus3 = (bus['NextBus3']['EstimatedArrival'],"Seats Available" if load3 == 'SEA' else ("Standing Available" if load3 == "SDA" else "Limited Standing"))
			
		nextbus,nextbus2,nextbus3 = time_to_min(nextbus),time_to_min(nextbus2),time_to_min(nextbus3)

		if nextbus != "No Estimate Available":
			nextbus = nextbus[0] + ", " + nextbus[1]
		if nextbus2 != "No Estimate Available":
			nextbus2 = nextbus2[0] + ", " + nextbus2[1]
		if nextbus3 != "No Estimate Available":
			nextbus3 = nextbus3[0] + ", " + nextbus3[1]

		ans += "Bus {}: \n".format(bus['ServiceNo'])
		ans += nextbus + "\n" + nextbus2 + "\n" + nextbus3 + "\n\n"		
	return ans  

def stop_data(stop_name):
	stop_name_to_code = json.loads(open("stop_name_to_code.json").read())
	data = requests.get(
		url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2",
		headers = headers,
		params = {"BusStopCode" : stop_name_to_code[stop_name]}
	).json()['Services']

	return data


def route_data(selected_bus):
	all_routes = json.loads(open("routes.json").read())
	stop_code_to_name = json.loads(open("stop_code_to_name.json").read())
	selected_bus_route = []
	for stop in all_routes:
		if stop["ServiceNo"] == str(selected_bus):
			selected_bus_route.append(stop_code_to_name[stop["BusStopCode"]])

	return selected_bus_route

def iscode(text):
	if len(text) < 5:
		return False
	for i in range (0,len(text)-4): 
		if text[i:i+5] in stop_codes: #sliding window to check if a bus stop code is a substring
			return text[i:i+5]

	return False

if __name__ == "__main__":
	data = single_arrival_data("Blk 429","12e")
	print(data)