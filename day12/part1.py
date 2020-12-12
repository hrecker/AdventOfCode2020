currentDegrees = 0
eastPos = 0
northPos = 0

def rotate(dir, degrees):
    global currentDegrees
    if dir == 'L':
        degrees = 360 - degrees
    currentDegrees += degrees
    currentDegrees = currentDegrees % 360

def move(dir, dist):
    global eastPos, northPos
    if dir == 'L' or dir == 'R':
        #print("rotating " + dir + str(dist))
        rotate(dir, dist)
        #print("new degrees: " + str(currentDegrees))
        return

    if dir == 'F':
        if currentDegrees == 90:
            dir = 'S'
        elif currentDegrees == 180:
            # This dumb W right here
            dir = 'W'
        elif currentDegrees == 270:
            dir = 'N'
        else:
            dir = 'E'

    if dir == 'N':
        #print("north " + str(dist))
        northPos += dist
    elif dir == 'S':
        #print("south " + str(dist))
        northPos -= dist
    elif dir == 'E':
        #print("east " + str(dist))
        eastPos += dist
    elif dir == 'W':
        #print("west " + str(dist))
        eastPos -= dist
    #print("(" + str(eastPos) + ", " + str(northPos) + ", " + str(currentDegrees) + ")")

with open("input.txt") as input:
    for line in input:
       move(line[0], int(line[1:]))

print(abs(eastPos) + abs(northPos))
