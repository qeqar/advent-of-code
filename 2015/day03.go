package main

import (
	"fmt"
	"io/ioutil"
)

type house struct {
	x int
	y int
}

func inArray(a house, list []house) bool {
	for _, t := range list {
		if t == a {
			return true
		}
	}
	return false
}

func main() {
	content, err := ioutil.ReadFile("inputs/day03.txt")
	if err != nil {
		panic(err)
	}
	santa := true
	var houses []house
	var houses2 []house

	x := 0
	y := 0
	xs := 0
	xr := 0
	ys := 0
	yr := 0
	houses = append(houses, house{x, y})
	houses2 = append(houses2, house{x, y})

	for _, direction := range content {
		if direction == '>' {
			x++
			if santa {
				xs++
			} else if ! santa {
				xr++
			}
		} else if direction == '<' {
			x--
			if santa {
				xs--
			} else if ! santa {
				xr--
			}
		} else if direction == '^' {
			y++
			if santa {
				ys++
			} else if !santa {
				yr++
			}
		} else if direction == 'v' {
			y--
			if santa {
				ys--
			} else if !santa {
				yr--
			}
		}
		if !inArray(house{x, y}, houses) {
			houses = append(houses, house{x, y})
		}

		if santa {
			if !inArray(house{xs, ys}, houses2) {
				houses2 = append(houses2, house{xs, ys})
			}
		} else if !santa {
			if !inArray(house{xr, yr}, houses2) {
				houses2 = append(houses2, house{xr, yr})
			}
		}
		santa = !santa
	}
	fmt.Printf("Number of houses: %d\n", len(houses))
	fmt.Printf("Number of houses2: %d", len(houses2))
}
