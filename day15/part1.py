iters = 2020
currentIter = 0
spoken = []

with open("input.txt") as input:
    line = input.readline().strip('\n')
    for val in line.split(','):
        spoken.append(int(val))
        currentIter += 1

# Thanks stackoverflow
def getLastIndex(val, list):
    for i in reversed(range(len(list))):
        if list[i] == val:
            return i
    raise ValueError("{} is not in list".format(val))
    
while currentIter < iters:
    last = spoken[-1]
    if last not in spoken[:-1]:
        spoken.append(0)
    else:
        #print("last index: " + str(getLastIndex(last, spoken[:-1])))
        spoken.append((currentIter) - (int(getLastIndex(last, spoken[:-1])) + 1))
    currentIter += 1

print(spoken[-1])