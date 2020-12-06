currentGroupAnswers = set()
newGroup = True
sum = 0

with open('input.txt') as input:
    for line in input:
        if line.strip():
            if newGroup:
                for char in line.rstrip('\n'):
                    currentGroupAnswers.add(char)
                newGroup = False
            else:
                currentAnswer = set()
                for char in line.rstrip('\n'):
                    currentAnswer.add(char)
                currentGroupAnswers = currentGroupAnswers.intersection(currentAnswer)
        else:
            sum += len(currentGroupAnswers)
            currentGroupAnswers = set()
            newGroup = True

sum += len(currentGroupAnswers)

print(sum)