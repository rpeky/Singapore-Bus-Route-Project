package main

import (
	"fmt"
	"log"
)

func main() {
	fmt.Println("Starting")

	if err := EnsureDataDirs(); err != nil {
		log.Fatal(err)
	}

	fmt.Println("Finished checking dirs")
}
