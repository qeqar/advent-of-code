#!/busr/bin/env python

import re

with open('inputs/day04.txt') as f:
    lines = f.read().splitlines()


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

    def validate(self, ident_entry, ident_value):
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
            if ident_value.startswith('#') and re.match('[0-9a-f]{6}', ident_value[1:]):
                return True
        elif ident_entry == "ecl":
            if ident_value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return True
        elif ident_entry == "pid":
            if re.match('[0-9]{9}', ident_value):
                return True
        elif ident_entry == "cid":
            return True

        return False


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
                if passport.validate(ent, value):
                    passport.byr = value
            elif ent == "iyr":
                if passport.validate(ent, value):
                    passport.iyr = value
            elif ent == "eyr":
                if passport.validate(ent, value):
                    passport.eyr = value
            elif ent == "hgt":
                if passport.validate(ent, value):
                    passport.hgt = value
            elif ent == "hcl":
                if passport.validate(ent, value):
                    passport.hcl = value
            elif ent == "ecl":
                if passport.validate(ent, value):
                    passport.ecl = value
            elif ent == "pid":
                if passport.validate(ent, value):
                    passport.pid = value
            elif ent == "cid":
                if passport.validate(ent, value):
                    passport.cid = value
            else:
                print("NOPE should not happened: " + str(ent))


valid = 0
for passport in passports:
    if passport.byr is not None and passport.iyr is not None and passport.eyr is not None and passport.hgt is not None \
            and passport.hcl is not None and passport.ecl is not None and passport.pid is not None:
        valid += 1

print("Part1 valid " + str(valid) + " out of " + str(len(passports)))

