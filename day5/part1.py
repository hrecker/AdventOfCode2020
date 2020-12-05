maxSeatId = 0
numRows = 128
numColumns = 8

with open('input.txt') as input:
    for line in input:
        row = 0
        col = 0

        bounds = (0, numRows - 1)
        for i in range(7):
            diff = int((bounds[1] - bounds[0] + 1) / 2)
            if line[i] == 'B':
                bounds = (bounds[0] + diff, bounds[1])
            else:
                bounds = (bounds[0], bounds[1] - diff)
        row = bounds[0]

        bounds = (0, numColumns - 1)
        for i in range(7, 10):
            diff = int((bounds[1] - bounds[0] + 1) / 2)
            if line[i] == 'R':
                bounds = (bounds[0] + diff, bounds[1])
            else:
                bounds = (bounds[0], bounds[1] - diff)
        col = bounds[0]

        maxSeatId = max(8 * row + col, maxSeatId)

print(maxSeatId)