#!/usr/bin/env python

with open('inputs/day08.txt') as f:
    lines = f.read().splitlines()


def instruction(op, arg, i, acc):
    if op == "acc":
        acc += int(arg)
        i += 1
    elif op == "jmp":
        i += int(arg)
    elif op == "nop":
        i += 1
    return i, acc


outer_index = 0
run_complete = False

for instruction_line in lines:

    if instruction_line.startswith("acc"):
        outer_index += 1
        continue

    index = 0
    accumulator = 0
    operations_done = []
    new_code = lines.copy()

    if lines[outer_index].startswith("jmp"):
        new_code[outer_index] = "nop " + lines[outer_index].split(' ')[1]
    else:
        new_code[outer_index] = "jmp " + lines[outer_index].split(' ')[1]

    while True:
        operation, argument = new_code[index].split(' ')
        index, accumulator = instruction(operation, argument, index, accumulator)
        if index >= len(new_code):
            run_complete = True
            break
        elif index in operations_done:
            break
        else:
            operations_done.append(index)

    if run_complete:
        print(accumulator)
        break
    outer_index += 1


