adapters = []
joltageDiff = 3

def calculateOneAndThreeDiffs(adapters):
    oneDiffs = 0
    threeDiffs = 0
    for index, adapter in enumerate(adapters[:len(adapters) - 1]):
        diff = adapters[index + 1] - adapter
        if diff == 1:
            oneDiffs += 1
        elif diff == 3:
            threeDiffs += 1
    return (oneDiffs, threeDiffs)

with open("input.txt") as input:
    for line in input:
        adapters.append(int(line))
    
adapters.sort()
adapters.insert(0, 0)
adapters.append(adapters[len(adapters) - 1] + joltageDiff)

diffs = calculateOneAndThreeDiffs(adapters)
print(diffs[0] * diffs[1])