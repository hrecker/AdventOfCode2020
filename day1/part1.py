with open('input.txt') as input:
    lines = [int(line.rstrip('\n')) for line in input]

for val1 in lines:
    for val2 in lines[1:]:
        if (val1 + val2 == 2020):
            print("Values found: (" + str(val1) + ", " + str(val2) + ")")
            result = val1 * val2
            print("Result: " + str(result))
            exit(0)

print("No valid combination found")