#!/usr/bin/env python

with open('inputs/day02.txt') as f:
    input = f.read()

codes = list(map(int, input.split(",")))
clear_codes = codes.copy()
codes[1] = 12
codes[2] = 2
i = 0

while i < len(codes):
    if codes[i] == 99:
        print("reached 99 at " + str(i))
        break
    elif codes[i] == 1:
        codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
    elif codes[i] == 2:
        codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
    else:
        print("schould not happen at " + str(i) + "\n")
    i += 4

print(codes)

for noun in range(100):
    for verb in range(100):
        i = 0
        actual_codes = clear_codes.copy()
        actual_codes[1] = noun
        actual_codes[2] = verb
        while i < len(actual_codes):
            if actual_codes[i] == 99:
                break
            elif actual_codes[i] == 1:
                actual_codes[actual_codes[i+3]] = actual_codes[actual_codes[i+1]] + actual_codes[actual_codes[i+2]]
            elif actual_codes[i] == 2:
                actual_codes[actual_codes[i+3]] = actual_codes[actual_codes[i+1]] * actual_codes[actual_codes[i+2]]
            else:
                print("schould not happen at " + str(i) + "\n")
            i += 4
        if actual_codes[0] == 19690720:
            print("part2: " + str(100 * noun + verb))
            exit(0)
