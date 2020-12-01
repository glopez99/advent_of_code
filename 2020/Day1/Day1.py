rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = [ int(line) for line in rawPuzzleInput.readlines() ]

def dayOne (puzzleInput) :
  for number in puzzleInput:
    numberToFind = 2020 - number
    if numberToFind in puzzleInput:
      return number * numberToFind

#print(dayOne(formattedPuzzleInput))

def dayOnePartTwo(puzzleInput):
  for numberOne in puzzleInput:
    for numberTwo in puzzleInput:
      for numberThree in puzzleInput:
        if numberOne + numberTwo + numberThree == 2020:
          return numberOne * numberTwo * numberThree

print(dayOnePartTwo(formattedPuzzleInput))