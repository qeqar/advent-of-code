with open('input6') as f:
    content = f.read().splitlines()

test = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']
cordinates = []
calc_cordinates = {}
max_x = 0
max_y = 0

for cordinate in content:
    x, y = cordinate.split(",")
    cordinates.append((int(x), int(y)))
    if int(x) > max_x:
        max_x = int(x)
    if int(y) > max_y:
        max_y = int(y)

#max_x += 1
#max_y += 1
print(max_x)
print(max_y)
print(cordinates)

for box_x in range(0, max_x):
    for box_y in range(0, max_y):
        dest = (box_x, box_y)
        #print("\ndestination: " + str(box_x) + "," + str(box_y))
        distance = abs(max_x + max_y)
        all_dist = []
        for cor in cordinates:
            all_dist.append(abs(box_x - cor[0]) + abs(box_y - cor[1]))
        calc_cordinates[dest] = sum(all_dist)

print(calc_cordinates)

dist_area = 0
for cor in calc_cordinates:
    if calc_cordinates[cor] < 10000:
        dist_area += 1

print(dist_area)
