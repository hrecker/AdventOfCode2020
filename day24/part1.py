blackTiles = {}

e = 0
se = 1
sw = 2
w = 3
nw = 4
ne = 5
n = 6
s = 7


with open("C:/users/henry/adventofcode2020/day24/input.txt") as input:
    for line in input:
        line = line.strip('\n')
        normalizedCoord = ""
        dirCounts = [0] * 8
        dirs = {}
        dirs[e] = 0
        dirs[w] = 0
        dirs[n] = 0
        dirs[s] = 0
        i = 0
        while i < len(line):
            if line[i] in ['e', 'w']:
                if line[i] == 'e':
                    dirs[e] += 1
                elif line[i] == 'w':
                    dirs[w] += 1
                else:
                    print("invalid single char direction: " + line[i])
                    exit(1)
                i += 1
            else:
                if line[i:i+2] == 'se':
                    dirs[s] += 1
                    dirs[e] += 0.5
                elif line[i:i+2] == 'sw':
                    dirs[s] += 1
                    dirs[w] += 0.5
                elif line[i:i+2] == 'nw':
                    dirs[n] += 1
                    dirs[w] += 0.5
                elif line[i:i+2] == 'ne':
                    dirs[n] += 1
                    dirs[e] += 0.5
                else:
                    print("invalid two char direction: " + line[i:i+2])
                    exit(1)
                i += 2
        
        if dirs[e] > dirs[w]:
            dirCounts[e] = dirs[e] - dirs[w]
            dirCounts[w] = 0
        else:
            dirCounts[w] = dirs[w] - dirs[e]
            dirCounts[e] = 0
        
        if dirs[n] > dirs[s]:
            dirCounts[n] = dirs[n] - dirs[s]
            dirCounts[s] = 0
        else:
            dirCounts[s] = dirs[s] - dirs[n]
            dirCounts[n] = 0

        for i in range(int(dirCounts[e] * 2)):
            normalizedCoord += 'e'
        for i in range(int(dirCounts[s] * 2)):
            normalizedCoord += 's'
        for i in range(int(dirCounts[w] * 2)):
            normalizedCoord += 'w'
        for i in range(int(dirCounts[n] * 2)):
            normalizedCoord += 'n'
        
        #print("normalized: " + normalizedCoord)
        if normalizedCoord in blackTiles:
            del blackTiles[normalizedCoord]
        else:
            blackTiles[normalizedCoord] = True

print(str(len(blackTiles)))
