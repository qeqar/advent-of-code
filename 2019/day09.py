#!/usr/bin/env python
import queue
import intComp

if __name__ == "__main__":
    with open('inputs/day09.txt') as f:
        instruction = f.read()
    codes = list(map(int, instruction.split(",")))

    inQueue = queue.Queue()
    inQueue.put(1)
    outQueue = queue.Queue()

    computer = intComp.Comp(codes.copy(), inQueue, outQueue)
    computer.start()
    computer.join()
    print("part1: " + str(outQueue.get_nowait()))
