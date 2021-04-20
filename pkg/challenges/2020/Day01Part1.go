package _020

import (
	"fmt"
	"github.com/qeqar/advent-of-code/pkg/aoc"
)

type Day01Part1 struct{}

func NewDay01Part1() *Day01Part1 {
	return &Day01Part1{}
}

func (f *Day01Part1) Run() error {
	fmt.Print("Challenge from year 2020 day 1 part 1 is implemented inside here")
	return nil
}

func (f *Day01Part1) String() string {
	return "2020Day01Part1"
}

func init() {
	aoc.GetAOCFactory().Register("2020", "01", "1", NewDay01Part1())
}
