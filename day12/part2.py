eastPos = 0
northPos = 0
waypoint = [10, 1]

def rotate(dir, degrees):
    global waypoint
    if dir == 'L':
        degrees = 360 - degrees
    
    if degrees == 90:
        waypoint = [waypoint[1], -waypoint[0]]
    elif degrees == 180:
        waypoint = [-waypoint[0], -waypoint[1]]
    elif degrees == 270:
        waypoint = [-waypoint[1], waypoint[0]]

def move(dir, dist):
    global eastPos, northPos, waypoint
    if dir == 'L' or dir == 'R':
        rotate(dir, dist)
        return

    if dir == 'F':
        eastPos += waypoint[0] * dist
        northPos += waypoint[1] * dist

    elif dir == 'N':
        #print("north " + str(dist))
        waypoint[1] += dist
    elif dir == 'S':
        #print("south " + str(dist))
        waypoint[1] -= dist
    elif dir == 'E':
        #print("east " + str(dist))
        waypoint[0] += dist
    elif dir == 'W':
        #print("west " + str(dist))
        waypoint[0] -= dist
    #print("(" + str(eastPos) + ", " + str(northPos) + ", " + str(currentDegrees) + ")")

with open("input.txt") as input:
    for line in input:
       move(line[0], int(line[1:]))

print(abs(eastPos) + abs(northPos))
