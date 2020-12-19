import re

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

def buildRegexGroup(options):
    group = "("
    for option in options[:-1]:
        group += option + '|'
    group += options[-1] + ')'
    return group

with open("input.txt") as input:
    # Store rule lines
    for line in input:
        stripped = line.strip('\n')
        if not stripped:
            break
        pieces = stripped.split(':')
        ruleLines[pieces[0]] = pieces[1]
    ruleLines["8"] = " 42 | 42 8"
    ruleLines["11"] = " 42 31 | 42 11 31"
    re42 = buildRegexGroup(expandRule(ruleLines["42"]))
    re31 = buildRegexGroup(expandRule(ruleLines["31"]))
    # Start with 2 or more 42's
    # Then end with 1 or more 31's
    regex = '^' + re42 + re42 + '+'
    regex += re31 + "+$"
    pattern = re.compile(regex)
    pattern42 = re.compile('^' + re42 + '$')
    pattern31 = re.compile('^' + re31 + '$')
    # Look for matches
    count = 0
    chunkLength = 8
    for line in input:
        stripped = line.strip('\n')
        match = pattern.match(stripped)
        if match:
            # Even when there is a match for the regex, there needs to be
            # more 42's than 31's, due to how rule 11 is structured.
            # I don't know how to do that in regex so I did it manually
            # here instead.
            index = 0
            section42 = True
            count42 = 0
            count31 = 0
            while index + chunkLength <= len(stripped):
                chunk = stripped[index:index + chunkLength]
                if section42:
                    if pattern42.match(chunk):
                        count42 += 1
                    elif pattern31.match(chunk):
                        section42 = False
                        count31 += 1
                elif pattern31.match(chunk):
                    count31 += 1
                index += chunkLength
            if count42 <= count31:
                print("This one doesn't count")
                count -= 1

            count += 1
    print(count)
