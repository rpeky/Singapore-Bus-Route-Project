package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

// consts
// set 1 more just in case they increase the data, to manually validate 250426
const (
	baseURL = "http://datamall2.mytransport.sg/ltaodataservice"

	NumBusStopRequest    = 12
	NumBusServiceRequest = 3
	NumBusRoutesRequest  = 52
)

// helper function to add the query to
// master query function, just modify the endpoint
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

/*-------------------------------------------------------------------------------*/
/*----------------------API Get Call helpers-----------------------*/

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
		return nil, fmt.Errorf("empty response for bus stop arrival data %s", busStopCode)
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
	Loop services may use suffixes such as G/W, for example:
	225G, 225W, 243G, 243W, 410G, 410W.

	Emperically, the last time I ran this there was only 2 payloads of output

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

/*
Refactoring generate_BusRoutesData_returnsStopJsonData(skips)
API 2.3: Bus Routes Request

Endpoint:
	/BusRoutes
	/BusRoutes?$skip=<n>

Sample JSON response:
{
    "odata.metadata": "http://datamall2.mytransport.sg/ltaodataservice/$metadataBusRoutes",
    "value": [
        {
            "BusStopCode": "75009",
            "Direction": 1,
            "Distance": 0,
            "Operator": "SBST",
            "SAT_FirstBus": "0500",
            "SAT_LastBus": "2300",
            "SUN_FirstBus": "0500",
            "SUN_LastBus": "2300",
            "ServiceNo": "10",
            "StopSequence": 1,
            "WD_FirstBus": "0500",
            "WD_LastBus": "2300"
        },
        {
            "BusStopCode": "76059",
            "Direction": 1,
            "Distance": 0.6,
            "Operator": "SBST",
            "SAT_FirstBus": "0502",
            "SAT_LastBus": "2302",
            "SUN_FirstBus": "0502",
            "SUN_LastBus": "2302",
            "ServiceNo": "10",
            "StopSequence": 2,
            "WD_FirstBus": "0502",
            "WD_LastBus": "2302"
        },
}

Notes:
	Emperically, the last time I ran this there were 51 payloads of output

*/

func QueryBusRoutesData(skips int) ([]byte, error) {
	endpoint := "/BusRoutes"

	// 2nd page onwards
	if skips != 0 {
		endpoint = fmt.Sprintf("/BusRoutes?$skip=%d", skips*500)
	}

	resp, err := Query(endpoint)
	if err != nil {
		return nil, err
	}

	// validate response is not empty
	if len(resp) == 0 {
		return nil, fmt.Errorf("empty response for bus route page %d", skips)
	}

	return resp, nil
}

/*
Refactoring generate_BusStopsRequest_togetallbusstop(skips)
API 2.4: Bus Stops Request

Endpoint:
	/BusStops
	/BusStops?$skip=<n>

Sample JSON response:
{
    "odata.metadata": "http://datamall2.mytransport.sg/ltaodataservice/$metadata#BusStops",
    "value": [
        {
            "BusStopCode": "01012",
            "Description": "Hotel Grand Pacific",
            "Latitude": 1.29684825487647,
            "Longitude": 103.85253591654006,
            "RoadName": "Victoria St"
        },
}

Notes:
	Emperically, the last time I ran this there were 11 payloads of output

*/

func QueryBusStopsData(skips int) ([]byte, error) {
	endpoint := "/BusStops"

	// 2nd page onwards
	if skips != 0 {
		endpoint = fmt.Sprintf("/BusStops?$skip=%d", skips*500)
	}

	resp, err := Query(endpoint)
	if err != nil {
		return nil, err
	}

	// validate response is not empty
	if len(resp) == 0 {
		return nil, fmt.Errorf("empty response for bus stop data page %d", skips)
	}

	return resp, nil
}

/*-------------------------------------------------------------------------------*/
/*----------------------Data fetching functions-----------------------*/
// makes the relevant api calls and generate the needed files

func FetchAllBusStops() error {
	for page := 0; page < NumBusStopRequest; page++ {
		data, err := QueryBusStopsData(page)
		if err != nil {
			return err
		}

		if err := WriteRawJSON(BusStopsPath(page), data); err != nil {
			return err
		}

		fmt.Println("saved bus stops page", page)
	}

	return nil
}

func FetchAllBusServices() error {
	for page := 0; page < NumBusServiceRequest; page++ {
		data, err := QueryBusServicesData(page)
		if err != nil {
			return err
		}

		if err := WriteRawJSON(BusServicesPath(page), data); err != nil {
			return err
		}

		fmt.Println("saved bus services page", page)
	}

	return nil
}

func FetchAllBusRoutes() error {
	for page := 0; page < NumBusRoutesRequest; page++ {
		data, err := QueryBusRoutesData(page)
		if err != nil {
			return err
		}

		if err := WriteRawJSON(BusRoutesPath(page), data); err != nil {
			return err
		}

		fmt.Println("saved bus routes page", page)
	}

	return nil
}

func FetchStaticData() error {
	// make sure the dirs are made (from files.go)
	if err := EnsureDataDirs(); err != nil {
		return err
	}

	if err := FetchAllBusStops(); err != nil {
		return err
	}

	if err := FetchAllBusServices(); err != nil {
		return err
	}

	if err := FetchAllBusRoutes(); err != nil {
		return err
	}

	return nil
}
