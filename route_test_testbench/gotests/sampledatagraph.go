package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// from processed stop data
type StopNode struct {
	BusStopCode  string   `json:"BusStopCode"`
	Direction    int      `json:"Direction"`
	Distance     float32  `json:"Distance"`
	StopSequence int      `json:"StopSequence"`
	IDofBus      []string `json:"IDofBus"`
	TimesVisited int      `json:"TimesVisited"`
	Description  string   `json:"Description"`
	AdjacentStop []string `json:"AdjacentStop"`
}

func main() {
	fmt.Println("teststart - Bus Stop node data")
	sample, err := os.ReadFile("ProcessedBusStopData/77311_busstop_data.json")
	if err != nil {
		panic(err)
	}

	fmt.Println("Output bus stop 77311 data")
	var samplestop StopNode

	err = json.Unmarshal(sample, &samplestop)
	if err != nil {
		panic(err)
	}

	fmt.Println(samplestop.BusStopCode)
	fmt.Println(samplestop.Direction)
	fmt.Println(samplestop.Distance)
	fmt.Println(samplestop.StopSequence)
	fmt.Println(samplestop.IDofBus)
	fmt.Println(samplestop.TimesVisited)
	fmt.Println(samplestop.Description)
	fmt.Println(samplestop.AdjacentStop)

	fmt.Println("---------------- check type ")
	for _, bus := range samplestop.IDofBus {
		fmt.Printf("%T\n", bus)
	}
	for _, bus := range samplestop.AdjacentStop {
		fmt.Printf("%T\n", bus)
	}

	fmt.Println("----------------")
	fmt.Println("teststart - Bus route data")
	sampleb, errb := os.ReadFile("ProcessedServiceRouteData/10_busserviceroute.json")

	if errb != nil {
		panic(errb)
	}

	fmt.Println("Output bus route for bus 10")
	var sampleroute [][]string

	errb = json.Unmarshal(sampleb, &sampleroute)
	if errb != nil {
		panic(errb)
	}

	for dir, stops := range sampleroute {
		// compensate for the 0/1 with +1 to become 1/2 in the
		// documnetation
		fmt.Printf("Direction %d:\n", dir+1)

		for i, stop := range stops {
			fmt.Printf("  %d: %s\n", i+1, stop)
		}
	}

}
