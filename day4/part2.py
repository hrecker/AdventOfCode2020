import re

expectedKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
currentPassport = {}
numValid = 0
validEcls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkCurrentPassport():
    global expectedKeys, currentPassport, numValid, validEcls

    if set(expectedKeys).issubset(currentPassport.keys()):
        isValid = True
        byr = int(currentPassport['byr'])
        iyr = int(currentPassport['iyr'])
        eyr = int(currentPassport['eyr'])
        hgt = currentPassport['hgt']
        hcl = currentPassport['hcl']
        ecl = currentPassport['ecl']
        pid = currentPassport['pid']
        if byr < 1920 or byr > 2002:
            isValid = False
        if isValid and (iyr < 2010 or iyr > 2020):
            isValid = False
        if isValid and (eyr < 2020 or eyr > 2030):
            isValid = False
        if isValid:
            hgtVal = int(re.split(r'\D+', hgt)[0])
            hgtUnits = hgt[len(hgt) - 2:]
            if hgtUnits == 'cm':
                if hgtVal < 150 or hgtVal > 193:
                    isValid = False
            elif hgtUnits == 'in':
                if hgtVal < 59 or hgtVal > 76:
                    isValid = False
            else:
                isValid = False
        if isValid:
            if hcl[0] != '#' or len(hcl) != 7:
                isValid = False
            else:
                try:
                    int(hcl[1:], 16)
                except ValueError:
                    isValid = False
        if isValid and ecl not in validEcls:
            isValid = False
        if isValid and len(pid) != 9:
            isValid = False
        if isValid:
            numValid = numValid + 1
    currentPassport.clear()

with open('input.txt') as input:
    for line in input:
        if line.strip():
            for field in line.rstrip('\n').split(' '):
                keyVal = field.split(':')
                currentPassport[keyVal[0]] = keyVal[1]
        else:
            checkCurrentPassport()

if currentPassport:
    checkCurrentPassport()

print(numValid)