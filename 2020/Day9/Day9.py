rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = [ int(line) for line in rawPuzzleInput.readlines() ]

def dayNinePartOne (startingPoint, puzzleInput):
  # this checks the validity if two numbers in the previous 25 equal
  # the number in the starting Point location. If it returns true,
  # it will move one number down the list and keep checking. If it returns
  # false, it will print that number.
  if checkValidity(startingPoint, puzzleInput):
    startingPoint += 1

    dayNinePartOne(startingPoint, puzzleInput)
  else:
    number = puzzleInput[startingPoint]
    print("the number that returned as false is", number)

def checkValidity(startingPoint, lineToCheck):
  previous25 = lineToCheck[(startingPoint - 25):(startingPoint)]
  numberToCheck = lineToCheck[startingPoint]

  for numberOne in previous25:
    for numberTwo in previous25:
      if numberOne != numberTwo:
        if numberOne + numberTwo == numberToCheck:
          return True

  return False

dayNinePartOne(25, formattedPuzzleInput)

partTwoPuzzleInput = formattedPuzzleInput[:562]
# found the location of my number -  you don't have to check past this number as 
# everything past this number will be larger

def dayNinePartTwo (numberToCheck, puzzleInput):
  # loops through the puzzle input walking from the front of the list
  # to the back of the list until it finds the solution
  encryptionWeakness = checkForSum(numberToCheck, puzzleInput)

  if  encryptionWeakness == None or encryptionWeakness == 0:
    if len(puzzleInput) > 1:
      puzzleInput = puzzleInput[1:]
      dayNinePartTwo(numberToCheck, puzzleInput)
    else:
      print("there is an error")
  elif encryptionWeakness != 0 or encryptionWeakness != None:
    print("The encryption weakness is", encryptionWeakness)


def checkForSum (numberToCheck, puzzleInput):
  # loops through the puzzle inputs to see if the current input
  # has the list that equals the number. If it's too large, it
  # slices a number off the end, if it's too small, it returns 0,
  # if it does equal the number - it returns the encryption weakness (aka solution)
  if sum(puzzleInput) == numberToCheck:
    return min(puzzleInput) + max(puzzleInput)
  elif sum(puzzleInput) > numberToCheck:
    newPuzzleInput = puzzleInput[:-1]
    # print("the number was too large. the new puzzle input is:", puzzleInput)
    return checkForSum(numberToCheck, newPuzzleInput)
  elif sum(puzzleInput) < numberToCheck:
    return 0

dayNinePartTwo(144381670, partTwoPuzzleInput)