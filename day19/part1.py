cachedRules = {}
ruleLines = {}

def expandRule(rule):
    rule = rule.strip()
    if rule in cachedRules:
        return cachedRules[rule]

    expansion = []
    if '"' in rule:
        expansion.append(rule.split('"')[1])
    elif '|' in rule:
        pieces = rule.split('|')
        for piece in pieces:
            expansion += expandRule(piece)
    elif ' ' not in rule:
        expansion = expandRule(ruleLines[rule])
    else:
        subRules = rule.strip().split(' ')
        for exp1 in expandRule(ruleLines[subRules[0]]):
            for exp2 in expandRule(ruleLines[subRules[1]]):
                expansion.append(exp1 + exp2)
        
    cachedRules[rule] = expansion
    return expansion

with open("input.txt") as input:
    # Store rule lines
    for line in input:
        stripped = line.strip('\n')
        if not stripped:
            break
        pieces = stripped.split(':')
        ruleLines[pieces[0]] = pieces[1]
    # Get all possible messages
    allPossibleMessages = expandRule(ruleLines["0"])
    # Check if messages match
    count = 0
    for line in input:
        stripped = line.strip('\n')
        if stripped in allPossibleMessages:
            count += 1
    print(count)
