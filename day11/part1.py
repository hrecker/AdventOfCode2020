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

def transition(x, y):
    seat = seats[x][y]
    if seat == floor:
        return floor

    if seat == empty:
        shouldOccupy = True
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                checkX = x + dx
                checkY = y + dy
                if (dx != 0 or dy != 0) and checkX >= 0 and checkY >= 0 \
                    and checkX < len(seats) and checkY < len(seats[0]) and seats[checkX][checkY] == fill:
                    shouldOccupy = False
        if shouldOccupy:
            return fill
        else:
            return empty
    
    if seat == fill:
        occupied = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                checkX = x + dx
                checkY = y + dy
                if (dx != 0 or dy != 0) and checkX >= 0 and checkY >= 0 \
                    and checkX < len(seats) and checkY < len(seats[0]) and seats[checkX][checkY] == fill:
                    occupied += 1
        if occupied >= 4:
            return empty
        else:
            return fill

with open("input.txt") as input:
    for line in input:
        seats.append([getState(c) for c in line.strip('\n')])

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
    
                    