iters = 30000000
currentIter = 0
spoken = []
lastSeen = {}

with open("input.txt") as input:
    line = input.readline().strip('\n')
    for val in line.split(','):
        spoken.append(int(val))
        lastSeen[int(val)] = currentIter + 1
        currentIter += 1

while currentIter < iters:
    #print(str(lastSeen))
    #print(str(spoken))
    #print()
    last = spoken[-1]
    val = 0
    if last in lastSeen:
        val = (currentIter) - lastSeen[last]
        #print("last index: " + str(getLastIndex(last, spoken[:-1])))
    #spoken.append((currentIter) - (int(getLastIndex(last, spoken[:-1])) + 1))
    spoken.append(val)
    lastSeen[last] = currentIter
    currentIter += 1
    #if currentIter % 10000 == 0:
    #    print("iter: " + str(currentIter))

#print("final spoken: " + str(spoken))
print("result: " + str(spoken[-1]))