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
    data = {"area": 0,
            "edge": False}
    calc_cordinates[(int(x), int(y))] = data
    if int(x) > max_x:
        max_x = int(x)
    if int(y) > max_y:
        max_y = int(y)

print(max_x)
print(max_y)
print(cordinates)
#print(calc_cordinates)

for box_x in range(0, max_x):
    for box_y in range(0, max_y):
        #print("\ndestination: " + str(box_x) + "," + str(box_y))
        nearest_cor = ()
        distance = abs(max_x + max_y)
        all_dist = []
        double = False
        for cor in cordinates:
            man_dist = abs(box_x - cor[0]) + abs(box_y - cor[1])
            all_dist.append(man_dist)
            if man_dist < distance:
                distance = man_dist
                nearest_cor = cor
        #print(all_dist)
        if len(list(filter(lambda x: x == distance, all_dist))) > 1:
            double = True
        #print("nearest distance " + str(distance))
        #print("nearest cordinate " + str(nearest_cor))
        #print("but is double " + str(double))
        if not double:
            calc_cordinates[nearest_cor]["area"] += 1
            if box_x == 1:
                calc_cordinates[nearest_cor]["edge"] = True
            if box_y == max_y:
                calc_cordinates[nearest_cor]["edge"] = True

print(calc_cordinates)

biggest_area = 0
bcor = ()
for ccor, value in calc_cordinates.items():
    if not value["edge"]:
        if value["area"] > biggest_area:
            biggest_area = value["area"]
            bcor = ccor

print(bcor)
print(biggest_area)
