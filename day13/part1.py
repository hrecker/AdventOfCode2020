initial = 0
buses = []

with open("input.txt") as input:
    initial = int(input.readline())
    for bus in input.readline().strip('\n').split(','):
        if bus != 'x':
            buses.append(int(bus))

check = initial
while True:
    for bus in buses:
        if check % bus == 0:
            print(bus * (check - initial))
            exit(0)

    check += 1
        
print("none found")