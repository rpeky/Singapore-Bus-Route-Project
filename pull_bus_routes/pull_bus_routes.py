import json
import os
import requests
import pprint
import datetime
import urllib
from urlprase import urlparse
import httplib2 as http


API_KEY = "4BXSLAQ5T+C4NJ6TA9/qjA=="

#for authentication
headers = {
	'AccountKey': API_KEY,
	'accept': 'application/json'
}	

stop_codes_list = json.loads(open("stop_codes.json").read())

stop_codes = set()

for code in stop_codes_list:
	stop_codes.add(code)


##http://datamall2.mytransport.sg/ltaodataservice/BusRoutes 
    #Returns detailed route information for all services currently in operation,
    #including: all bus stops along each route, first/last bus timings for each stop.

    ##TODO: 1) list bus stop 2) find buses approaching 3) find buses leaving _can use array to test(?)
def collecting_order_of_bus_stops(interchange_name,selected_bus):
    

    data = requests.get(
        url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2",
		headers = headers,
		params = {"BusStopCode" : }
	).json()['Services']





    return














## KIV for timing bus time taken
#def time_to_min(bustimestring_tuple): #does not handle special cases when the arrival time will cross midnight
#	bustimestring = bustimestring_tuple[0]
#	if bustimestring == "": #check if correct condition, not sure
#		return "No Estimate Available"
#	datetimestring = str(datetime.datetime.utcnow())
#	hourdiff = int(bustimestring[11:13]) - int(datetimestring[11:13]) - 8 #converting hours difference from UTC to UTC+8
#	mindiff = int(bustimestring[14:16]) - int(datetimestring[14:16])
#	secdiff = int(bustimestring[17:19]); - int(datetimestring[17:19])
#	arrivaltime_sec = hourdiff*60*60 + mindiff*60 + secdiff #arrival time in seconds
#	arrivaltime_min = int(arrivaltime_sec/60) #arrival time in minutes, rounded down
#	if (arrivaltime_min <= 0):
#		return ("Arriving",bustimestring_tuple[1])
#	return (str(arrivaltime_min) + " min",bustimestring_tuple[1])