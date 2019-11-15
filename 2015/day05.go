package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func main(){
	file, err := os.Open("inputs/day05.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var not = regexp.MustCompile(`ab|cd|pq|xy`)
	var vowels = regexp.MustCompile(`a|e|i|o|u`)
	nice := 0
	nice2 := 0
	for scanner.Scan() {
		isNice := scanner.Text()
		// part1
		if ! not.MatchString(isNice) {
			if len(vowels.FindAllStringIndex(isNice, -1)) >= 3 {
				var c2 string
				for i, c := range isNice {
					if i == 0 {
						c2 = string(c)
						continue
					}
					if string(c) == c2 {
						nice++
						break
					}
					c2 = string(c)
				}
			}
		}
		// part 2
		var c2 string
		var c3 string
		double := make(map[string]int)
		rule1 := 0
		rule2 := 0
		for i, c := range isNice {
			if i == 0 {
				c2 = string(c)
				c3 = string(c)
				continue
			}
			if  i > 1 {
				if c3 == string(c) {
					rule2++
				}
				c3 = c2
			}
			if val, ok := double[ c2 + string(c) ]; ! ok {
				double[c2 + string(c)] = i
			} else {
				if val < i-1 {
					rule1++
				}
			}
			c2 = string(c)
		}
		if rule2 > 0 && rule1 > 0 {
			nice2++
		}
	}
	fmt.Printf("numer of nice: %d\n", nice)
	fmt.Printf("numer2 of nice2: %d", nice2)
}
