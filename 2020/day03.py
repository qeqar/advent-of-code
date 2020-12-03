#!/usr/bin/env python

with open('inputs/day03.txt') as f:
    lines = f.readlines()

slops = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

mtrees = []
for slope in slops:
    right = slope[0]
    down = slope[1]
    trees = 0
    x = 0
    y = 0
    length = len(lines[1]) - 1  # we need to get rid of the new line

    while y < len(lines) - 1:
        x += right
        y += down
        if lines[y][x % length] == '#':
            trees += 1
    mtrees.append(trees)

multiple = 1
for i in mtrees:
    multiple = multiple * i

print(multiple)
