package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

const baseURL = "http://datamall2.mytransport.sg/ltaodataservice"

// helper function to add the query to
func Query(endpoint string) ([]byte, error) {
	// check if this device has the datamall API key
	apiKey := os.Getenv("API_KEY")
	if apiKey == "" {
		return nil, fmt.Errorf("API_KEY not set")
	}

	// all the queries are GET requests, empty body
	req, err := http.NewRequest("GET", baseURL+endpoint, nil)
	if err != nil {
		return nil, err
	}

	// set headers
	req.Header.Set("AccountKey", apiKey)
	req.Header.Set("accept", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return nil, fmt.Errorf("bad status: %s", resp.Status)
	}

	// based on the API docs, it should always be a json payload returned
	// can just take the output and write directly later
	return io.ReadAll(resp.Body)
}

/*
Refactoring generate_BusArrivalData_returnsBusServiceID(BusStopCode)
API 2.1: Bus Arrival Request
Endpoint:
	/v3/BusArrival?BusStopCode=<busStopCode>


Sample Json response:
{
	"odata.metadata": "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival",
	"BusStopCode": "83139",
	"Services": [
		{
			"ServiceNo": "15",
			"Operator": "GAS",
			"NextBus": {
				"OriginCode": "77009",
				"DestinationCode": "77009",
				"EstimatedArrival": "2024-08-14T16:41:48+08:00",
				"Monitored": 1,
				"Latitude": "1.3154918333333334",
				"Longitude": "103.9059125",
				"VisitNumber": "1",
				"Load": "SEA",
				"Feature": "WAB",
				"Type": "SD"
			},
			"NextBus2": {
			},
			"NextBus3": {
			}
		},
		{
			"ServiceNo": "150",
			"Operator": "SBST",
			"NextBus": {
			},
		}
	]
}

Additional info:
	Loop Services are appended with ‘G’ or ‘W’ to denote their
	direction of travel.
	You should account for and display these services individually
	– 225G, 225W, 243G, 243W, 410G, 410W

*/

func QueryBusArrivalData(busStopCode string) ([]byte, error) {
	endpoint := "/v3/BusArrival?BusStopCode=" + busStopCode
	resp, err := Query(endpoint)
	if err != nil {
		return nil, err
	}

	// validate response is not empty
	if len(resp) == 0 {
		return nil, fmt.Errorf("empty response for bus stop %s", busStopCode)
	}

	return resp, nil
}

/*
Refactoring generate_BusServicesData_returnsStopJsonData(skips)
API 2.2: Bus Services Request

Endpoint:
    /BusServices
    /BusServices?$skip=<n>

The LTA API returns bus service metadata in pages of 500 records.

Sample JSON response:
    {
        "odata.metadata": "http://datamall2.mytransport.sg/ltaodataservice/$metadata#BusServices",
        "value": [
            {
                "ServiceNo": "118",
                "Operator": "GAS",
                "Direction": 1,
                "Category": "TRUNK",
                "OriginCode": "65009",
                "DestinationCode": "97009",
                "AM_Peak_Freq": "5-08",
                "AM_Offpeak_Freq": "8-12",
                "PM_Peak_Freq": "8-10",
                "PM_Offpeak_Freq": "09-14",
                "LoopDesc": ""
            }
        ]
    }

Notes:
    - Direction 1 and Direction 2 should be treated separately.
    - Loop services may use suffixes such as G/W, for example:
      225G, 225W, 243G, 243W, 410G, 410W.
*/

func QueryBusServicesData(skips int) ([]byte, error) {
	endpoint := "/BusServices"

	// 2nd page onwards
	if skips != 0 {
		endpoint = fmt.Sprintf("/BusServices?$skip=%d", skips*500)
	}

	resp, err := Query(endpoint)
	if err != nil {
		return nil, err
	}

	// validate response is not empty
	if len(resp) == 0 {
		return nil, fmt.Errorf("empty response for bus service page %d", skips)
	}

	return resp, nil
}
