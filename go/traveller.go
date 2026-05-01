package main

import (
	"encoding/json"
	"fmt"
	"math"
	"os"
	"path/filepath"
)

// return the tour or an error
type Traveller interface {
	Name() string
	Tour(g Graph, start StopID) ([]StopID, error)
}

// Generic way to run the traveller on the graph,
// take in the strat from main stdin to pass tot he
func RunTraveller(method string, start StopID) error {
	// load the consolidated working copy of the graph
	g, err := LoadGraph(WorkingMapPath())
	if err != nil {
		return err
	}

	// load the map of every stop name
	stopNames, err := LoadStopNames()
	if err != nil {
		fmt.Println("warning: could not load stop names:", err)
		stopNames = make(map[StopID]string)
	}

	// initialise a new traveller based on the method from stdin
	traveller, err := NewTraveller(method)
	if err != nil {
		return err
	}

	// run the tour
	tour, err := traveller.Tour(g, start)
	if err != nil {
		fmt.Println("partial/failure:", err)
	}

	fmt.Println("method:", traveller.Name())
	fmt.Println("tour length:", len(tour))

	valid := buildValidStopSet(g)
	seen := make(map[StopID]bool)

	// format the tour results, in the order:
	// visitno#, stopid, name, curr/total
	for i, stop := range tour {
		if valid[stop] {
			seen[stop] = true
		}

		name := stopNames[stop]
		if name == "" {
			name = "(unknown)"
		}

		fmt.Printf(
			"%d. %s %-40s | unique valid visited: %d/%d\n",
			i+1,
			stop,
			name,
			len(seen),
			len(valid),
		)
	}

	return nil
}

// method to swap for the correct struct to pair with the interface
func NewTraveller(method string) (Traveller, error) {
	switch method {
	case "greedy":
		return GreedyTraveller{}, nil
	case "reachable-greedy":
		return ReachableGreedyTraveller{}, nil
	case "relaxed-greedy":
		return RelaxedGreedyTraveller{}, nil
	case "path-greedy":
		return PathGreedyTraveller{}, nil
	default:
		return nil, fmt.Errorf("unknown traveller method: %s", method)
	}
}

/*--------------------------------------------------------------------------*/
//Shared traveller helpers

func buildValidStopSet(g Graph) map[StopID]bool {
	valid := make(map[StopID]bool)

	for id, v := range g {
		// check if the vertex is not isolated
		if len(v.Neighbours) > 0 {
			valid[id] = true
		}
	}

	return valid
}

func nearestUnvisitedNeighbour(g Graph, curr StopID, visited map[StopID]bool) (StopID, bool) {
	// get vertex data and check if exist
	v, ok := g[curr]
	if !ok {
		return "", false
	}

	var best StopID
	bestSet := false
	bestDist := 0.0

	// iterate through vertex neighbours
	for _, n := range v.Neighbours {
		// skip if visited
		if visited[n] {
			continue
		}

		// skip if does not exist
		if _, ok := g[n]; !ok {
			continue
		}

		// diff between interchange distances
		dist := DistanceBetweenStops(g, curr, n)

		// update flags if better
		if !bestSet || dist < bestDist {
			best = n
			bestDist = dist
			bestSet = true
		}
	}

	return best, bestSet
}

func DistanceBetweenStops(g Graph, a, b StopID) float64 {
	return math.Abs(g[b].DistFromInt - g[a].DistFromInt)
}

func nearestUnvisitedValidNeighbour(
	g Graph,
	curr StopID,
	visited map[StopID]bool,
	valid map[StopID]bool,
) (StopID, bool) {

	// iterate through vertex neighbours
	v, ok := g[curr]
	if !ok {
		return "", false
	}

	var best StopID
	bestSet := false
	bestDist := 0.0

	// go through the neighbour set for the stop
	for _, next := range v.Neighbours {
		// skip if neighbour not valid
		if !valid[next] {
			continue
		}

		// skip if neighbour already visited
		if visited[next] {
			continue
		}

		// g[curr] returns value, exist bool
		// check if the neighbour does not exist as a vertex skip
		if _, ok := g[next]; !ok {
			continue
		}

		// distance from inter for next - dist from inter for curr
		dist := DistanceBetweenStops(g, curr, next)

		// flags to check if new values are better
		if !bestSet || dist < bestDist {
			best = next
			bestDist = dist
			bestSet = true
		}
	}

	return best, bestSet
}

func leastVisitedNeighbour(g Graph,
	curr StopID,
	valid map[StopID]bool,
	visits map[StopID]int,
) (StopID, bool) {

	v, ok := g[curr]
	if !ok {
		return "", false
	}

	var best StopID
	bestSet := false
	bestVisits := 0
	bestDist := 0.0

	for _, next := range v.Neighbours {
		if !valid[next] {
			continue
		}

		if _, ok := g[next]; !ok {
			continue
		}

		nextVisits := visits[next]
		dist := DistanceBetweenStops(g, curr, next)

		if !bestSet ||
			nextVisits < bestVisits ||
			(nextVisits == bestVisits && dist < bestDist) {
			best = next
			bestVisits = nextVisits
			bestDist = dist
			bestSet = true
		}
	}

	return best, bestSet
}

func nearestUnvisitedByDistance(g Graph,
	curr StopID,
	visited map[StopID]bool,
	valid map[StopID]bool,
) (StopID, bool) {

	var best StopID
	bestSet := false
	bestDist := 0.0

	for id := range valid {
		if visited[id] {
			continue
		}

		if _, ok := g[id]; !ok {
			continue
		}

		dist := DistanceBetweenStops(g, curr, id)

		if !bestSet || dist < bestDist {
			best = id
			bestDist = dist
			bestSet = true
		}
	}

	return best, bestSet
}

func BFSNearestUnvisitedValid(g Graph,
	start StopID,
	visited map[StopID]bool,
	valid map[StopID]bool,
) ([]StopID, bool) {

	queue := []StopID{start}
	parent := make(map[StopID]StopID)
	seen := make(map[StopID]bool)

	seen[start] = true

	var target StopID
	found := false

	for len(queue) > 0 {
		// pop the queue
		curr := queue[0]
		queue = queue[1:]

		// check if the vertex found is valid and unvisited
		if valid[curr] && !visited[curr] {
			target = curr
			found = true
			break
		}

		// if not valid, add push new neighbours in queue, set the parent
		// as the current vertex
		for _, next := range g[curr].Neighbours {
			if seen[next] {
				continue
			}

			if _, ok := g[next]; !ok {
				continue
			}

			seen[next] = true
			parent[next] = curr
			queue = append(queue, next)
		}
	}

	// for some reason, it has no valid neighbours, its stuck
	if !found {
		return nil, false
	}

	path := []StopID{target}

	// reconstruct path using the parent
	for path[len(path)-1] != start {
		prev := parent[path[len(path)-1]]
		path = append(path, prev)
	}

	// flip it so the path is in correct order, target is end of path
	reverseStopPath(path)
	return path, true
}

func reverseStopPath(path []StopID) {
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
}

func countVisitedValid(visited map[StopID]bool, valid map[StopID]bool) int {
	count := 0

	// count stops in the visited set
	for id := range valid {
		if visited[id] {
			count++
		}
	}

	return count
}

func countVisitedByCount(visits map[StopID]int, valid map[StopID]bool) int {
	count := 0

	for id := range valid {
		if visits[id] > 0 {
			count++
		}
	}

	return count
}

/*--------------------------------------------------------------------------*/
// Stop name structs and helpers for json parsing

type BusStopsPayload struct {
	Value []BusStopNameRecord `json:"value"`
}

type BusStopNameRecord struct {
	BusStopCode string `json:"BusStopCode"`
	Description string `json:"Description"`
}

func LoadStopNames() (map[StopID]string, error) {
	names := make(map[StopID]string)

	files, err := filepath.Glob("data/raw/bus_stops/*.json")
	if err != nil {
		return nil, err
	}

	for _, path := range files {
		data, err := os.ReadFile(path)
		if err != nil {
			return nil, err
		}

		var payload BusStopsPayload
		if err := json.Unmarshal(data, &payload); err != nil {
			return nil, err
		}

		for _, stop := range payload.Value {
			names[StopID(stop.BusStopCode)] = stop.Description
		}
	}

	return names, nil
}

/*--------------------------------------------------------------------------*/

/*
	Traveller Definitions
*/

/*--------------------------------------------------------------------------*/
//Greedy traveller
// look for the nearest unvisited neighbour -> high chance of collision into
// a vertex where all neighbours have been visited

type GreedyTraveller struct{}

func (t GreedyTraveller) Name() string {
	return "greedy"
}

// find nearest unvisited neighbour, very simple greedy
func (t GreedyTraveller) Tour(g Graph, start StopID) ([]StopID, error) {
	// check if the starting vertex exists
	if _, ok := g[start]; !ok {
		return nil, fmt.Errorf("start stop %s not found", start)
	}

	visited := make(map[StopID]bool)
	tour := make([]StopID, 0, len(g)+1)

	curr := start
	visited[curr] = true
	tour = append(tour, curr)

	// run until visited all vertices
	for len(visited) < len(g) {
		// check if there is a unvisited neighbour, and if exists
		next, ok := nearestUnvisitedNeighbour(g, curr, visited)
		if !ok {
			return tour, fmt.Errorf("dead end at %s after visiting %d/%d stops", curr, len(visited), len(g))
		}

		curr = next
		visited[curr] = true
		tour = append(tour, curr)
	}

	return tour, nil
}

/*--------------------------------------------------------------------------*/
// Less strict greedy greedy traveller
type ReachableGreedyTraveller struct{}

func (t ReachableGreedyTraveller) Name() string {
	return "reachable-greedy"
}

// less restrictive version since you can get stuck in a strict greedy if all
// neighbours have already been visited (spiraled to death)

/*
Try the nearest unvisited neighbour

if no unvisited neighbours in the neighbour set/list, run bfs to find
nearest unvisited stop following the directed edges
*/
func (t ReachableGreedyTraveller) Tour(g Graph, start StopID) ([]StopID, error) {
	// check if starting vertex exists
	if _, ok := g[start]; !ok {
		return nil, fmt.Errorf("start stop %s not found", start)
	}

	valid := buildValidStopSet(g)
	visited := make(map[StopID]bool)
	tour := make([]StopID, 0, len(valid))

	curr := start

	for {
		// check if current stop is valid and not visited
		// -> set as visited
		// add to tour
		if valid[curr] && !visited[curr] {
			visited[curr] = true
			tour = append(tour, curr)
		}

		// check if visited all stops
		if countVisitedValid(visited, valid) == len(valid) {
			return tour, nil
		}

		// slightly stricter neighbour checking
		next, ok := nearestUnvisitedValidNeighbour(g, curr, visited, valid)
		// if valid go next to visit
		if ok {
			curr = next
			continue
		}

		// otherwise run bfs
		path, ok := BFSNearestUnvisitedValid(g, curr, visited, valid)
		if !ok {
			return tour, fmt.Errorf(
				"stuck at %s after visiting %d/%d valid stops",
				curr,
				countVisitedValid(visited, valid),
				len(valid),
			)
		}

		// extract the path, exclude 0 since we are already there
		for _, stop := range path[1:] {
			curr = stop

			// when constructing the path if the vertex is new mark
			// as visited
			if valid[curr] && !visited[curr] {
				visited[curr] = true
			}

			// append the vertex whether visited or unvisited as
			// part of tour, dont cut them off
			tour = append(tour, curr)
		}
	}
}

/*--------------------------------------------------------------------------*/
// small heuristic based on the neighbour with the lowest visit count
// same method as the python prototype with the greedy neighbour method
type RelaxedGreedyTraveller struct{}

func (t RelaxedGreedyTraveller) Name() string {
	return "relaxed-greedy"
}

/*
choose neighbour stop with lowest visit count

should break the stuck condition, but its essentially blind cause you only
look ahead by one vertex
*/
func (t RelaxedGreedyTraveller) Tour(g Graph, start StopID) ([]StopID, error) {
	if _, ok := g[start]; !ok {
		return nil, fmt.Errorf("start stop %s not found", start)
	}

	valid := buildValidStopSet(g)
	visits := make(map[StopID]int)
	tour := make([]StopID, 0, len(valid))

	curr := start
	// gave additional buffer since i expect there to be alot of repeats
	// from the python experiment
	maxSteps := len(g) * 100

	for step := 0; step < maxSteps; step++ {
		// increment current stop visit count
		if valid[curr] {
			visits[curr]++
			tour = append(tour, curr)
		}

		// check if visited all valid stops
		if countVisitedByCount(visits, valid) == len(valid) {
			return tour, nil
		}

		next, ok := leastVisitedNeighbour(g, curr, valid, visits)
		if !ok {
			return tour, fmt.Errorf("no valid outgoing neighbour at %s", curr)
		}

		curr = next
	}

	return tour, fmt.Errorf(
		"step limit hit after visiting %d/%d valid stops",
		countVisitedByCount(visits, valid),
		len(valid),
	)
}

/*--------------------------------------------------------------------------*/
// another heuristic to run bfs and find nearest unvisited stop and run there

type PathGreedyTraveller struct{}

func (t PathGreedyTraveller) Name() string {
	return "path-greedy"
}

/*
run bfs at current stop to nearest unvisited stop and go there

if there are no undirected paths to the target, start a new segment
from the nearest unvisited by distance
*/
func (t PathGreedyTraveller) Tour(g Graph, start StopID) ([]StopID, error) {
	if _, ok := g[start]; !ok {
		return nil, fmt.Errorf("start stop %s not found", start)
	}

	valid := buildValidStopSet(g)
	visited := make(map[StopID]bool)
	tour := make([]StopID, 0, len(valid)*2)

	curr := start

	if valid[curr] {
		visited[curr] = true
		tour = append(tour, curr)
	}

	segments := 1

	for countVisitedValid(visited, valid) < len(valid) {
		path, ok := BFSNearestUnvisitedValid(g, curr, visited, valid)
		if !ok {
			next, ok := nearestUnvisitedByDistance(g, curr, visited, valid)
			if !ok {
				break
			}

			fmt.Printf(
				"restart segment %d: %s -> %s | visited %d/%d\n",
				segments+1,
				curr,
				next,
				countVisitedValid(visited, valid),
				len(valid),
			)

			curr = next
			segments++

			if valid[curr] && !visited[curr] {
				visited[curr] = true
				tour = append(tour, curr)
			}

			continue
		}

		for _, stop := range path[1:] {
			curr = stop
			tour = append(tour, curr)

			if valid[curr] && !visited[curr] {
				visited[curr] = true
			}
		}
	}

	if countVisitedValid(visited, valid) < len(valid) {
		return tour, fmt.Errorf(
			"ended after visiting %d/%d valid stops",
			countVisitedValid(visited, valid),
			len(valid),
		)
	}

	fmt.Println("segments:", segments)
	return tour, nil
}
