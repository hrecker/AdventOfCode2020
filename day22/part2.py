from collections import deque

decks = {}
decks[1] = deque()
decks[2] = deque()
currentPlayer = -1

with open("C:/users/henry/adventofcode2020/day22/input.txt") as input:
    for line in input:
        stripped = line.strip('\n')
        if "Player" in stripped:
            currentPlayer = int(stripped[-2])
        elif stripped:
            decks[currentPlayer].append(int(stripped))

def getRoundStateStr(deck1, deck2):
    return str(deck1) + str(deck2)

def playCombatGame(deck1, deck2):
    allPlayedRounds = {}
    while len(deck1) > 0 and len(deck2) > 0:
        stateStr = getRoundStateStr(deck1, deck2)
        if stateStr in allPlayedRounds:
            deck2.clear()
            return
        allPlayedRounds[stateStr] = 1
        win, card1, card2 = playCombatRound(deck1, deck2)

        if win == 1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

def playCombatRound(deck1, deck2):
    card1 = deck1.popleft()
    card2 = deck2.popleft()
    if len(deck1) >= card1 and len(deck2) >= card2:
        # Create subdecks
        subDeck1 = deque()
        subDeck2 = deque()
        copy1 = deck1.copy()
        copy2 = deck2.copy()
        for i in range(card1):
            subDeck1.append(copy1.popleft())
        for i in range(card2):
            subDeck2.append(copy2.popleft())

        # If player 1 has the highest card and it is bigger than both decks combined, they will always win
        maxSubDeck1 = max(subDeck1)
        maxSubDeck2 = max(subDeck2)
        winner = -1
        if maxSubDeck1 > maxSubDeck2 and maxSubDeck1 > (len(subDeck1) + len(subDeck2)):
            winner = 1

        if winner == -1:
            playCombatGame(subDeck1, subDeck2)
            winner = determineWinner(subDeck1, subDeck2)
        return (winner, card1, card2)
    elif card1 > card2:
        return (1, card1, card2)
    elif card2 > card1:
        return (2, card1, card2)
    else:
        print("Something very bad has happened")

def determineWinner(deck1, deck2):
    if len(deck1) > 0:
        return 1
    return 2

playCombatGame(decks[1], decks[2])
winnerIndex = determineWinner(decks[1], decks[2])
winner = decks[winnerIndex]

print("player1: " + str(decks[1]))
print("player2: " + str(decks[2]))

score = 0
iter = 1
while len(winner) > 0:
    card = winner.pop()
    score += card * iter
    iter += 1

print("winner: " + str(winnerIndex))
print(score)