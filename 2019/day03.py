#!/usr/bin/env python
import re
import sys

with open('inputs/day03.txt') as f:
    wire_pathes = f.readlines()

#wire_pathes = ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51",
#               "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]

grids = []
for wire_path in wire_pathes:
    x = 0
    y = 0
    grid = []
    for move in wire_path.split(","):
        move = move.rstrip()
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
shortest_step_distance = sys.maxsize
print(shortest_manhatten_distance)

index = 0 # it is faster as to add a second grids[0].index(point)
for point in grids[0]:
    if point in grids[1]:
        manhatten = abs(point[0]) + abs(point[1])
        if shortest_manhatten_distance > manhatten:
            shortest_manhatten_distance = manhatten
        steps = grids[1].index(point) + index + 2
        if shortest_step_distance > steps:
            shortest_step_distance = steps
    index += 1

print("Manhatten: " + str(shortest_manhatten_distance))
print("Steps: " + str(shortest_step_distance))


