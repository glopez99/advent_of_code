playerOneDeck = []
playerTwoDeck = []

with open("PuzzleInput.txt", "r") as f:
  for i, line in enumerate(f):
    if 0 < i <= 25:
      playerOneDeck.append(int(line.strip('\n')))
    elif 27 < i <= 52:
      playerTwoDeck.append(int(line.strip('\n')))
    else:
      continue

def dayTwentyTwo(playerOne, playerTwo):
  winner = playCombat(playerOne, playerTwo)

  print("The winning score is", calculateScore(winner))

def playCombat(playerOne, playerTwo):
  p1Deck = playerOne.copy()
  p2Deck = playerTwo.copy()

  while len(p1Deck) != 0 and len(p2Deck) != 0:
    cardOne = p1Deck.pop(0)
    cardTwo = p2Deck.pop(0)

    if cardOne > cardTwo:
      winningHand = [cardOne, cardTwo]
      p1Deck.extend(winningHand)
    else:
      winningHand = [cardTwo, cardOne]
      p2Deck.extend(winningHand)

  if len(p1Deck) != 0:
    return p1Deck
  else:
    return p2Deck

def calculateScore(winner):
  score = 0

  for i, value in enumerate(winner):
    score = score + value * (len(winner) - i)
  
  return score

if __name__ == "__main__":
  dayTwentyTwo(playerOneDeck, playerTwoDeck )