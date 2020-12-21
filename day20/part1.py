import copy

tiles = {}

def getBaseBorders(id):
    lines = tiles[id]
    return [lines[0], ''.join([l[9] for l in lines]), lines[9], ''.join([l[0] for l in lines])]

def getAllPossibleBorders(id):
    base = getBaseBorders(id)
    all = copy.deepcopy(base)
    for border in base:
        all.append(border[::-1])
    return all

with open("input.txt") as input:
    tileId = 0
    tile = []
    for line in input:
        line = line.strip('\n')
        if "Tile" in line:
            tileId = int(line[5:9])
            tile = []
        elif line:
            tile.append(line)
        else:
            tiles[tileId] = tile
    tiles[tileId] = tile

borderCount = {}
for id1 in tiles:
    borderCount[id1] = 0
    borders1 = getAllPossibleBorders(id1)
    for id2 in tiles:
        if id1 != id2:
            borders2 = getAllPossibleBorders(id2)
            borderCount[id1] += len(set(borders1) & set(borders2)) // 2

result = 1
for id in borderCount:
    if borderCount[id] == 2:
        result *= id
print(result)
