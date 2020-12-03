count = 0
with open('input.txt') as input:
    for line in input:
        pieces = line.rstrip('\n').split(' ')
        min = int(pieces[0].split('-')[0])
        max = int(pieces[0].split('-')[1])
        charCount = pieces[2].count(pieces[1][0])
        if charCount >= min and charCount <= max:
            count += 1
        
print(count)