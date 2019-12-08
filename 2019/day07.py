#!/usr/bin/env python


def parameter_mode(opcode, param):
    if param == 1:
        p = -3
    elif param == 2:
        p = -4
    else:
        print("wrong parameter for mode")
        exit(1)
    return int(str(opcode)[p]) if len(str(opcode)) > param + 1 else 0


def value(codes, mode, i, param):
    return codes[codes[i + param]] if not int(mode) else codes[i + param]


with open('inputs/day07.txt') as f:
    instruction = f.read()

codes = list(map(int, instruction.split(",")))
clear_codes = codes.copy()

max_phase = ""
phases = []

for p0 in range(0, 5):
    for p1 in range(0, 5):
        if p1 == p0:
            continue
        for p2 in range(0, 5):
            if p2 == p1 or p2 == p0:
                continue
            for p3 in range(0, 5):
                if p3 == p2 or p3 == p1 or p3 == p0:
                    continue
                for p4 in range(0, 5):
                    if p4 == p3 or p4 == p2 or p4 == p1 or p4 == p0:
                        continue
                    phases.append(str(p0) + str(p1) + str(p2) + str(p3) + str(p4))

print(phases)
max_output = 0

for phase in phases:
    print("phase: " + phase)
    last_amp_input = 0
    for p in phase:
        print(p)
        print("last_amp: " + str(last_amp_input))
        actual_codes = clear_codes.copy()
        act_output = 0
        amp_input = 0
        i = 0
        while i < len(actual_codes):
            if str(actual_codes[i])[-1] == '9':
                print("reached 99 at " + str(i))
                break
            elif str(actual_codes[i])[-1] == '1':
                actual_codes[actual_codes[i+3]] = value(actual_codes, parameter_mode(actual_codes[i], 1), i, 1) + value(actual_codes, parameter_mode(actual_codes[i], 2), i, 2)
                i += 4
            elif str(actual_codes[i])[-1] == '2':
                actual_codes[actual_codes[i+3]] = value(actual_codes, parameter_mode(actual_codes[i], 1), i, 1) * value(actual_codes, parameter_mode(actual_codes[i], 2), i, 2)
                i += 4
            elif str(actual_codes[i])[-1] == '3':
                print("Input: " + str(p))
                actual_codes[actual_codes[i+1]] = int(p)
                p = last_amp_input
                i += 2
            elif str(actual_codes[i])[-1] == '4':
                amp_input = actual_codes[actual_codes[i+1]]
                print("Amp_input " + str(amp_input))
                i += 2
            elif str(actual_codes[i])[-1] == '5':
                if value(actual_codes, parameter_mode(actual_codes[i], 1), i, 1) > 0:
                    i = value(actual_codes, parameter_mode(actual_codes[i], 2), i, 2)
                else:
                    i += 3
            elif str(actual_codes[i])[-1] == '6':
                if value(actual_codes, parameter_mode(actual_codes[i], 1), i, 1) == 0:
                    i = value(actual_codes, parameter_mode(actual_codes[i], 2), i, 2)
                else:
                    i += 3
            elif str(actual_codes[i])[-1] == '7':
                if value(actual_codes, parameter_mode(actual_codes[i], 1), i, 1) < value(actual_codes, parameter_mode(actual_codes[i], 2), i, 2):
                    actual_codes[actual_codes[i+3]] = 1
                else:
                    actual_codes[actual_codes[i+3]] = 0
                i += 4
            elif str(actual_codes[i])[-1] == '8':
                if value(actual_codes, parameter_mode(actual_codes[i], 1), i, 1) == value(actual_codes, parameter_mode(actual_codes[i], 2), i, 2):
                    actual_codes[actual_codes[i+3]] = 1
                else:
                    actual_codes[actual_codes[i+3]] = 0
                i += 4
            else:
                print("schould not happen at " + str(i) + "\n")
                exit(1)
        last_amp_input = amp_input

    print("phase output " + str(last_amp_input))
    if max_output < last_amp_input:
        max_output = last_amp_input
        max_phase = phase

print("Max Output: " + str(max_output) + " Max Phase: " + max_phase)
