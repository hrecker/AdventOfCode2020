lines = []
acc = 0
executed = set()

with open('input.txt') as input:
    for line in input:
        lines.append(line)
    currentLine = 0
    while True:
        executed.add(currentLine)
        nextLine = currentLine + 1
        line = lines[currentLine]
        pieces = line.split(' ')
        op = pieces[0]
        val = pieces[1]
        if val[1] == '+':
            val = val[1:]
        val = int(val)

        if op == "jmp":
            nextLine = currentLine + val
        elif op == "acc":
            acc += val

        if nextLine in executed:
            break

        currentLine = nextLine



print(acc)
