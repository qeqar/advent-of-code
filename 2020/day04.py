#!/usr/bin/env python

import re

with open('inputs/day04.txt') as f:
    lines = f.read().splitlines()


def validate(ident_entry, ident_value):
    if ident_entry == "byr":
        if 1920 <= int(ident_value) <= 2002:
            return True
    elif ident_entry == "iyr":
        if 2010 <= int(ident_value) <= 2020:
            return True
    elif ident_entry == "eyr":
        if 2020 <= int(ident_value) <= 2030:
            return True
    elif ident_entry == "hgt":
        if ident_value[-2:] == 'cm' and 150 <= int(ident_value[:-2]) <= 193:
            return True
        elif ident_value[-2:] == "in" and 59 <= int(ident_value[:-2]) <= 76:
            return True
    elif ident_entry == "hcl":
        if re.match('^#[0-9a-f]{6}$', ident_value):
            return True
    elif ident_entry == "ecl":
        if ident_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
    elif ident_entry == "pid":
        if re.match('^[0-9]{9}$', ident_value):
            return True
    elif ident_entry == "cid":
        return True

    return False


class Ident:
    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None
    cid = None

    def show(self):
        print(self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid, self.cid)


passports = []
passport = Ident()

for line in lines:
    if line == "":
        passports.append(passport)
        passport = Ident()
    else:
        for entry in line.split(' '):
            ent, value = entry.split(':')
            if ent == "byr":
                if validate(ent, value):
                    if passport.byr is not None:
                        exit(1)
                    else:
                        passport.byr = value
            elif ent == "iyr":
                if validate(ent, value):
                    if passport.iyr is not None:
                        exit(1)
                    else:
                        passport.iyr = value
            elif ent == "eyr":
                if validate(ent, value):
                    if passport.eyr is not None:
                        exit(1)
                    else:
                        passport.eyr = value
            elif ent == "hgt":
                if validate(ent, value):
                    if passport.hgt is not None:
                        exit(1)
                    else:
                        passport.hgt = value
            elif ent == "hcl":
                if validate(ent, value):
                    if passport.hcl is not None:
                        exit(1)
                    else:
                        passport.hcl = value
            elif ent == "ecl":
                if validate(ent, value):
                    if passport.ecl is not None:
                        exit(1)
                    else:
                        passport.ecl = value
            elif ent == "pid":
                if validate(ent, value):
                    if passport.pid is not None:
                        exit(1)
                    else:
                        passport.pid = value
            elif ent == "cid":
                if validate(ent, value):
                    if passport.cid is not None:
                        exit(1)
                    else:
                        passport.cid = value
            else:
                print("NOPE should not happened: " + str(ent))


valid = 0
for passport in passports:
    if passport.byr is not None and passport.iyr is not None and passport.eyr is not None and passport.hgt is not None \
            and passport.hcl is not None and passport.ecl is not None and passport.pid is not None:
        valid += 1
    else:
        passport.show()

print("Valid " + str(valid) + " out of " + str(len(passports)))
