#!/usr/bin/env python
import re
import sys

with open('inputs/day03.txt') as f:
    wire_pathes = f.readlines()

grids = []
for wire_path in wire_pathes:
    x = 0
    y = 0
    grid = []
    for move in wire_path.split(","):
        direction = re.sub("[0-9]", "", move)
        distance = int(re.sub("[A-Z]", "", move))
        if direction == "U":
            for i in range(distance):
                y += 1
                grid.append((x, y))
        elif direction == "D":
            for i in range(distance):
                y -= 1
                grid.append((x, y))
        elif direction == "R":
            for i in range(distance):
                x += 1
                grid.append((x, y))
        elif direction == "L":
            for i in range(distance):
                x -= 1
                grid.append((x, y))
        else:
            print("wtf")
            print(move)
    grids.append(grid)

shortest_manhatten_distance = sys.maxsize
print(shortest_manhatten_distance)

for point in grids[0]:
    if point in grids[1]:
        manhatten = abs(point[0]) + abs(point[1])
        if shortest_manhatten_distance > manhatten:
            shortest_manhatten_distance = manhatten

print(shortest_manhatten_distance)


