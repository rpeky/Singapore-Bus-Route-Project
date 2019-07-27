import json
import os
import requests
import pprint
import datetime
import urllib
#from urlprase import urlparse  #not sure what this module does tbh
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
import httplib2 as http


API_KEY = "4BXSLAQ5T+C4NJ6TA9/qjA=="
#API_KEY = "V3Vgr4XCSiCOCLGwxt6QbQ=="
#for authentication
headers = {
	'AccountKey': API_KEY,
	'accept': 'application/json'
}	


#check if bus is to or away (??) test attribute anyways
def check_direction(bus_service_number): 
    direction_1_or_2 = ""
    data = requests.get(
        url = "http://datamall2.mytransport.sg/ltaodataservice/BusServices",
        headers = headers,
        params = {"Direction" : direction_1_or_2}
        ).json()

    return direction_1_or_2


if __name__ == "__main__":
    testdata = check_direction("225w") #check for return
    testdata2 = check_direction("12") #check for return
    testdata3 = check_direction("229") #check for return
    if testdata is None: #nani no value, maybe its at night no data?
        print("desu")
    print("abc")
    print(testdata)
    print("efg")
    print(testdata2)
    print("hij")
    print(testdata3)
    print("klm")
    






















































###http://datamall2.mytransport.sg/ltaodataservice/BusRoutes 
#    #Returns detailed route information for all services currently in operation,
#    #including: all bus stops along each route, first/last bus timings for each stop.

#    ##TODO: 1) list bus stop 2) find buses approaching 3) find buses leaving _can use array to test(?)
#def collecting_order_of_bus_stops(interchange_name,selected_bus):
    
#    #use array to test? // recurse the function maybe
#    data = requests.get(
#        url = "http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2",
#		headers = headers,
#		params = {"BusStopCode" : }
#	).json()['Services']





#    return


#def listing_bus_stops()











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