expectedKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
currentPassportKeys = []
numValid = 0
with open('input.txt') as input:
    for line in input:
        if line.strip():
            for field in line.split(' '):
                currentPassportKeys.append(field.split(':')[0])
        else:
            if set(expectedKeys).issubset(currentPassportKeys):
                numValid = numValid + 1
            currentPassportKeys.clear()

print(numValid)