preambleSize = 25
buffer = []

def findValues(sum, buffer):
    for val1 in buffer:
        for val2 in buffer:
            if val1 != val2 and (val1 + val2) == sum:
                return True
    return False

with open('input.txt') as input:
    for line in input:
        if len(buffer) < preambleSize:
            buffer.append(int(line))
        else:
            if not findValues(int(line), buffer):
                print(int(line))
                exit(0)
            else:
                buffer.append(int(line))
                buffer = buffer[1:]

print("none found")
