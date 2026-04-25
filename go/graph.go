package main

// minimal graph struct for now

type StopID string

type Vertex struct {
	neighbours   []StopID
	timesvisited int
}

type Graph map[StopID]Vertex
