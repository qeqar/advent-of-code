#!/usr/bin/env python

import math


with open('inputs/day05.txt') as f:
    lines = f.read().splitlines()


def get_row(l):
    min_row = 0
    max_row = 127
    for c in l:
        if c == 'F':
            max_row = min_row + math.floor((max_row - min_row) / 2)
        elif c == 'B':
            min_row = max_row - math.floor((max_row - min_row) / 2)
        else:
            print("Nope " + c + " " + l)
            exit(1)
    return min_row


def get_seat(s):
    min_seat = 0
    max_seat = 7
    for c in s:
        if c == 'L':
            max_seat = min_seat + math.floor((max_seat - min_seat) / 2)
        elif c == 'R':
            min_seat = max_seat - math.floor((max_seat - min_seat) / 2)
        else:
            print("Nope " + c + " " + s)
            exit(1)
    return min_seat


seat_id = 0
seat_list = []

for line in lines:
    row = get_row(line[:7])
    seat = get_seat(line[-3:])

    sid = (int(row) * 8) + int(seat)
    seat_list.append(sid)
    if sid > seat_id:
        seat_id = sid

print(seat_id)
seat_list = sorted(seat_list)

# missed edge case fist and last possible seat
for s in range(len(seat_list) - 1):
    if seat_list[s + 1] - seat_list[s] != 1:
        print(seat_list[s] + 1)

