from collections import deque

decks = {}
decks[1] = deque()
decks[2] = deque()
currentPlayer = -1

with open("input.txt") as input:
    for line in input:
        stripped = line.strip('\n')
        if "Player" in stripped:
            currentPlayer = int(stripped[-2])
        elif stripped:
            decks[currentPlayer].append(int(stripped))

while len(decks[1]) > 0 and len(decks[2]) > 0:
    card1 = decks[1].popleft()
    card2 = decks[2].popleft()
    if card1 > card2:
        decks[1].append(card1)
        decks[1].append(card2)
    else:
        decks[2].append(card2)
        decks[2].append(card1)

winner = decks[1]
if len(decks[2]) > 0:
    winner = decks[2]
    
print("player1: " + str(decks[1]))
print("player2: " + str(decks[2]))

score = 0
iter = 1
while len(winner) > 0:
    card = winner.pop()
    score += card * iter
    iter += 1

print(score)