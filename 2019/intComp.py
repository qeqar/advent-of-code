#!/usr/bin/env python
import threading
import queue


def parameter_mode(opcode, param):
    if param == 1:
        p = -3
    elif param == 2:
        p = -4
    elif param == 3:
        p = -5
    else:
        print("wrong parameter for mode")
        exit(1)
    return int(str(opcode)[p]) if len(str(opcode)) > param + 1 else 0


def get_value(codes, mode, i, param, rbase):
    if mode == 0:  # position mode
        index = codes[i + param]
    elif mode == 1:  # immediate mode
        index = i + param
    elif mode == 2:  # relative mode
        index = codes[i + param] + rbase
    else:
        print("mode " + str(mode) + " not supported")
        exit(1)
    if index >= len(codes):
        return 0
    return codes[index]


def add_value(codes, position, value):
    if position >= len(codes):
        for _ in range(len(codes), position + 1):
            codes.append(0)
    codes[position] = value


class Comp(threading.Thread):
    indicator = 0
    output = 0
    relative_base = 0

    def __init__(self, codes, input_queue, output_queue):
        threading.Thread.__init__(self)
        self.codes = codes
        self.input_queue = input_queue
        self.output_queue = output_queue

    def run(self):
        while self.indicator < len(self.codes):
            opcode = str(self.codes[self.indicator])[-2:].zfill(2)
            print("opcodes " + opcode)
            if opcode == '99':
                # print("reached 99 at " + str(self.indicator) + "\n")
                return self.output
            elif opcode == '01':
                add_value(self.codes, self.codes[get_value(self.codes, parameter_mode(self.codes[self.indicator], 3), self.indicator, 3, self.relative_base)], get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base) + get_value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2, self.relative_base))
                self.indicator += 4
            elif opcode == '02':
                add_value(self.codes, self.codes[get_value(self.codes, parameter_mode(self.codes[self.indicator], 3), self.indicator, 3, self.relative_base)], get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base) * get_value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2, self.relative_base))
                self.indicator += 4
            elif opcode == '03':
                add_value(self.codes, self.codes[get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base)], self.input_queue.get())
                self.indicator += 2
            elif opcode == '04':
                self.output = get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base)
                self.output_queue.put(int(self.output))
                self.indicator += 2
            elif opcode == '05':
                if get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base) > 0:
                    self.indicator = get_value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2, self.relative_base)
                else:
                    self.indicator += 3
            elif opcode == '06':
                if get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base) == 0:
                    self.indicator = get_value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2, self.relative_base)
                else:
                    self.indicator += 3
            elif opcode == '07':
                if get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base) < get_value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2, self.relative_base):
                    add_value(self.codes, self.codes[get_value(self.codes, parameter_mode(self.codes[self.indicator], 3), self.indicator, 3, self.relative_base)], 1)
                else:
                    add_value(self.codes, self.codes[get_value(self.codes, parameter_mode(self.codes[self.indicator], 3), self.indicator, 3, self.relative_base)], 0)
                self.indicator += 4
            elif opcode == '08':
                if get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base) == get_value(
                        self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2, self.relative_base):
                    add_value(self.codes, self.codes[get_value(self.codes, parameter_mode(self.codes[self.indicator], 3), self.indicator, 3, self.relative_base)], 1)
                else:
                    add_value(self.codes, self.codes[get_value(self.codes, parameter_mode(self.codes[self.indicator], 3), self.indicator, 3, self.relative_base)], 0)
                self.indicator += 4
            elif opcode == '09':
                self.relative_base += get_value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1, self.relative_base)
                self.indicator += 2
            else:
                print("should not happen at " + str(self.indicator) + "\n")
                exit(1)
