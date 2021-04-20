package _020

import (
	"fmt"
	"github.com/qeqar/advent-of-code/pkg/aoc"
)

type Day01Part2 struct{}

func NewDay01Part2() *Day01Part2 {
	return &Day01Part2{}
}

func (f *Day01Part2) Run() error {
	fmt.Print("Challenge from year 2020 day 01 part 2 is implemented inside here")
	return nil
}

func (f *Day01Part2) String() string {
	return "2020Day01Part2"
}

func init() {
	aoc.GetAOCFactory().Register("2020", "01", "2", NewDay01Part2())
}
