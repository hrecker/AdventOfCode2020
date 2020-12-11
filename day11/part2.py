seats = []
fill = 0
empty = 1
floor = 2

def getState(char):
    if char == 'L':
        return empty
    elif char == '.':
        return floor
    elif char == '#':
        return fill
        
def getChar(seat):
    if seat == empty:
        return 'L'
    elif seat == floor:
        return '.'
    elif seat == fill:
        return '#'

def printSeats():
    for row in seats:
        print(str([getChar(s) for s in row]))

def isValidCoord(x, y):
    return x >= 0 and y >= 0 and x < len(seats) and y < len(seats[0])

def countVisibleOccupied(x, y):
    occupied = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                seatFound = False
                dist = 1
                while not seatFound:
                    checkX = x + (dist * dx)
                    checkY = y + (dist * dy)
                    if not isValidCoord(checkX, checkY):
                        break
                    if seats[checkX][checkY] == fill:
                        occupied += 1
                        seatFound = True
                    elif seats[checkX][checkY] == empty:
                        seatFound = True
                    dist += 1
    return occupied

with open("input.txt") as input:
    for line in input:
        seats.append([getState(c) for c in line.strip('\n')])

def transition(x, y):
    seat = seats[x][y]
    if seat == floor:
        return floor

    if seat == empty:
        if countVisibleOccupied(x, y) == 0:
            return fill
        else:
            return empty
    
    if seat == fill:
        if countVisibleOccupied(x, y) >= 5:
            return empty
        else:
            return fill

lastState = ""
while lastState != str(seats):
    #printSeats()
    lastState = str(seats)
    originalSeats = [row[:] for row in seats]
    for x in range(len(originalSeats)):
        for y in range(len(originalSeats[x])):
            originalSeats[x][y] = transition(x, y)
    seats = originalSeats
    #print("transition")

filled = 0
for x in range(len(seats)):
    for y in range(len(seats[x])):
        if seats[x][y] == fill:
            filled += 1

print(filled)
    
                    