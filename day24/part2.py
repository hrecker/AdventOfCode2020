import copy

blackTiles = {}
numDays = 100

e = 0
w = 1
n = 2
s = 3

def normalize(dirCounts):
    if dirCounts[e] > dirCounts[w]:
        dirCounts[e] = dirCounts[e] - dirCounts[w]
        dirCounts[w] = 0
    else:
        dirCounts[w] = dirCounts[w] - dirCounts[e]
        dirCounts[e] = 0
    
    if dirCounts[n] > dirCounts[s]:
        dirCounts[n] = dirCounts[n] - dirCounts[s]
        dirCounts[s] = 0
    else:
        dirCounts[s] = dirCounts[s] - dirCounts[n]
        dirCounts[n] = 0

    normalized = ""
    for i in range(dirCounts[e]):
        normalized += 'e'
    for i in range(dirCounts[s]):
        normalized += 's'
    for i in range(dirCounts[w]):
        normalized += 'w'
    for i in range(dirCounts[n]):
        normalized += 'n'
    return normalized

def getDirCounts(normalizedCoord):
    dirCounts = [0] * 4
    dirCounts[e] = normalizedCoord.count('e')
    dirCounts[s] = normalizedCoord.count('s')
    dirCounts[w] = normalizedCoord.count('w')
    dirCounts[n] = normalizedCoord.count('n')
    return dirCounts

def getNormAdjacentTiles(normalizedCoord):
    dirCounts = getDirCounts(normalizedCoord)
    newDirs = []
    newDirs.append(copy.deepcopy(dirCounts))
    newDirs.append(copy.deepcopy(dirCounts))
    newDirs.append(copy.deepcopy(dirCounts))
    newDirs.append(copy.deepcopy(dirCounts))
    newDirs.append(copy.deepcopy(dirCounts))
    newDirs.append(copy.deepcopy(dirCounts))
    
    newDirs[0][e] += 2

    newDirs[1][e] += 1
    newDirs[1][s] += 2

    newDirs[2][w] += 1
    newDirs[2][s] += 2

    newDirs[3][w] += 2

    newDirs[4][w] += 1
    newDirs[4][n] += 2

    newDirs[5][e] += 1
    newDirs[5][n] += 2

    return [normalize(dirs) for dirs in newDirs]

def getTilesToCheck(blackTiles):
    tilesToCheck = set()
    for tile in blackTiles:
        tilesToCheck.add(tile)
        for neighbor in getNormAdjacentTiles(tile):
            tilesToCheck.add(neighbor)
    return tilesToCheck

def countAdjacentBlackTiles(blackTiles, tile):
    count = 0
    for neighbor in getNormAdjacentTiles(tile):
        if neighbor in blackTiles:
            count += 1
    return count

with open("C:/users/henry/adventofcode2020/day24/input.txt") as input:
    for line in input:
        line = line.strip('\n')
        normalizedCoord = ""
        dirCounts = [0] * 4
        i = 0
        while i < len(line):
            if line[i] in ['e', 'w']:
                if line[i] == 'e':
                    dirCounts[e] += 2
                elif line[i] == 'w':
                    dirCounts[w] += 2
                else:
                    print("invalid single char direction: " + line[i])
                    exit(1)
                i += 1
            else:
                if line[i:i+2] == 'se':
                    dirCounts[s] += 2
                    dirCounts[e] += 1
                elif line[i:i+2] == 'sw':
                    dirCounts[s] += 2
                    dirCounts[w] += 1
                elif line[i:i+2] == 'nw':
                    dirCounts[n] += 2
                    dirCounts[w] += 1
                elif line[i:i+2] == 'ne':
                    dirCounts[n] += 2
                    dirCounts[e] += 1
                else:
                    print("invalid two char direction: " + line[i:i+2])
                    exit(1)
                i += 2
        
        normalizedCoord = normalize(dirCounts)
        
        if normalizedCoord in blackTiles:
            del blackTiles[normalizedCoord]
        else:
            blackTiles[normalizedCoord] = True

day = 1
while day < numDays + 1:
    print("Day " + str(day))
    origBlackTiles = copy.deepcopy(blackTiles)
    for tile in getTilesToCheck(origBlackTiles):
        blackAdjacent = countAdjacentBlackTiles(origBlackTiles, tile)
        if tile in origBlackTiles and (blackAdjacent == 0 or blackAdjacent > 2):
            del blackTiles[tile]
        elif blackAdjacent == 2:
            blackTiles[tile] = True
    day += 1

print(str(len(blackTiles)))
