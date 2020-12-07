count = 0
canContain = set()
lastCount = 0
lines = []

with open('input.txt') as input:
    for line in input:
        lines.append(line)
    while True:
        lastCount = len(canContain)
        for line in lines:
            pieces = line.split("contain")
            contents = pieces[1]
            bagName = pieces[0].split(" bags")[0]
            if "shiny gold" in contents:
                canContain.add(bagName)
            for container in canContain.copy():
                if container in contents:
                    canContain.add(bagName)

        if lastCount == len(canContain):
            break

print(len(canContain))