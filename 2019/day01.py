#!/usr/bin/env python
import math

with open('inputs/day01.txt') as f:
    masses = f.readlines()
fuel1 = 0
fuel2 = 0

for mass in masses:
    f = math.floor(int(mass) / 3) - 2
    fuel1 += f
    fuel2 += f
    while f > 0:
        f = math.floor(f / 3) - 2
        if f > 0:
            fuel2 += f

print(str(fuel1) + "\n")
print(fuel2)
