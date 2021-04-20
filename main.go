package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/qeqar/advent-of-code/pkg/aoc"
	// import year folder to register all created challenges of that year
	_ "github.com/qeqar/advent-of-code/pkg/challenges/2020"
)

func main() {
	// TODO: add checks for valid values like. only year that i already started, and 2 digit days, and on 1 or 2 in part
	var year = flag.String("year", "", "choose year full year")
	var day = flag.String("day", "", "choose day in 2 digit format")
	var part = flag.String("part", "", "choose part only 1 or 2")
	flag.Parse()

	factory := aoc.GetAOCFactory()
	aocChallenge := factory.Get(*year, *day, *part)
	if aocChallenge == nil {
		fmt.Printf("Challenge %s %s %s not jet coded\n", *year, *day, *part)
		os.Exit(1)
	}

	fmt.Printf("Executing challenge: %s\n", aocChallenge)

	err := aocChallenge.Run()
	if err != nil {
		fmt.Printf("Failed: %v\n", err)
	}
}
