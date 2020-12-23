moves = 100
cupGroupSize = 3
currentCupIndex = 0
cupIndices = {}
cups = []

def getNextTarget(currentTarget, cups):
    nextTarget = currentTarget - 1
    if nextTarget == 0:
        nextTarget = max(cups)
    return nextTarget

def move(cups, cupIndices, currentCupIndex):
    currentCup = cups[currentCupIndex]
    moveGroupIndices = [(currentCupIndex + i) % len(cups) for i in range(1, cupGroupSize + 1)]
    moveGroupCups = [cups[i] for i in moveGroupIndices]
    moveGroupIndices.sort()
    targetIndex = -1
    target = getNextTarget(currentCup, cups)
    while targetIndex == -1:
        if target not in moveGroupCups:
            targetIndex = cupIndices[target]
        else:
            target = getNextTarget(target, cups)
    
    for i in reversed(range(cupGroupSize)):
        cups.insert(targetIndex + 1, moveGroupCups[i])

    for i in reversed(range(cupGroupSize)):
        toDelete = moveGroupIndices[i]
        if targetIndex < toDelete:
            toDelete += cupGroupSize
        del cups[toDelete]

    for i, cup in enumerate(cups):
        cupIndices[cup] = i
    
    nextCupIndex = cupIndices[currentCup] + 1
    nextCupIndex = nextCupIndex % len(cups)

    return cups, cupIndices, nextCupIndex

def getResult(cups, cupIndices):
    startingIndex = (cupIndices[1] + 1) % len(cups)
    result = []
    for i in range(len(cups) - 1):
        index = (startingIndex + i) % len(cups)
        result.append(str(cups[index]))
    return "".join(result)

with open("C:/users/henry/adventofcode2020/day23/input.txt") as input:
    cups = [int(c) for c in input.readline().strip('\n')]
    for index, c in enumerate(cups):
        cupIndices[c] = index

#print("Initial")
#print(str(cups))
#print(str(cupIndices))
for i in range(1, moves + 1):
    cups, cupIndices, currentCupIndex = move(cups, cupIndices, currentCupIndex)
    #print()
    #print("After move " + str(i))
    #print(str(cups))
    #print("current cup: " + str(cups[currentCupIndex]))

#print()
print(getResult(cups, cupIndices))
