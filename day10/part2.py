adapters = []
joltageDiff = 3

def countArrangements(adapters, index):
    arrangements = 0
    currentAdapter = adapters[index]
    while index < len(adapters) - 1:
        index += 1
        if adapters[index] - currentAdapter <= joltageDiff:
            arrangements += countArrangements(adapters, index)
        else:
            break
    if arrangements == 0:
        arrangements = 1
    return arrangements

def isRemovable(adapters, index):
    return index > 0 and index < len(adapters) - 1 and \
        adapters[index + 1] - adapters[index - 1] <= joltageDiff

with open("input.txt") as input:
    for line in input:
        adapters.append(int(line))
    
adapters.sort()
adapters.insert(0, 0)
adapters.append(adapters[len(adapters) - 1] + joltageDiff)

nonRemovableIndices = [i for i, a in enumerate(adapters) if not isRemovable(adapters, i)]

arrangements = 1
for i, nonRemovable in enumerate(nonRemovableIndices[:len(nonRemovableIndices) - 1]):
    start = nonRemovable
    end = nonRemovableIndices[i + 1] + 1
    if end - start > 2:
        arrangements *= countArrangements(adapters[start:end], 0)

print(str(arrangements))