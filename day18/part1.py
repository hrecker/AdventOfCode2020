operators = ['+', '*']

def evaluate(expression):
    #print("eval: " + expression)
    terms = []
    operations = []
    ignoreUntil = -1
    for index, char in enumerate(expression):
        if ignoreUntil >= 0 and index < ignoreUntil:
            continue
        else:
            ignoreUntil = -1
        if char != ' ':
            if char == '(':
                end = getEndParenthesesIndex(index, expression)
                #print("start: " + str(index) + ", end: " + str(end))
                terms.append(evaluate(expression[index + 1:end]))
                ignoreUntil = end + 1
            else:
                if char in operators:
                    operations.append(char)
                else:
                    terms.append(int(char))
    
    result = terms[0]
    for index, term in enumerate(terms[1:]):
        operation = operations[index]
        if operation == '+':
            result += term
        elif operation == '*':
            result *= term
    #print("result: " + str(result))
    return result

def getEndParenthesesIndex(index, expression):
    endsNeeded = 0
    #print("get " + str(index) + " end: " + expression)
    for idx, char in enumerate(expression[index:]):
        if char == '(':
            endsNeeded += 1
        elif char == ')':
            endsNeeded -= 1
            if endsNeeded == 0:
                #print("end: " + str(index))
                return idx + index
    #print("no end found")
    return -1

with open("input.txt") as input:
    sum = 0
    for line in input:
        #print("line: " + line)
        sum += evaluate(line.strip('\n'))
    print(sum)
