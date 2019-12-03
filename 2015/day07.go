package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

type wireDefinition struct{
	idenifier string
	signal uint16
}

func inArray(a string, list []wireDefinition) bool {
	for _, t := range list {
		if t.idenifier == a {
			return true
		}
	}
	return false
}

func main() {
	file, err := os.Open("inputs/day07.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var wires []wireDefinition
	for scanner.Scan() {
		instruction := scanner.Text()
		fmt.Printf("instruction %s\n", instruction)
		target := strings.Split(instruction, "->")
		if ! inArray(target[len(target)-1], wires) {
			wires = append(wires, wireDefinition{target[len(target)-1], 0})
		}
	}
	fmt.Println(wires)
}
