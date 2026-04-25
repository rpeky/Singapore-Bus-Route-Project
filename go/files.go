package main

import (
	"os"
	"path/filepath"
	"strconv"
)

const (
	DataDir = "data"

	RawDir       = DataDir + "/raw"
	ProcessedDir = DataDir + "/processed"

	BusArrivalDir  = RawDir + "/bus_arrivals"
	BusServicesDir = RawDir + "/bus_services"
	BusRoutesDir   = RawDir + "/bus_routes"
	BusStopsDir    = RawDir + "/bus_stops"

	ProcessedBusStopDir = ProcessedDir + "/bus_stops"
	ProcessedRouteDir   = ProcessedDir + "/service_routes"
	WorkingMapDir       = ProcessedDir + "/working_map"
)

// check if dirs exist, otherwise os.MkdirAll will create them
func EnsureDataDirs() error {
	dirs := []string{
		BusArrivalDir,
		BusServicesDir,
		BusRoutesDir,
		BusStopsDir,
		ProcessedBusStopDir,
		ProcessedRouteDir,
		WorkingMapDir,
	}

	for _, dir := range dirs {
		if err := os.MkdirAll(dir, 0755); err != nil {
			return err
		}
	}

	return nil
}

// check if file w path exists
func FileExists(path string) bool {
	_, err := os.Stat(path)
	return err == nil || !os.IsNotExist(err)
}

// helper functions to build the filenames / paths after checking the json
func BusArrivalPath(busStopCode string) string {
	return filepath.Join(BusArrivalDir, busStopCode+"_BusArrivalRequest_BusStop_data.json")
}

func BusServicesPath(page int) string {
	return filepath.Join(BusServicesDir, strconv.Itoa(page)+"_BusServicesRequest_data.json")
}

func BusRoutesPath(page int) string {
	return filepath.Join(BusRoutesDir, strconv.Itoa(page)+"_BusRoutesRequest_data.json")
}

func BusStopsPath(page int) string {
	return filepath.Join(BusStopsDir, strconv.Itoa(page)+"_BusStopsRequest_bus_stop_info.json")
}

// Processed data
func ProcessedBusStopPath(busStopCode string) string {
	return filepath.Join(ProcessedBusStopDir, busStopCode+"_busstop_data.json")
}

func ProcessedRoutePath(serviceNo string) string {
	return filepath.Join(ProcessedRouteDir, serviceNo+"_busserviceroute.json")
}

func WorkingMapPath() string {
	return filepath.Join(WorkingMapDir, "MC_Noneworkingmapdata.json")
}

func WriteRawJSON(path string, data []byte) error {
	return os.WriteFile(path, data, 0644)
}
