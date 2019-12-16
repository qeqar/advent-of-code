#!/usr/bin/env python
import queue
import intComp

if __name__ == "__main__":
    with open('inputs/day09.txt') as f:
        instruction = f.read()

    #instruction = "104,1125899906842624,99"
    #instruction = "1102,34915192,34915192,7,4,7,99,0"
    #instruction = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    codes = list(map(int, instruction.split(",")))

    inQueue = queue.Queue()
    inQueue.put(1)
    outQueue = queue.Queue()

    computer = intComp.Comp(codes.copy(), inQueue, outQueue)
    computer.start()
    computer.join()
    print(outQueue.get_nowait())
