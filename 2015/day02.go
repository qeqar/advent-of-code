package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("inputs/day02.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)



	totalSquare := 0
	totalRibbon := 0

	for scanner.Scan() {

		dimensions := strings.Split(string(scanner.Text()), "x")

		lenght, _ := strconv.Atoi(dimensions[0])
		with, _ := strconv.Atoi(dimensions[1])
		hight, _ := strconv.Atoi(dimensions[2])

		totalSquare += (2 * lenght * with) + (2 * with * hight) + (2 * hight * lenght)
		totalRibbon += lenght * with * hight

		dimensions_int := []int{lenght, with, hight}
		sort.Ints(dimensions_int)
		totalSquare += dimensions_int[0] * dimensions_int[1]
		totalRibbon += (2*dimensions_int[0]) + (2*dimensions_int[1])

	}
	if err := scanner.Err(); err != nil {
        panic(err)
    }
	fmt.Printf("Total_square: %d\nTotal_ribbon %d\n", totalSquare, totalRibbon)
}
