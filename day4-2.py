test = ['[1518-11-01 00:00] Guard #10 begins shift\n',
        '[1518-11-01 00:05] falls asleep\n',
        '[1518-11-01 00:25] wakes up\n',
        '[1518-11-01 00:30] falls asleep\n',
        '[1518-11-01 00:55] wakes up\n',
        '[1518-11-02 00:56] Guard #100 begins shift\n',
        '[1518-11-03 23:58] Guard #99 begins shift\n',
        '[1518-11-03 00:40] falls asleep\n',
        '[1518-11-03 00:50] wakes up\n',
        '[1518-11-04 00:05] Guard #10 begins shift\n',
        '[1518-11-04 00:24] falls asleep\n',
        '[1518-11-04 00:29] wakes up\n',
        '[1518-11-05 00:02] Guard #99 begins shift\n',
        '[1518-11-05 00:36] falls asleep\n',
        '[1518-11-05 00:46] wakes up\n',
        '[1518-11-06 00:03] Guard #99 begins shift\n',
        '[1518-11-06 00:45] falls asleep\n',
        '[1518-11-06 00:55] wakes up\n',
        ]


def get_sleep_minutes(payload):
    p = payload.split('\n')
    ip = iter(p)
    sleep_time = {}
    for tik in ip:
        try:
            tok = next(ip)
        except StopIteration:
            continue
        asleep = int(tik.split(' ')[1].split(':')[1].strip(']'))
        awake = int(tok.split(' ')[1].split(':')[1].strip(']'))
        if asleep > awake:
            print("no no no " + str(tik) + ' ' + str(tok))
        for i in range(asleep, awake):
            if i in sleep_time:
                sleep_time[i] += 1
            else:
                sleep_time[i] = 1
    return sleep_time


def main():
    with open('sorted_input4') as f:
            content = f.readlines()

    payload_per_guard = {}
    sleep_time = {}
    guard_id = ""

    for line in content:
        payload = line.split(']')[1].strip()
        #print(guard_id, payload, line)
        if payload.startswith('Guard'):
            guard_id = payload.split(' ')[1].strip('#')
        else:
            if guard_id in payload_per_guard:
                payload_per_guard[guard_id] += line
            else:
                payload_per_guard[guard_id] = line

    #print(payload_per_guard)

    for guard in payload_per_guard:
        if payload_per_guard[guard]:
            sleep_time[guard] = get_sleep_minutes(payload_per_guard[guard])

    #print(sleep_time)

    best_minute = 0
    max_minute = 0
    guard_id_max = 0

    for guard in sleep_time:
        for minute, num_minute in sleep_time[guard].items():
                #print(minute, num_minute, max_minute, best_minute, guard)
                if num_minute > max_minute:
                    max_minute = num_minute
                    best_minute = minute
                    guard_id_max = guard


    print(guard_id_max, best_minute, max_minute)

    now = int(guard_id_max) * int(best_minute)

    print(now)


if __name__ == '__main__':
    main()
