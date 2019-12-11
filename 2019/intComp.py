#!/usr/bin/env python
import threading
import queue


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


class Comp(threading.Thread):
    indicator = 0
    output = 0

    def __init__(self, codes, input_queue, output_queue):
        threading.Thread.__init__(self)
        self.codes = codes
        self.input_queue = input_queue
        self.output_queue = output_queue

    def run(self):
        while self.indicator < len(self.codes):
            if str(self.codes[self.indicator])[-1] == '9':
                #print("reached 99 at " + str(self.indicator) + "\n")
                return self.output
            elif str(self.codes[self.indicator])[-1] == '1':
                self.codes[self.codes[self.indicator + 3]] = value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1) + value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2)
                self.indicator += 4
            elif str(self.codes[self.indicator])[-1] == '2':
                self.codes[self.codes[self.indicator + 3]] = value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1) * value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2)
                self.indicator += 4
            elif str(self.codes[self.indicator])[-1] == '3':
                self.codes[self.codes[self.indicator + 1]] = self.input_queue.get()
                self.indicator += 2
            elif str(self.codes[self.indicator])[-1] == '4':
                self.output = self.codes[self.codes[self.indicator + 1]]
                self.output_queue.put(int(self.output))
                self.indicator += 2
            elif str(self.codes[self.indicator])[-1] == '5':
                if value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1) > 0:
                    self.indicator = value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2)
                else:
                    self.indicator += 3
            elif str(self.codes[self.indicator])[-1] == '6':
                if value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1) == 0:
                    self.indicator = value(self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2)
                else:
                    self.indicator += 3
            elif str(self.codes[self.indicator])[-1] == '7':
                if value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1) < value(
                        self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2):
                    self.codes[self.codes[self.indicator + 3]] = 1
                else:
                    self.codes[self.codes[self.indicator + 3]] = 0
                self.indicator += 4
            elif str(self.codes[self.indicator])[-1] == '8':
                if value(self.codes, parameter_mode(self.codes[self.indicator], 1), self.indicator, 1) == value(
                        self.codes, parameter_mode(self.codes[self.indicator], 2), self.indicator, 2):
                    self.codes[self.codes[self.indicator + 3]] = 1
                else:
                    self.codes[self.codes[self.indicator + 3]] = 0
                self.indicator += 4
            else:
                print("should not happen at " + str(self.indicator) + "\n")
                exit(1)
