import copy

cubes = {}
xBounds = (0, 0)
yBounds = (0, 0)
zBounds = (0, 0)
iters = 6

with open("input.txt") as input:
    y = 0
    for l in input:
        line = l.strip('\n')
        x = 0
        while x < len(line):
            coord = (x, y, 0)
            cubes[coord] = line[x]
            x += 1
        y += 1
    xBounds = (0, x)
    yBounds = (0, y)

def countActiveNeighbors(x, y, z, cubes):
    active = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            for dz in [-1, 0, 1]:
                if dx != 0 or dy != 0 or dz != 0:
                    coord = (x + dx, y + dy, z + dz)
                    if coord in cubes and cubes[coord] == '#':
                        active += 1
    return active

currentIter = 0
while currentIter < iters:
    originalCubes = copy.deepcopy(cubes)

    x = xBounds[0] - 1
    while x <= xBounds[1] + 1:
        y = yBounds[0] - 1
        while y <= yBounds[1] + 1:
            z = zBounds[0] - 1
            while z <= zBounds[1] + 1:
                coord = (x, y, z)
                active = coord in cubes and originalCubes[coord] == '#'
                activeNeighbors = countActiveNeighbors(x, y, z, originalCubes)
                if active and activeNeighbors not in [2, 3]:
                    cubes[coord] = '.'
                if not active and activeNeighbors == 3:
                    cubes[coord] = '#'

                z += 1
            y += 1
        x += 1

    xBounds = (xBounds[0] - 1, xBounds[1] + 1)
    yBounds = (yBounds[0] - 1, yBounds[1] + 1)
    zBounds = (zBounds[0] - 1, zBounds[1] + 1)

    currentIter += 1

count = 0
for cube in cubes.values():
    if cube == '#':
        count += 1

print(count)
