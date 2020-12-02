#!/usr/bin/env python

with open('inputs/day02.txt') as f:
    lines = f.readlines()

correct_part_1 = 0
correct_part_2 = 0

for line in lines:
    minimum = int((line.split(' ')[0]).split('-')[0])
    maximum = int((line.split(' ')[0]).split('-')[1])
    c = (line.split(' ')[1])[0]
    password = line.split(' ')[2]
    occurrence = password.count(c)

    if minimum <= occurrence <= maximum:
        correct_part_1 += 1

    if (password[minimum - 1] == c and not password[maximum - 1] == c) \
            or (password[maximum - 1] == c and not password[minimum - 1] == c):
        correct_part_2 += 1

print("part 1: " + str(correct_part_1))
print("part 2: " + str(correct_part_2))
