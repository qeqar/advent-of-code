package _022

import (
	"fmt"
	"github.com/qeqar/advent-of-code/pkg/aoc"
	"github.com/qeqar/advent-of-code/pkg/utils"
	"sort"
	"strconv"
)

type Day01Part2 struct{}

func NewDay01Part2() *Day01Part2 {
	return &Day01Part2{}
}

func (f *Day01Part2) Run() error {
	callories := 0
	var cals []int
	content := utils.FileScanner("2022", "1")
	for content.Scan() {
		c, _ := strconv.Atoi(content.Text())
		if content.Text() == "" {
			cals = append(cals, callories)
			callories = 0
		} else {
			callories += c
		}
	}
	sort.Ints(cals)
	solution := cals[len(cals)-1] + cals[len(cals)-2] + cals[len(cals)-3]
	fmt.Println(solution)
	return nil
}

func (f *Day01Part2) String() string {
	return "2022Day01Part2"
}

func init() {
	aoc.GetAOCFactory().Register("2022", "01", "2", NewDay01Part2())
}
