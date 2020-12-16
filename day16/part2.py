cats = []
stage = "cats"
rules = []
ruleNames = []
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
                namePieces = inputLine.split(": ")
                pieces = namePieces[1].split(" or ")
                rule1 = pieces[0].split("-")
                rule2 = pieces[1].split("-")
                ruleFull = {}
                ruleFull["name"] = namePieces[0]
                ruleFull["bounds1"] = (int(rule1[0]), int(rule1[1]))
                ruleFull["bounds2"] = (int(rule2[0]), int(rule2[1]))
                rules.append(ruleFull)
        elif stage == "yourTicket" and inputLine:
            if "ticket" not in inputLine:
                tickets.append([int(v) for v in inputLine.split(",")])
                anyInvalid = False
                for val in inputLine.split(","):
                    anyValid = False
                    for rule in rules:
                        if int(val) >= rule["bounds1"][0] and int(val) <= rule["bounds1"][1]:
                            anyValid = True
                            break
                        if int(val) >= rule["bounds2"][0] and int(val) <= rule["bounds2"][1]:
                            anyValid = True
                            break
                    if not anyValid:
                        anyInvalid = True
                        errorRate += int(val)
                if anyInvalid:
                    tickets.remove(tickets[-1])

#print(str(tickets))
#print(str(rules))

ordering = {}
possibleCols = {}
currentRule = 0
#while len(ordering) < :
while currentRule < len(rules):
    rule = rules[currentRule]
    currentCol = 0
    validCols = []
    #print("checking rule: " + str(rule))
    while currentCol < len(rules):
        anyInvalid = False
        #print("checking col: " + str(currentCol))
        for ticket in tickets:
            #print("checking ticket: " + str(ticket))
            if (ticket[currentCol] < rule["bounds1"][0] or ticket[currentCol] > rule["bounds1"][1]) and (ticket[currentCol] < rule["bounds2"][0] or ticket[currentCol] > rule["bounds2"][1]):
                anyInvalid = True
                break
        if not anyInvalid:
            #print("column found: " + str(currentCol))
            validCols.append(currentCol)
        currentCol += 1
    possibleCols[currentRule] = validCols
    currentRule += 1
    #if currentRule >= len(rules):
    #    currentRule = 0

print()
print("possible: " + str(possibleCols))

while len(ordering) < len(rules):
    for rule in possibleCols.keys():
        if len(possibleCols[rule]) == 1:
            col = possibleCols[rule][0]
            ordering[rule] = col
            for possible in possibleCols.values():
                if col in possible:
                    possible.remove(col)

print("final ordering: " + str(ordering))

result = 1
for index, rule in enumerate(rules):
    if "departure" in rule["name"]:
        result *= tickets[0][ordering[index]]


print(result)

