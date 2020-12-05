import re

expectedKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
currentPassport = {}
numValid = 0
validEcls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkPassport(passport):
    global expectedKeys, numValid, validEcls

    if set(expectedKeys).issubset(passport.keys()):
        byr = int(passport['byr'])
        iyr = int(passport['iyr'])
        eyr = int(passport['eyr'])
        hgt = passport['hgt']
        hcl = passport['hcl']
        ecl = passport['ecl']
        pid = passport['pid']
        if byr < 1920 or byr > 2002:
            return False
        if iyr < 2010 or iyr > 2020:
            return False
        if eyr < 2020 or eyr > 2030:
            return False
        hgtVal = int(re.split(r'\D+', hgt)[0])
        hgtUnits = hgt[len(hgt) - 2:]
        if hgtUnits == 'cm':
            if hgtVal < 150 or hgtVal > 193:
                return False
        elif hgtUnits == 'in':
            if hgtVal < 59 or hgtVal > 76:
                return False
        else:
            return False
        if hcl[0] != '#' or len(hcl) != 7:
            return False
        else:
            try:
                int(hcl[1:], 16)
            except ValueError:
                return False
        if ecl not in validEcls:
            return False
        if len(pid) != 9:
            return False
    else:
        return False
    return True

with open('input.txt') as input:
    for line in input:
        if line.strip():
            for field in line.rstrip('\n').split(' '):
                keyVal = field.split(':')
                currentPassport[keyVal[0]] = keyVal[1]
        else:
            if checkPassport(currentPassport):
                numValid += 1
            currentPassport.clear()

if currentPassport:
    if checkPassport(currentPassport):
        numValid += 1

print(numValid)