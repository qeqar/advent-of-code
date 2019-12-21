#!/usr/bin/env python
import itertools
import queue
import intComp

if __name__ == "__main__":
    codes = intComp.get_codes("07")

    max_phase = ""
    max_output = 0

    phases = itertools.permutations(range(5, 10))
    threads = []

    for phase in phases:
        #print("phase: " + str(phase))
        aQueue = queue.Queue()
        aQueue.put(int(phase[0]))
        aQueue.put(0)
        bQueue = queue.Queue()
        bQueue.put(int(phase[1]))
        cQueue = queue.Queue()
        cQueue.put(int(phase[2]))
        dQueue = queue.Queue()
        dQueue.put(int(phase[3]))
        eQueue = queue.Queue()
        eQueue.put(int(phase[4]))

        aAmp = intComp.Comp(codes.copy(), aQueue, bQueue)
        aAmp.start()
        bAmp = intComp.Comp(codes.copy(), bQueue, cQueue)
        bAmp.start()
        cAmp = intComp.Comp(codes.copy(), cQueue, dQueue)
        cAmp.start()
        dAmp = intComp.Comp(codes.copy(), dQueue, eQueue)
        dAmp.start()
        eAmp = intComp.Comp(codes.copy(), eQueue, aQueue)
        eAmp.start()

        eAmp.join()
        out = aQueue.get_nowait()
        if max_output < out:
            max_output = out
            max_phase = phase

    print("max_ouput %d at phase %s" % (max_output, max_phase))

