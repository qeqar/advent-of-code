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


with open('inputs/day05.txt') as f:
    instruction = f.read()

codes = list(map(int, instruction.split(",")))
i = 0
system_id = 1

while i < len(codes):
    if str(codes[i])[-1] == '9':
        print("reached 99 at " + str(i))
        break
    elif str(codes[i])[-1] == '1':
        codes[codes[i+3]] = value(codes, parameter_mode(codes[i], 1), i, 1) + value(codes, parameter_mode(codes[i], 2), i, 2)
        i += 4
    elif str(codes[i])[-1] == '2':
        codes[codes[i+3]] = value(codes, parameter_mode(codes[i], 1), i, 1) * value(codes, parameter_mode(codes[i], 2), i, 2)
        i += 4
    elif str(codes[i])[-1] == '3':
        codes[codes[i+1]] = system_id
        i += 2
    elif str(codes[i])[-1] == '4':
        print(codes[codes[i+1]])
        i += 2
    elif str(codes[i])[-1] == '5':
        if value(codes, parameter_mode(codes[i], 1), i, 1) > 0:
            i = value(codes, parameter_mode(codes[i], 2), i, 2)
        else:
            i += 3
    elif str(codes[i])[-1] == '6':
        if value(codes, parameter_mode(codes[i], 1), i, 1) == 0:
            i = value(codes, parameter_mode(codes[i], 2), i, 2)
        else:
            i += 3
    elif str(codes[i])[-1] == '7':
        if value(codes, parameter_mode(codes[i], 1), i, 1) < value(codes, parameter_mode(codes[i], 2), i, 2):
            codes[codes[i+3]] = 1
        else:
            codes[codes[i+3]] = 0
        i += 4
    elif str(codes[i])[-1] == '8':
        if value(codes, parameter_mode(codes[i], 1), i, 1) == value(codes, parameter_mode(codes[i], 2), i, 2):
            codes[codes[i+3]] = 1
        else:
            codes[codes[i+3]] = 0
        i += 4
    else:
        print("schould not happen at " + str(i) + "\n")
        exit(1)

print(codes)