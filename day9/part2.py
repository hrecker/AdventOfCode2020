preambleSize = 25
buffer = []
lines = []
targetSum = -1

def findValues(sum, buffer):
    for val1 in buffer:
        for val2 in buffer:
            if val1 != val2 and (val1 + val2) == sum:
                return True
    return False

with open('input.txt') as input:
    for line in input:
        lines.append(int(line))
    for line in lines:
        if len(buffer) < preambleSize:
            buffer.append(line)
        else:
            if not findValues(line, buffer):
                targetSum = line
                break
            else:
                buffer.append(line)
                buffer = buffer[1:]
    
    if targetSum == -1:
        print("none found")
        exit(1)
    
    for i1, line in enumerate(lines):
        for i2 in range(i1 + 1, len(lines)):
            if (sum(lines[i1:i2]) == targetSum):
                weakness = min(lines[i1:i2]) + max(lines[i1:i2])
                print(weakness)
                exit(0)

print("none found")
