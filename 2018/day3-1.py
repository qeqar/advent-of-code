
test = ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']


def get_all_points(start_left, start_top, left, top):
    points = set()
    for i in range(left):
        for y in range(top):
            l = start_left + i +1
            t = start_top + y +1
            points.add(str(l) + "x" + str(t))
    return points


def main():
    with open('input3') as f:
        content = f.readlines()

    used_points = set()
    multi_points = set()
    for line in content:
        start_left, start_top = line.split(' ')[2].split(',')
        start_top = start_top[0:-1]
        left, top = line.split(' ')[3].split('x')

        test_points = get_all_points(int(start_left), int(start_top), int(left), int(top))
        for tp in test_points:
            if tp in used_points:
                multi_points.add(tp)
            else:
                used_points.add(tp)

    #print(used_points)
    #print(multi_points)
    print(len(multi_points))

if __name__ == '__main__':
    main()
