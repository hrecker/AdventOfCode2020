with open('input.txt') as input:
    lines = [int(line.rstrip('\n')) for line in input]

for val1 in lines:
    for val2 in lines[1:]:
        for val3 in lines[2:]:
            if (val1 + val2 + val3 == 2020):
                print("Values found: (" + str(val1) + ", " + str(val2) + ", " + str(val3) + ")")
                result = val1 * val2 * val3
                print("Result: " + str(result))
                exit(0)

print("No valid combination found")