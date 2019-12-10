#!/usr/bin/env python

import sys
import re
from PIL import Image

with open('inputs/day08.txt') as f:
    pixel = f.read()

number_of_pixel_per_layer = 25 * 6
min_zeros = sys.maxsize
min_layer_index = sys.maxsize
layers = [pixel[i:i+number_of_pixel_per_layer] for i in range(0, len(pixel), number_of_pixel_per_layer)]

if not len(layers[-1]) == number_of_pixel_per_layer:
    print("last layer not complete")
    exit(1)

for i in range(len(layers)):
    zeros = re.findall('0', layers[i])
    if len(zeros) < min_zeros:
        min_zeros = len(zeros)
        min_layer_index = i

print("Solution Part1: " + str(len(re.findall('1', layers[min_layer_index])) * len(re.findall('2', layers[min_layer_index]))))

color_pixel = ""
for p in range(number_of_pixel_per_layer):
    for l in range(len(layers)):
        if not layers[l][p] == '2':
            color_pixel += layers[l][p]
            break


color_array = [color_pixel[i:i+25] for i in range(0, len(color_pixel), 25)]
img = Image.new('1', (24, 6), "black")
pixel_map = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixel_map[i, j] = 1 - int(color_array[j][i])

img.show()
