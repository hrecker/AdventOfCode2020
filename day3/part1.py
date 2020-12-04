terrain = []
with open('input.txt') as input:
    for line in input:
        row = []
        for char in line:
            if char == '#':
                row.append(True)
            elif char == '.':
                row.append(False)
        terrain.append(row)

xPos = 0
treeCount = 0
for row in terrain:
    if row[xPos]:
        treeCount = treeCount + 1
    xPos = (xPos + 3) % len(row)

print(treeCount)