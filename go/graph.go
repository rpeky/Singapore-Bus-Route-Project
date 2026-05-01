package main

import (
	"encoding/json"
	"fmt"
	"os"
)

// minimal graph struct for now

type StopID string

type Vertex struct {
	Neighbours   []StopID `json:"neighbours"`
	TimesVisited int      `json:"timesvisited"`
	DistFromInt  float64  `json:"distfromint"`
}

type Graph map[StopID]Vertex

func LoadGraph(path string) (Graph, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return nil, err
	}

	var g Graph
	if err := json.Unmarshal(data, &g); err != nil {
		return nil, err
	}

	return g, nil
}

func SaveGraph(path string, g Graph) error {
	data, err := json.MarshalIndent(g, "", "\t")
	if err != nil {
		return err
	}

	return os.WriteFile(path, data, 0644)
}

func ShowStop(id StopID) error {
	g, err := LoadGraph(WorkingMapPath())
	if err != nil {
		return err
	}

	v, ok := g[id]
	if !ok {
		return fmt.Errorf("stop %s not found", id)
	}

	fmt.Println("stop:", id)
	fmt.Println("distance from interchange:", v.DistFromInt)
	fmt.Println("times visited:", v.TimesVisited)
	fmt.Println("neighbours:")

	for _, n := range v.Neighbours {
		fmt.Println(" ", n)
	}

	return nil
}

func GraphStats() error {
	g, err := LoadGraph(WorkingMapPath())
	if err != nil {
		return err
	}

	edges := 0
	deadEnds := 0

	for _, v := range g {
		edges += len(v.Neighbours)
		if len(v.Neighbours) == 0 {
			deadEnds++
		}
	}

	fmt.Println("stops:", len(g))
	fmt.Println("edges:", edges)
	fmt.Println("dead ends:", deadEnds)

	return nil
}

func ValidateGraph() error {
	g, err := LoadGraph(WorkingMapPath())
	if err != nil {
		return err
	}

	missing := 0
	selfLoops := 0
	deadEnds := 0

	for from, v := range g {
		if len(v.Neighbours) == 0 {
			fmt.Printf("dead end: %s\n", from)
			deadEnds++
		}

		for _, to := range v.Neighbours {
			if from == to {
				fmt.Printf("self loop: %s -> %s\n", from, to)
				selfLoops++
			}

			if _, ok := g[to]; !ok {
				fmt.Printf("missing neighbour: %s -> %s\n", from, to)
				missing++
			}
		}
	}

	fmt.Println("stops:", len(g))
	fmt.Println("dead ends:", deadEnds)
	fmt.Println("self loops:", selfLoops)
	fmt.Println("missing neighbours:", missing)

	if missing > 0 {
		return fmt.Errorf("graph has %d missing neighbour references", missing)
	}

	fmt.Println("graph ok")
	return nil
}
