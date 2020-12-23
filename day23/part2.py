moves = 10000000
numCups = 1000000
cupGroupSize = 3
cups = {}
currentCup = -1

prev = 0
val = 1
next = 2

def move(cups, currentCup):
    currentCupNode = cups[currentCup]
    moveGroupCups = []
    moveGroupCups.append(currentCupNode[next])
    for i in range(cupGroupSize - 1):
        moveGroupCups.append(cups[moveGroupCups[i]][next])
    
    target = currentCup - 1
    if target == 0:
        target = numCups
    while target in moveGroupCups:
        target -= 1
        if target == 0:
            target = numCups
    
    afterMoveGroup = cups[moveGroupCups[-1]][next]
    currentCupNode[next] = afterMoveGroup
    cups[afterMoveGroup][prev] = currentCup

    afterTarget = cups[target][next]
    cups[moveGroupCups[-1]][next] = cups[target][next]
    cups[target][next] = moveGroupCups[0]
    cups[afterTarget][prev] = moveGroupCups[-1]
    cups[moveGroupCups[0]][prev] = target

    return cups, currentCupNode[next]

def getResult(cups):
    next1 = cups[1][next]
    next2 = cups[next1][next]
    return next1 * next2

def addCup(cups, lastCup, newCup):
    if lastCup != -1:
        cups[lastCup][next] = newCup
    newCupNode = [lastCup, newCup, 0]
    cups[newCup] = newCupNode
    return newCupNode

def getCupString(cups, start):
    cup = start
    result = ""
    while str(cup) not in result:
        result += str(cup)
        cup = cups[cup][next]
    return result

def getReverseCupString(cups, start):
    cup = start
    result = ""
    while str(cup) not in result:
        result += str(cup)
        cup = cups[cup][prev]
    return result[::-1]

with open("C:/users/henry/adventofcode2020/day23/input.txt") as input:
    lastCup = -1
    for c in input.readline().strip('\n'):
        newCup = int(c)
        addCup(cups, lastCup, newCup)
        lastCup = newCup
        if currentCup == -1:
            currentCup = newCup
    for c in range(max(cups) + 1, numCups + 1):
        newCup = int(c)
        addCup(cups, lastCup, newCup)
        lastCup = newCup
    # Connect the ends
    cups[currentCup][prev] = lastCup
    cups[lastCup][next] = currentCup

#print("Initial")
#print(getCupString(cups, currentCup))
#print(getReverseCupString(cups, cups[currentCup][prev]))
#exit()

for i in range(1, moves + 1):
    #if i % 1000 == 0:
    #    print("move " + str(i))
    cups, currentCup = move(cups, currentCup)
    #print()
    #print("After move " + str(i))
    #print(getCupString(cups, currentCup))
    #print(getReverseCupString(cups, cups[currentCup][prev]))
    #print("current cup: " + str(currentCup))

print(getResult(cups))
