#!/usr/bin/env python

import collections

with open('inputs/day06.txt') as f:
    lines = f.read().splitlines()

yes_count = 0
yes_count2 = 0
group = ""
group_count = 0

for line in lines:
    if line == "":
        yes_count += len(set(group))
        group_result = collections.Counter(group)
        for r in group_result.values():
            if r == group_count:
                yes_count2 += 1
        group = ""
        group_count = 0
    else:
        group += line
        group_count += 1

print("part1 " + str(yes_count))
print("part2 " + str(yes_count2))
