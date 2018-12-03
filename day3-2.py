
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

    for first_line in content:
        has_double = False
        first_id = first_line.split(' ')[0]

        start_left, start_top = first_line.split(' ')[2].split(',')
        start_top = start_top[0:-1]
        left, top = first_line.split(' ')[3].split('x')
        first_points = get_all_points(int(start_left), int(start_top), int(left), int(top))
        for second_line in content:
                second_id = second_line.split(' ')[0]
                if first_id == second_id:
                    continue

                #print(first_id + ":" + second_id)
                start_left, start_top = second_line.split(' ')[2].split(',')
                start_top = start_top[0:-1]
                left, top = second_line.split(' ')[3].split('x')

                second_points = get_all_points(int(start_left), int(start_top), int(left), int(top))
                if not first_points.isdisjoint(second_points):
                    has_double = True

        if has_double:
            continue
        else:
            print(first_id)
            exit(0)


if __name__ == '__main__':
    main()
