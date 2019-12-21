#!/usr/bin/env python
import queue
import intComp

if __name__ == "__main__":
    codes = intComp.get_codes("09")

    part = 2
    inQueue = queue.Queue()
    inQueue.put(part)
    outQueue = queue.Queue()

    computer = intComp.Comp(codes.copy(), inQueue, outQueue)
    computer.start()
    computer.join()
    print("solution part: " + str(part) + ": " + str(outQueue.get_nowait()))
