count = 0
with open('input.txt') as input:
    for line in input:
        pieces = line.rstrip('\n').split(' ')
        i1 = int(pieces[0].split('-')[0]) - 1
        i2 = int(pieces[0].split('-')[1]) - 1
        password = pieces[2]
        char = pieces[1][0]
        if (password[i1] == char) != (password[i2] == char):
            count += 1
        
print(count)
