currentGroupAnswers = set()
sum = 0

with open('input.txt') as input:
    for line in input:
        if line.strip():
            for char in line.rstrip('\n'):
                currentGroupAnswers.add(char)
        else:
            sum += len(currentGroupAnswers)
            currentGroupAnswers = set()

sum += len(currentGroupAnswers)

print(sum)