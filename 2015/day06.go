package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func allPoints(points []string) []string {
	corner1 := strings.Split(points[0], ",")
	corner2 := strings.Split(points[1], ",")
	c11, _ := strconv.Atoi(corner1[0])
	c12, _ := strconv.Atoi(corner1[1])
	c21, _ := strconv.Atoi(corner2[0])
	c22, _ := strconv.Atoi(corner2[1])
	var allPoints []string
	for i := c11; i <= c21; i++ {
		for y := c12; y <= c22; y++ {
			point := strconv.Itoa(i) + "," + strconv.Itoa(y)
			allPoints = append(allPoints, point)
		}
	}
	return allPoints
}

func getPoint(point string) [2]int {
	po := strings.Split(point, ",")
	p1, _ := strconv.Atoi(po[0])
	p2, _ := strconv.Atoi(po[1])
	return [2]int{p1, p2}
}

func main() {
	file, err := os.Open("inputs/day06.txt.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)

	var lights [1000][1000]int
	var brightnessLights [1000][1000]int

	for scanner.Scan() {
		command := scanner.Text()
		r := regexp.MustCompile(`[0-9]+,[0-9]+`)
		points := r.FindAllString(command, -1)
		all := allPoints(points)
		if strings.HasPrefix(command, "turn on") {
			for _, p := range all {
				a := getPoint(p)
				lights[a[0]][a[1]] = 1
				brightnessLights[a[0]][a[1]] = brightnessLights[a[0]][a[1]] +1
			}
		}
		if strings.HasPrefix(command, "turn off") {
			for _, p := range all {
				a := getPoint(p)
				lights[a[0]][a[1]] = 0
				brightnessLights[a[0]][a[1]] = brightnessLights[a[0]][a[1]] -1

				if brightnessLights[a[0]][a[1]] < 0 {
					brightnessLights[a[0]][a[1]] = 0
				}
			}
		}
		if strings.HasPrefix(command, "toggle") {
			for _, p := range all {
				a := getPoint(p)
				if lights[a[0]][a[1]] == 0 {
					lights[a[0]][a[1]] = 1
				} else {
					lights[a[0]][a[1]] = 0
				}
				brightnessLights[a[0]][a[1]] = brightnessLights[a[0]][a[1]] +2
			}
		}
	}
	count := 0
	for _, a := range lights {
		for _, l := range a {
			count = count + l
		}
	}
	brightness := 0
	for _, a := range brightnessLights {
		for _, l := range a {
			brightness = brightness + l
		}
	}

	fmt.Printf("lit lights: %d\n", count)
	fmt.Printf("brightnessLights: %d\n", brightness)
}
