#!/usr/bin/env python

with open('inputs/day01.txt') as f:
    lines = f.readlines()

for first in lines:
    first.strip()
    for second in lines:
        second.strip()
        if first != second:
            if int(first) + int(second) == 2020:
                print(int(first) * int(second))


for first in lines:
    first.strip()
    for second in lines:
        second.strip()
        for third in lines:
            third.strip()
            if first != second and first != third and second != third:
                if int(first) + int(second) + int(third)== 2020:
                    print(int(first) * int(second) * int(third))
                    exit(0)
