package _022

import (
	"fmt"
	"github.com/qeqar/advent-of-code/pkg/aoc"
	"github.com/qeqar/advent-of-code/pkg/utils"
	"strconv"
)

type Day01Part1 struct{}

func NewDay01Part1() *Day01Part1 {
	return &Day01Part1{}
}

func (f *Day01Part1) Run() error {
	callories := 0
	maxCallories := 0
	content := utils.FileScanner("2022", "1")
	for content.Scan() {
		if content.Text() == "" {
			if callories > maxCallories {
				maxCallories = callories
			}
			callories = 0
		} else {
			c, _ := strconv.Atoi(content.Text())
			callories += c
		}
	}
	fmt.Printf("MaxCallories: %d", maxCallories)
	return nil
}

func (f *Day01Part1) String() string {
	return "2022Day01Part1"
}

func init() {
	aoc.GetAOCFactory().Register("2022", "01", "1", NewDay01Part1())
}
