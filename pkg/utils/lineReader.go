package utils

import (
	"bufio"
	"fmt"
	"os"
)

func FileScanner(year, input string) *bufio.Scanner {
	file, err := os.Open(fmt.Sprintf("./inputs/%s/input%s", year, input))
	if err != nil {
		panic(err)
	}
	scanner := bufio.NewScanner(file)
	return scanner
}
