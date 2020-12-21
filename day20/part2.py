import copy
import math

tilePositions = []
tiles = {}
north = 0
east = 1
south = 2
west = 3

seaMonster1 = "                  # "
seaMonster2 = "#    ##    ##    ###"
seaMonster3 = " #  #  #  #  #  #   "

def getOppositeDirection(dir):
    return (dir + 2) % 4

def printTile(id):
    printLines(tiles[id]["lines"])

def printLines(lines):
    for line in lines:
        print(*line, sep="")

def addTile(id, tileLines):
    global tiles
    tiles[id] = {}
    tiles[id]["lines"] = tileLines
    tiles[id]["neighbors"] = []
    tiles[id]["shared"] = []

def getBaseBorders(id):
    lines = tiles[id]["lines"]
    # Order borders N, E, S, W
    return [lines[0], ''.join([l[9] for l in lines]), lines[9], ''.join([l[0] for l in lines])]

def getAllPossibleBorders(id):
    base = getBaseBorders(id)
    all = copy.deepcopy(base)
    for border in base:
        all.append(border[::-1])
    return all

def rotateLines(lines):
    return [''.join([l[i] for l in lines[::-1]]) for i in range(len(lines))]

def rotateTile(id):
    tiles[id]["lines"] = rotateLines(tiles[id]["lines"])
    tiles[id]["shared"] = [(x + 1) % 4 for x in tiles[id]["shared"]]

def flipLines(lines):
    return lines[::-1]

def flipTile(id):
    tiles[id]["lines"] = flipLines(tiles[id]["lines"])
    for index, share in enumerate(tiles[id]["shared"]):
        if share in [0, 2]:
            tiles[id]["shared"][index] = (share + 2) % 4

def coordInMap(x, y):
    return x >= 0 and y >= 0 and x < imageWidth and y < imageWidth

def findTilePositions(processedTiles, iter):
    if iter > (imageWidth - 1) * 2:
        return

    global tilePositions
    # Handle the first iteration from the top left corner
    if iter == 1:
        topLeft = tilePositions[0][0]
        borders = getBaseBorders(topLeft)
        eastBorder = borders[east]
        eastNeighbor = tiles[topLeft]["neighbors"][0]
        southNeighbor = tiles[topLeft]["neighbors"][1]
        # Determine which neighbor belongs east and which belongs south
        if eastBorder not in getAllPossibleBorders(eastNeighbor):
            temp = eastNeighbor
            eastNeighbor = southNeighbor
            southNeighbor = temp
        tilePositions[1][0] = southNeighbor
        processedTiles.append(southNeighbor)
        findTileOrientation(topLeft, southNeighbor, south)
        tilePositions[0][1] = eastNeighbor
        processedTiles.append(eastNeighbor)
        findTileOrientation(topLeft, eastNeighbor, east)
    else:
        # First iterate over tiles that have to align with two neighbors
        for x in range(1, iter):
            y = iter - x
            if not coordInMap(x, y):
                continue
            west = tilePositions[y][x - 1]
            north = tilePositions[y - 1][x]
            # There should be exactly one tile that is in common between the north and west neighbors
            common = set([n for n in tiles[west]["neighbors"] if n not in processedTiles]) \
                & set([n for n in tiles[north]["neighbors"] if n not in processedTiles])
            newTile = common.pop()
            tilePositions[y][x] = newTile
            processedTiles.append(newTile)
            findTileOrientation(west, newTile, east)
        # Next set border tiles that only need to align with one neighbor
        if coordInMap(0, iter):
            # North border of the full image
            westNeighbor = tilePositions[0][iter - 1]
            tilePositions[0][iter] = [n for n in tiles[westNeighbor]["neighbors"] if n not in processedTiles][0]
            processedTiles.append(tilePositions[0][iter])
            findTileOrientation(westNeighbor, tilePositions[0][iter], east)

            # West border of the full image
            northNeighbor = tilePositions[iter - 1][0]
            tilePositions[iter][0] = [n for n in tiles[northNeighbor]["neighbors"] if n not in processedTiles][0]
            processedTiles.append(tilePositions[iter][0])
            findTileOrientation(northNeighbor, tilePositions[iter][0], south)

    findTilePositions(processedTiles, iter + 1)

# Flip or rotate the new tile as necessary to line up with the existing tile
def findTileOrientation(existing, new, dir):
    expectedBorder = getBaseBorders(existing)[dir]
    expectedDir = getOppositeDirection(dir)
    for flip in range(2):
        for rot in range(4):
            if getBaseBorders(new)[expectedDir] == expectedBorder:
                return
            rotateTile(new)
        if flip == 0:
            flipTile(new)

def removeTileBorders(id):
    tiles[id]["lines"] = [line[1:9] for line in tiles[id]["lines"][1:9]]

def buildFinalImage(tilePositions, tileWidth, includeGaps):
    finalImage = []
    for x in range(len(tilePositions)):
        for y in range(len(tilePositions)):
            tileId = tilePositions[y][x]
            lines = tiles[tileId]["lines"]
            for lineY in range(len(lines)):
                index = (y * tileWidth) + lineY
                if len(finalImage) <= index:
                    finalImage.append("")
                finalImage[index] += tiles[tileId]["lines"][lineY]
                if includeGaps:
                    finalImage[index] += ' '
    # Add gaps for output that is easier to compare to the sample
    if includeGaps:
        for y in reversed(range(len(tilePositions))):
            finalImage.insert(y * tileWidth, [' '] * tileWidth * imageWidth)
    return finalImage

def getSeaMonsterHashesAt(image, x, y):
    hashes = []
    for dx in range(len(seaMonster1)):
        if seaMonster1[dx] == '#':
            if image[y][x + dx] == '#':
                hashes.append((x + dx, y))
            else:
                return []
    for dx in range(len(seaMonster2)):
        if seaMonster2[dx] == '#':
            if image[y + 1][x + dx] == '#':
                hashes.append((x + dx, y + 1))
            else:
                return []
    for dx in range(len(seaMonster3)):
        if seaMonster3[dx] == '#':
            if image[y + 2][x + dx] == '#':
                hashes.append((x + dx, y + 2))
            else:
                return []
    #print("sea monster found at: (" + str(x) + ", " + str(y) + ")")
    return hashes

def getSeaMonsterHashes(image):
    global markedMonsters
    hashes = [[False] * len(image)] * len(image)
    anyMonsters = False
    for x in range(len(image) - len(seaMonster1) + 1):
        for y in range(len(image) - 2):
            for hx, hy in getSeaMonsterHashesAt(image, x, y):
                hashes[hy][hx] = True
                markedMonsters[hy] = markedMonsters[hy][:hx] + 'O' + markedMonsters[hy][hx + 1:]
                anyMonsters = True
    if not anyMonsters:
        return []
    return hashes

def countHashes(markedMonsters):
    nonMonsterHashCount = 0
    for x in range(len(final)):
        for y in range(len(final)):
            if markedMonsters[y][x] == '#':
                nonMonsterHashCount += 1
    return nonMonsterHashCount

with open("C:/Users/henry/AdventOfCode2020/day20/input.txt") as input:
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
            addTile(tileId, tile)
    addTile(tileId, tile)

# Get all possible neighbors for each tile
borderCount = {}
for id1 in tiles:
    borderCount[id1] = 0
    borders1 = getBaseBorders(id1)
    for id2 in tiles:
        if id1 != id2:
            borders2 = getAllPossibleBorders(id2)
            shared = 0
            for dir in [north, east, south, west]:
                if borders1[dir] in borders2:
                    shared += 1
                    tiles[id1]["shared"].append(dir)
            borderCount[id1] += shared
            if shared > 0:
                tiles[id1]["neighbors"].append(id2)

# Find the corners
corners = []
for id in borderCount:
    if borderCount[id] == 2:
        corners.append(id)

imageWidth = int(math.sqrt(len(tiles)))
tilePositions = [[-1] * imageWidth for i in range(imageWidth)]
tilePositions[0][0] = corners[0]

# Rotate the top left corner correctly, so that its shared borders are east and south
while 1 not in tiles[corners[0]]["shared"] or 2 not in tiles[corners[0]]["shared"]:
    #print("rotatin")
    rotateTile(corners[0])

findTilePositions([corners[0]], 1)
print("Final tile positions")
for row in tilePositions:
    print(str(row))

#print()
#print("Final image")
#printLines(buildFinalImage(tilePositions, 10, False))

# Remove borders for final image
for tile in tiles:
    removeTileBorders(tile)

#print()
#print("Borders removed")
final = buildFinalImage(tilePositions, 8, False)
#printLines(final)

print()
print("Checking for sea monsters")
# Flip and rotate the full image until seamonsters are found
for flip in range(2):
    for rot in range(4):
        markedMonsters = copy.deepcopy(final)
        hashes = getSeaMonsterHashes(final)
        if not hashes:
            #print("none found")
            final = rotateLines(final)
        else:
            print()
            #print("DONE!")
            printLines(markedMonsters)
            print(countHashes(markedMonsters))
            exit(0)
    if flip == 0:
        final = flipLines(final)

print()
print("None found at all, so this probably isn't right")
print(countHashes(final))
