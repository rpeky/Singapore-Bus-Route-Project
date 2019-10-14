#Data test set
bigassstring = """
{
    "BusStopCode": "85091",
    "Services": [
        {
            "NextBus": {
                "DestinationCode": "77009",
                "EstimatedArrival": "2019-10-14T18:45:33+08:00",
                "Feature": "WAB",
                "Latitude": "1.319632",
                "Load": "SEA",
                "Longitude": "103.93512233333334",
                "OriginCode": "10499",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "77009",
                "EstimatedArrival": "2019-10-14T18:51:41+08:00",
                "Feature": "WAB",
                "Latitude": "1.3121158333333334",
                "Load": "SEA",
                "Longitude": "103.92304133333333",
                "OriginCode": "10499",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "77009",
                "EstimatedArrival": "2019-10-14T19:00:15+08:00",
                "Feature": "WAB",
                "Latitude": "1.3072195",
                "Load": "SEA",
                "Longitude": "103.90673983333333",
                "OriginCode": "10499",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "Operator": "GAS",
            "ServiceNo": "12"
        },
        {
            "NextBus": {
                "DestinationCode": "77009",
                "EstimatedArrival": "2019-10-14T18:40:17+08:00",
                "Feature": "WAB",
                "Latitude": "1.3237168333333333",
                "Load": "SEA",
                "Longitude": "103.94420116666667",
                "OriginCode": "10499",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "77009",
                "EstimatedArrival": "2019-10-14T19:08:29+08:00",
                "Feature": "WAB",
                "Latitude": "1.3000831666666666",
                "Load": "SEA",
                "Longitude": "103.85521316666667",
                "OriginCode": "10499",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "",
                "EstimatedArrival": "",
                "Feature": "",
                "Latitude": "",
                "Load": "",
                "Longitude": "",
                "OriginCode": "",
                "Type": "",
                "VisitNumber": ""
            },
            "Operator": "GAS",
            "ServiceNo": "12e"
        },
        {
            "NextBus": {
                "DestinationCode": "17009",
                "EstimatedArrival": "2019-10-14T18:41:45+08:00",
                "Feature": "WAB",
                "Latitude": "1.3265901666666666",
                "Load": "SEA",
                "Longitude": "103.9403455",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "17009",
                "EstimatedArrival": "2019-10-14T18:52:45+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "17009",
                "EstimatedArrival": "2019-10-14T19:07:45+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "14"
        },
        {
            "NextBus": {
                "DestinationCode": "99009",
                "EstimatedArrival": "2019-10-14T18:39:08+08:00",
                "Feature": "WAB",
                "Latitude": "1.3264245",
                "Load": "SEA",
                "Longitude": "103.94392666666667",
                "OriginCode": "10499",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "99009",
                "EstimatedArrival": "2019-10-14T18:55:54+08:00",
                "Feature": "WAB",
                "Latitude": "1.3209373333333332",
                "Load": "SEA",
                "Longitude": "103.91331966666667",
                "OriginCode": "10499",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "99009",
                "EstimatedArrival": "2019-10-14T19:03:46+08:00",
                "Feature": "WAB",
                "Latitude": "1.3177846666666666",
                "Load": "SEA",
                "Longitude": "103.89753733333333",
                "OriginCode": "10499",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "Operator": "GAS",
            "ServiceNo": "2"
        },
        {
            "NextBus": {
                "DestinationCode": "54009",
                "EstimatedArrival": "2019-10-14T18:52:16+08:00",
                "Feature": "WAB",
                "Latitude": "1.3215673333333333",
                "Load": "SDA",
                "Longitude": "103.91969183333333",
                "OriginCode": "54009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "54009",
                "EstimatedArrival": "2019-10-14T19:00:18+08:00",
                "Feature": "WAB",
                "Latitude": "1.3187401666666667",
                "Load": "SDA",
                "Longitude": "103.90233266666667",
                "OriginCode": "54009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "54009",
                "EstimatedArrival": "2019-10-14T19:07:27+08:00",
                "Feature": "WAB",
                "Latitude": "1.3184061666666667",
                "Load": "SDA",
                "Longitude": "103.8921115",
                "OriginCode": "54009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "24"
        },
        {
            "NextBus": {
                "DestinationCode": "75009",
                "EstimatedArrival": "2019-10-14T18:37:25+08:00",
                "Feature": "WAB",
                "Latitude": "1.3269885",
                "Load": "SEA",
                "Longitude": "103.9452035",
                "OriginCode": "52009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "75009",
                "EstimatedArrival": "2019-10-14T18:44:29+08:00",
                "Feature": "WAB",
                "Latitude": "1.3246898333333332",
                "Load": "SEA",
                "Longitude": "103.93470333333333",
                "OriginCode": "52009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "75009",
                "EstimatedArrival": "2019-10-14T18:48:00+08:00",
                "Feature": "",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "85091",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "31"
        },
        {
            "NextBus": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2019-10-14T18:45:11+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2019-10-14T18:57:31+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2019-10-14T19:11:31+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "35"
        },
        {
            "NextBus": {
                "DestinationCode": "75009",
                "EstimatedArrival": "2019-10-14T18:40:19+08:00",
                "Feature": "WAB",
                "Latitude": "1.3260173333333334",
                "Load": "SEA",
                "Longitude": "103.9441885",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "75009",
                "EstimatedArrival": "2019-10-14T18:44:50+08:00",
                "Feature": "WAB",
                "Latitude": "1.3202755",
                "Load": "SEA",
                "Longitude": "103.93753983333333",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "75009",
                "EstimatedArrival": "2019-10-14T18:53:13+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "38"
        },
        {
            "NextBus": {
                "DestinationCode": "94009",
                "EstimatedArrival": "2019-10-14T18:40:07+08:00",
                "Feature": "WAB",
                "Latitude": "1.3258358333333333",
                "Load": "SEA",
                "Longitude": "103.94242816666667",
                "OriginCode": "55009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "94009",
                "EstimatedArrival": "2019-10-14T18:48:44+08:00",
                "Feature": "WAB",
                "Latitude": "1.3311366666666666",
                "Load": "SEA",
                "Longitude": "103.9326485",
                "OriginCode": "55009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "94009",
                "EstimatedArrival": "2019-10-14T19:01:42+08:00",
                "Feature": "WAB",
                "Latitude": "1.3336999999999999",
                "Load": "SDA",
                "Longitude": "103.9006155",
                "OriginCode": "55009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "45"
        },
        {
            "NextBus": {
                "DestinationCode": "97009",
                "EstimatedArrival": "2019-10-14T18:47:03+08:00",
                "Feature": "WAB",
                "Latitude": "1.3186661666666666",
                "Load": "SEA",
                "Longitude": "103.93284316666667",
                "OriginCode": "97009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "97009",
                "EstimatedArrival": "2019-10-14T19:00:31+08:00",
                "Feature": "WAB",
                "Latitude": "1.30665",
                "Load": "SEA",
                "Longitude": "103.90948616666667",
                "OriginCode": "97009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "97009",
                "EstimatedArrival": "2019-10-14T19:10:15+08:00",
                "Feature": "WAB",
                "Latitude": "1.3032575",
                "Load": "SEA",
                "Longitude": "103.90572083333333",
                "OriginCode": "97009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "47"
        },
        {
            "NextBus": {
                "DestinationCode": "84299",
                "EstimatedArrival": "2019-10-14T18:44:16+08:00",
                "Feature": "WAB",
                "Latitude": "1.3160918333333333",
                "Load": "SEA",
                "Longitude": "103.94420383333333",
                "OriginCode": "11379",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "84299",
                "EstimatedArrival": "2019-10-14T18:56:22+08:00",
                "Feature": "WAB",
                "Latitude": "1.3074646666666667",
                "Load": "SEA",
                "Longitude": "103.91779966666667",
                "OriginCode": "11379",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "84299",
                "EstimatedArrival": "2019-10-14T19:03:32+08:00",
                "Feature": "WAB",
                "Latitude": "1.3045618333333333",
                "Load": "SDA",
                "Longitude": "103.9074115",
                "OriginCode": "11379",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "48"
        },
        {
            "NextBus": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2019-10-14T18:37:38+08:00",
                "Feature": "WAB",
                "Latitude": "1.327444",
                "Load": "SEA",
                "Longitude": "103.946377",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "NextBus2": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2019-10-14T18:44:29+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "DD",
                "VisitNumber": "1"
            },
            "NextBus3": {
                "DestinationCode": "84009",
                "EstimatedArrival": "2019-10-14T18:48:49+08:00",
                "Feature": "WAB",
                "Latitude": "0",
                "Load": "SEA",
                "Longitude": "0",
                "OriginCode": "84009",
                "Type": "SD",
                "VisitNumber": "1"
            },
            "Operator": "SBST",
            "ServiceNo": "9"
        }
    ],
    "odata.metadata": "http://datamall2.mytransport.sg/ltaodataservice/$metadata#BusArrivalv2/@Element"
}
    """

brokenstring = []

def string_breaker(strxd):
    for line in strxd:
        brokenstring.append(line)



def seacrh_no_bus_in_bs(stingarino):
    #position of "serviceno"
    position = bigassstring.find("ServiceNo")
    return position



#plan here is to break the data into indivisual lines, since the 
#data appears to have a fixed structure, we can assume that the
#same line will have the same data for all stops (other than the number of results we can obtain)
#hence we can break the string into a list for each line
#and find the bus number, destination it came from 
#and next destination

#next step is to produce a map using the set of a bus, the previous stop, curr stop and next stop for a route

if __name__=="__main__":
    string_breaker(bigassstring)
    brokestringlength = len(brokenstring)

    