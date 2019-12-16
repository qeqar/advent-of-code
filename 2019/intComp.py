#!/usr/bin/env python
import threading
import queue


class Comp(threading.Thread):
    indicator = 0
    output = 0
    relative_base = 0

    def __init__(self, codes, input_queue, output_queue):
        threading.Thread.__init__(self)
        self.codes = codes
        self.input_queue = input_queue
        self.output_queue = output_queue

    def parameter_mode(self, param):
        if param == 1:
            p = -3
        elif param == 2:
            p = -4
        elif param == 3:
            p = -5
        else:
            print("wrong parameter for mode")
            exit(1)
        return int(str(self.codes[self.indicator])[p]) if len(str(self.codes[self.indicator])) > param + 1 else 0

    def get_value(self, param, write=False):
        mode = self.parameter_mode(param)
        if mode == 0:  # position mode
            index = self.codes[self.indicator + param]
        elif mode == 1:  # immediate mode
            index = self.indicator + param
        elif mode == 2:  # relative mode
            index = self.relative_base + self.codes[self.indicator + param]
        else:
            print("mode " + str(mode) + " not supported")
            exit(1)
        if write:
            return index
        if index >= len(self.codes):
            return 0
        return self.codes[index]

    def add_value(self, position, value):
        if position >= len(self.codes):
            for _ in range(len(self.codes), position + 1):
                self.codes.append(0)
        self.codes[position] = value
    
    def run(self):
        while self.indicator < len(self.codes):
            opcode = str(self.codes[self.indicator])[-2:].zfill(2)
            if opcode == '99':
                #print("reached 99 at " + str(self.indicator) + "\n")
                return self.output
            elif opcode == '01':
                self.add_value(self.get_value(3, True), self.get_value(1) + self.get_value(2))
                self.indicator += 4
            elif opcode == '02':
                self.add_value(self.get_value(3, True), self.get_value(1) * self.get_value(2))
                self.indicator += 4
            elif opcode == '03':
                self.add_value(self.get_value(1, True), self.input_queue.get())
                self.indicator += 2
            elif opcode == '04':
                self.output = self.get_value(1)
                self.output_queue.put(int(self.output))
                self.indicator += 2
            elif opcode == '05':
                if self.get_value(1) > 0:
                    self.indicator = self.get_value(2)
                else:
                    self.indicator += 3
            elif opcode == '06':
                if self.get_value(1) == 0:
                    self.indicator = self.get_value(2)
                else:
                    self.indicator += 3
            elif opcode == '07':
                if self.get_value(1) < self.get_value(2):
                    self.add_value(self.get_value(3, True), 1)
                else:
                    self.add_value(self.get_value(3, True), 0)
                self.indicator += 4
            elif opcode == '08':
                if self.get_value(1) == self.get_value(2):
                    self.add_value(self.get_value(3, True), 1)
                else:
                    self.add_value(self.get_value(3, True), 0)
                self.indicator += 4
            elif opcode == '09':
                self.relative_base += self.get_value(1)
                self.indicator += 2
            else:
                print("should not happen at " + str(self.indicator) + "\n")
                exit(1)
