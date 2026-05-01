package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func runCommand(args []string) error {
	if len(args) == 0 {
		usage()
		return nil
	}

	cmd := args[0]

	switch cmd {
	case "fetch":
		return FetchStaticData()

	case "fetch-stops":
		if err := EnsureDataDirs(); err != nil {
			return err
		}
		return FetchAllBusStops()

	case "fetch-services":
		if err := EnsureDataDirs(); err != nil {
			return err
		}
		return FetchAllBusServices()

	case "fetch-routes":
		if err := EnsureDataDirs(); err != nil {
			return err
		}
		return FetchAllBusRoutes()

		/*
			case "build-routes":
				return GenerateAllRoutesForEveryBus()

			case "build-graph":
				return GenerateAdjacencyListForAllBusStops()

			case "all":
				if err := FetchStaticData(); err != nil {
					return err
				}
				if err := GenerateAllRoutesForEveryBus(); err != nil {
					return err
				}
				return GenerateAdjacencyListForAllBusStops()
		*/
	case "show-stop":
		if len(args) < 2 {
			return fmt.Errorf("usage: busgraph show-stop <busstopcode>")
		}
		return ShowStop(StopID(args[1]))

	case "tour":
		if len(args) < 2 {
			return fmt.Errorf("usage: busgraph tour <startstop>")
		}
		return RunGreedyTour(StopID(args[1]))

	case "stats":
		return GraphStats()

	case "validate-graph":
		return ValidateGraph()

	case "datadir":
		return EnsureDataDirs()

	case "help", "-h", "--help":
		usage()
		return nil

	case "traveller":
		if len(args) < 3 {
			return fmt.Errorf("usage: busgraph traveller <method> <startstop>")
		}
		return RunTraveller(args[1], StopID(args[2]))

	default:
		usage()
		return fmt.Errorf("unknown command: %s", cmd)
	}
}

func runInteractiveMenu() {
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Println()
		fmt.Println("Singapore Bus Graph CLI")
		fmt.Println("-----------------------")
		fmt.Println("1.  Fetch all static data")
		fmt.Println("2.  Fetch bus stops")
		fmt.Println("3.  Fetch bus services")
		fmt.Println("4.  Fetch bus routes")
		fmt.Println("5.  Build service routes")
		fmt.Println("6.  Build adjacency graph")
		fmt.Println("7.  Run all")
		fmt.Println("8.  Show stop")
		fmt.Println("9.  Run greedy tour")
		fmt.Println("10. Graph stats")
		fmt.Println("11. Validate graph")
		fmt.Println("12. Ensure data dirs exist")
		fmt.Println("13. Traveller run tour")
		fmt.Println("14. Help")
		fmt.Println("0.  Exit")
		fmt.Print("> ")

		line, err := reader.ReadString('\n')
		if err != nil {
			fmt.Fprintln(os.Stderr, "input error:", err)
			continue
		}

		choice := strings.TrimSpace(line)

		var runErr error

		switch choice {
		case "1":
			runErr = runCommand([]string{"fetch"})

		case "2":
			runErr = runCommand([]string{"fetch-stops"})

		case "3":
			runErr = runCommand([]string{"fetch-services"})

		case "4":
			runErr = runCommand([]string{"fetch-routes"})

		case "5":
			runErr = runCommand([]string{"build-routes"})

		case "6":
			runErr = runCommand([]string{"build-graph"})

		case "7":
			runErr = runCommand([]string{"all"})

		case "8":
			stop := prompt(reader, "bus stop code: ")
			if stop == "" {
				fmt.Println("empty stop code")
				continue
			}
			runErr = runCommand([]string{"show-stop", stop})

		case "9":
			start := prompt(reader, "start stop code: ")
			if start == "" {
				fmt.Println("empty start stop code")
				continue
			}
			runErr = runCommand([]string{"tour", start})

		case "10":
			runErr = runCommand([]string{"stats"})

		case "11":
			runErr = runCommand([]string{"validate-graph"})

		case "12":
			runErr = runCommand([]string{"datadir"})

		case "13":
			method := prompt(reader, "method [greedy/reachable-greedy]: ")
			if method == "" {
				fmt.Println("empty method")
				continue
			}

			start := prompt(reader, "start stop code: ")
			if start == "" {
				fmt.Println("empty start stop code")
				continue
			}

			runErr = runCommand([]string{"traveller", method, start})

		case "14":
			usage()
			continue

		case "0", "q", "quit", "exit":
			fmt.Println("bye")
			return

		default:
			fmt.Println("unknown option")
			continue
		}

		if runErr != nil {
			fmt.Fprintln(os.Stderr, "error:", runErr)
		} else {
			fmt.Println("done")
		}
	}
}

func prompt(reader *bufio.Reader, msg string) string {
	fmt.Print(msg)

	line, err := reader.ReadString('\n')
	if err != nil {
		fmt.Fprintln(os.Stderr, "input error:", err)
		return ""
	}

	return strings.TrimSpace(line)
}

func usage() {
	fmt.Println(`usage:
		  busgraph fetch
		  busgraph fetch-stops
		  busgraph fetch-services
		  busgraph fetch-routes
		  busgraph build-routes
		  busgraph build-graph
		  busgraph all
		  busgraph show-stop <busstopcode>
		  busgraph tour <startstop>
		  busgraph stats
		  busgraph validate-graph

		If no command is given, interactive mode starts.
		`)
}

func main() {
	if len(os.Args) > 1 {
		if err := runCommand(os.Args[1:]); err != nil {
			fmt.Fprintln(os.Stderr, "error:", err)
			os.Exit(1)
		}
		return
	}

	runInteractiveMenu()
}
