#!/usr/bin/env python
import queue
import intComp
from PIL import Image


def goto(direction, turn):
    if turn == 0:
        direction += 90
    elif turn == 1:
        direction -= 90
    else:
        print("no not that direction: " + turn)
        exit(1)
    if direction < 0:
        direction += 360
    if direction > 360:
        direction -= 360
    return direction


def set_color(panel, x, y, color):
    for p in panel:
        if p[0] == (x, y):
            panel[(x, y)] = color
            return
    panel.append((x, y), color)


if __name__ == "__main__":
    codes = intComp.get_codes("11")
    panel = {}
    x = 0
    y = 0
    color = True
    direction = 0
    inQueue = queue.Queue()
    inQueue.put(1)
    outQueue = queue.Queue()

    computer = intComp.Comp(codes.copy(), inQueue, outQueue)
    computer.start()

    while computer.is_alive():
        out = outQueue.get()
        if color:
            panel[(x, y)] = out
            color = False
        else:
            direction = goto(direction, out)
            if direction == 0 or direction == 360:
                y += 1
            elif direction == 90:
                x += 1
            elif direction == 180:
                y -= 1
            elif direction == 270:
                x -= 1
            else:
                print("nope not that direction: " + direction)
            inQueue.put(panel[(x, y)] if (x, y) in panel else 0)
            color = True

    print("number of panels: " + str(len(panel)))

    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0

    for p in panel.keys():
        if p[0] < min_x:
            min_x = p[0]
        elif p[0] > max_x:
            max_x = p[0]
        if p[1] < min_y:
            min_y = p[1]
        elif p[1] > max_y:
            max_y = p[1]
    px = abs(min_x) + max_x +1
    py = abs(min_y) + max_y +1

    img = Image.new('1', (px, py), "black")
    pixel_map = img.load()

    for p in panel.keys():
        pixel_map[p[0] + abs(min_x), p[1] + abs(min_y)] = panel[p]

    img.show()
