lines = []
acc = 0
executed = set()

def isInfinite(lines):
    global acc
    acc = 0
    executed = set()
    currentLine = 0
    while currentLine < len(lines):
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
            return True

        currentLine = nextLine
    return False

with open('input.txt') as input:
    for line in input:
        lines.append(line)
    currentLine = 0
    originalLine = ""
    while True:
        line = lines[currentLine]
        originalLine = line
        pieces = line.split(' ')
        op = pieces[0]

        if op == "jmp":
            lines[currentLine] = lines[currentLine].replace("jmp", "nop")
        elif op == "nop":
            lines[currentLine] = lines[currentLine].replace("nop", "jmp")
        
        if not isInfinite(lines):
            break
        else:
            lines[currentLine] = originalLine
            
        currentLine += 1

print(acc)
