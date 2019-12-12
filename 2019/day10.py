#!/usr/bin/env python
import math


def check_distance(see, asteroid, distance, miss):
    if not see:
        return (asteroid, distance)
    elif see[1] > distance:
        miss.append(see[0])
        return (asteroid, distance)
    else:
        miss.append(asteroid)
        return see


def manhattan_distance(a, a1):
    return abs(a1[0] - a[0]) + abs(a1[1] - a[1])


def calc_angle(a, a1):
    gegenkathete = abs(a1[1]) - abs(a[1])
    ankathete = abs(a1[0]) - abs(a[0])
    hypotenuse = math.sqrt(gegenkathete * gegenkathete + ankathete * ankathete)
    angle = round(math.degrees(gegenkathete / hypotenuse), 2)
    return angle


def check_angle(see, asteroid, angle, distance, miss):
    new_angle = {"coordinate": asteroid,
                 "angle": angle,
                 "distance": distance}
    if len(see) == 0:
        see.append(new_angle)
        return
    same_angle = list(filter(lambda see: see['angle'] == angle, see))
    if len(same_angle) == 0:
        see.append(new_angle)
    elif len(same_angle) == 1:
        if distance < same_angle[0]['distance']:
            see.append(new_angle)
            see.remove(same_angle[0])
            miss.append(same_angle[0]['coordinate'])
        else:
            miss.append(asteroid)
    else:
        print("nope that should not happen")
        print(see, same_angle, asteroid)
        exit(1)


with open('inputs/day10.txt') as f:
    lines = f.readlines()

max_y = len(lines) - 1
max_x = len(lines[0]) - 1
asteroids_coordinates = []
max_asteroids = 0
max_asteroid_coordinate = ()

for y in range(len(lines)):
    line = lines[y].strip()
    for x in range(len(line)):
        a = line[x].strip()
        if a == "#":
            asteroids_coordinates.append((x, y))

num_of_asteroid = len(asteroids_coordinates)

for asteroid in asteroids_coordinates:
    #print(asteroid)
    same_x_y_plus = ()
    same_x_y_minus = ()
    same_y_x_plus = ()
    same_y_x_minus = ()
    xy_plus = []
    xy_minus = []
    x_plus_y_minus = []
    x_minus_y_plus = []
    miss = []
    for a in asteroids_coordinates:
        if asteroid == a:
            continue
        if asteroid[0] == a[0]:  # same x-axis
            if a[1] - asteroid[1] > 0:  # same x y+
                same_x_y_plus = check_distance(same_x_y_plus, a, a[1] - asteroid[1], miss)
            else:  # same x y-
                same_x_y_minus = check_distance(same_x_y_minus, a, abs(a[1] - asteroid[1]), miss)
        elif asteroid[1] == a[1]:  # same y-axis
            if a[0] - asteroid[0] > 0:  # same y x+
                same_y_x_plus = check_distance(same_y_x_plus, a, a[0] - asteroid[0], miss)
            else:  # same y x-
                same_y_x_minus = check_distance(same_y_x_minus, a, abs(a[0] - asteroid[0]), miss)
        elif a[0] - asteroid[0] > 0:  # x+
            if a[1] - asteroid[1] > 0:  # xy+
                check_angle(xy_plus, a, calc_angle(asteroid, a), manhattan_distance(asteroid, a), miss)
            else:   # x+y-
                check_angle(x_plus_y_minus, a, calc_angle(asteroid, a), manhattan_distance(asteroid, a), miss)
        elif a[0] - asteroid[0] < 0:  # x-
            if a[1] - asteroid[1] < 0:  # xy-
                check_angle(xy_minus, a, calc_angle(asteroid, a), manhattan_distance(asteroid, a), miss)
            else:  # x-y+
                check_angle(x_minus_y_plus, a, calc_angle(asteroid, a), manhattan_distance(asteroid, a), miss)

    assert len(same_x_y_plus) < 3, same_x_y_plus
    assert len(same_x_y_minus) < 3, same_x_y_minus
    assert len(same_y_x_plus) < 3, same_y_x_plus
    assert len(same_y_x_minus) < 3, same_y_x_minus

    run_num_asteroids = len(xy_plus) + len(xy_minus) + len(x_plus_y_minus) + len(x_minus_y_plus)
    if same_x_y_plus:
        run_num_asteroids += 1
    if same_x_y_minus:
        run_num_asteroids += 1
    if same_y_x_plus:
        run_num_asteroids += 1
    if same_y_x_minus:
        run_num_asteroids += 1

    assert len(miss) + run_num_asteroids + 1 == num_of_asteroid,\
        str(run_num_asteroids) + " " + str(len(miss)) + " " + str(num_of_asteroid)

    if run_num_asteroids > max_asteroids:
        max_asteroids = run_num_asteroids
        max_asteroid_coordinate = asteroid

print("max number of asteroids: " + str(max_asteroids))
print("at coordinate: " + str(max_asteroid_coordinate))
