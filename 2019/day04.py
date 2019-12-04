#!/usr/bin/env python

good_codes = []
for _code in range(372304, 847060):
    code = [int(i) for i in str(_code)]
    double = False
    decrease = True
    c1 = code[1]
    c2 = code[0]
    for i in range(2, 6):
        if i == 2:
            if c2 > c1:
                print("no match: " + str(code))
                decrease = False
                break
            if c2 == c1 and not c1 == code[i]:
                double = True
        if c1 > code[i]:
            print("no match: " + str(code))
            decrease = False
            break
        if c1 == code[i]:
            if not c1 == c2:
                if i == 5:
                    double = True
                elif not code[i] == code[i+1]:
                    double = True
        c2 = c1
        c1 = code[i]
    if double and decrease:
        good_codes.append(str(_code))

print(len(good_codes))

