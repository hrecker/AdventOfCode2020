
cardPub = 0
doorPub = 0
maxLoopCheck = 2048
transform7Cache = {}

def transform(subject, loopSize):
    maxCached = 0
    if subject == 7:
        if loopSize in transform7Cache:
            return transform7Cache[loopSize]
        else:
            maxCached = len(transform7Cache)

    if maxCached > 1:
        value = transform7Cache[maxCached]
    else:
        value = 1
    
    for i in range(maxCached, loopSize):
        value *= subject
        value = value % 20201227
        if subject == 7:
            transform7Cache[i + 1] = value
    return value

with open("C:/users/henry/adventofcode2020/day25/input.txt") as input:
    cardPub = int(input.readline())
    doorPub = int(input.readline())

# Get card loop
cardLoop = -1
currentCheck = 2
while True:
    transformed = transform(7, currentCheck)
    if transformed == cardPub:
        cardLoop = currentCheck
        break
    else:
        currentCheck += 1
print("card loop: " + str(cardLoop))

# Get door loop
doorLoop = -1
currentCheck = 2
while True:
    transformed = transform(7, currentCheck)
    if transformed == doorPub:
        doorLoop = currentCheck
        break
    else:
        currentCheck += 1
print("door loop: " + str(doorLoop))

print(str(transform(cardPub, doorLoop)))