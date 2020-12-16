cats = []
stage = "cats"
rules = []
errorRate = 0
invalid = {}
tickets = []

with open("input.txt") as input:
    for line in input:
        inputLine = line.strip('\n')
        if stage == "cats":
            if not inputLine:
                stage = "yourTicket"
            else:
                pieces = inputLine.split(": ")[1].split(" or ")
                rule1 = pieces[0].split("-")
                rule2 = pieces[1].split("-")
                rules.append((int(rule1[0]), int(rule1[1])))
                rules.append((int(rule2[0]), int(rule2[1])))
        elif stage == "yourTicket" and inputLine:
            if "ticket" not in inputLine:
                tickets.append(inputLine)
                anyInvalid = False
                for val in inputLine.split(","):
                    anyValid = False
                    for rule in rules:
                        if int(val) >= rule[0] and int(val) <= rule[1]:
                            anyValid = True
                            break
                    if not anyValid:
                        anyInvalid = True
                        errorRate += int(val)
                if anyInvalid:
                    tickets.remove(inputLine)

print(str(tickets))


print(errorRate)

