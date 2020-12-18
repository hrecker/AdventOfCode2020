operators = ['+', '*']

def evaluate(expression):
    #print("eval: " + expression)
    terms = []
    operations = []
    ignoreUntil = -1
    currentVal = ""
    # Parse terms, operations, and evaluate expressions in parentheses
    for index, char in enumerate(expression):
        if ignoreUntil >= 0 and index < ignoreUntil:
            continue
        else:
            ignoreUntil = -1
        if char != ' ':
            if char == '(':
                end = getEndParenthesesIndex(index, expression)
                terms.append(evaluate(expression[index + 1:end]))
                ignoreUntil = end + 1
            else:
                if char in operators:
                    operations.append(char)
                else:
                    currentVal += char
        elif currentVal:
            terms.append(int(currentVal))
            currentVal = ""
    if currentVal:
        terms.append(int(currentVal))
    
    if '+' in operations:
        # Calculate all + operations, then evaluate the remaining string
        operationsCopy = list(operations)
        updatedString = ""
        deleted = 0
        for index, op in enumerate(operationsCopy):
            if op == '+':
                terms[index - deleted] = terms[index - deleted] + terms[index - deleted + 1]
                del terms[index - deleted + 1]
                deleted += 1
        for term in terms[:-1]:
            updatedString += str(term) + " * "
        updatedString += str(terms[-1])
        return evaluate(updatedString)
    else:
        # Calculate the * operations that are left over
        result = 1
        for term in terms:
            result *= term
        return result

# Get the end parentheses from a starting index
def getEndParenthesesIndex(index, expression):
    endsNeeded = 0
    for idx, char in enumerate(expression[index:]):
        if char == '(':
            endsNeeded += 1
        elif char == ')':
            endsNeeded -= 1
            if endsNeeded == 0:
                return idx + index
    print("no end found")
    return -1

with open("input.txt") as input:
    sum = 0
    for line in input:
        #print("line: " + line)
        sum += evaluate(line.strip('\n'))
    print(sum)
