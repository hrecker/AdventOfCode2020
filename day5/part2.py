numRows = 128
numColumns = 8
seatIds = []

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

        seatIds.append(8 * row + col)

seatIds.sort()
minSeatId = seatIds[0]
for index, seatId in enumerate(seatIds):
    if seatId != minSeatId + index:
        print(seatId - 1)
        exit()

print("Open seat not found")