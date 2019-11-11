package main

import (
	"fmt"
	"io/ioutil"
)

func main() {
	content, err := ioutil.ReadFile("inputs/day01.txt")
	if err != nil {
		panic(err)
	}
	basement := false
	sum := 0
	for i, c := range string(content) {
		if c == '(' {
			sum++
		} else if c == ')' {
			sum--
		} else {
			panic(c)
		}
		if !basement {
			if sum < 0 {
				basement = true
				fmt.Printf("Part 2: at %d\n", i+1)
			}
		}
	}
	fmt.Printf("Part 1: Floor %d", sum)

}
