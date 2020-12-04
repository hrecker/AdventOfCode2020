from functools import reduce

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

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
treeCounts = [0] * len(slopes)
for rowIndex, row in enumerate(terrain):
    for slopeIndex, slope in enumerate(slopes):
        if rowIndex % slope[1] == 0 and row[(slope[0] * int(rowIndex / slope[1])) % len(row)]:
            treeCounts[slopeIndex] = treeCounts[slopeIndex] + 1

for slopeIndex, slope in enumerate(slopes):
    print("Slope " + str(slope) + ": " + str(treeCounts[slopeIndex]))

print("Result: " + str(reduce(lambda x, y: x*y, treeCounts)))