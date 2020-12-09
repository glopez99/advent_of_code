rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = [ int(line) for line in rawPuzzleInput.readlines() ]

def dayNinePartOne (startingPoint, puzzleInput):
  if checkValidity(startingPoint, puzzleInput):
    startingPoint += 1
    # print("The new starting point is", startingPoint)
    dayNine(startingPoint, puzzleInput)
  else:
    number = puzzleInput[startingPoint]
    print("the number that returned as false is", number)

def checkValidity(startingPoint, lineToCheck):
  previous25 = lineToCheck[(startingPoint - 25):(startingPoint)]
  #print("The list to check is", previous25)
  numberToCheck = lineToCheck[startingPoint]
  #print("the number to check is", numberToCheck)

  for numberOne in previous25:
    for numberTwo in previous25:
      if numberOne != numberTwo:
        if numberOne + numberTwo == numberToCheck:
          #print("number one is", numberOne)
          #print("number two is", numberTwo)
          return True

  return False

# dayNinePartOne(25, formattedPuzzleInput)

# partTwoPuzzleInput = formattedPuzzleInput[:14]
partTwoPuzzleInput = formattedPuzzleInput[:562]

def dayNinePartTwo (numberToCheck, puzzleInput):
  encryptionWeakness = checkForSum(numberToCheck, puzzleInput)

  if  encryptionWeakness == None or encryptionWeakness == 0:
    if len(puzzleInput) > 1:
      puzzleInput = puzzleInput[1:]
      dayNinePartTwo(numberToCheck, puzzleInput)
    else:
      print("there is an error")
  elif encryptionWeakness != 0 or encryptionWeakness != None:
    print("The encryption weakness is", encryptionWeakness)
    return  encryptionWeakness

def checkForSum (numberToCheck, puzzleInput):
  if sumTheList(puzzleInput) == numberToCheck:
    encrpytionWeakness = findEncryptionWeakness(puzzleInput)
    print('the encryption weakness is', encrpytionWeakness)
    return encrpytionWeakness
  elif sumTheList(puzzleInput) > numberToCheck:
    newPuzzleInput = puzzleInput[:-1]
    # print("the number was too large. the new puzzle input is:", puzzleInput)
    checkForSum(numberToCheck, newPuzzleInput)
  elif sumTheList(puzzleInput) < numberToCheck:
    return None or 0

def sumTheList(puzzleInput):
  summedNumbers = sum(puzzleInput)
  return summedNumbers

def findEncryptionWeakness(input):
  minNumber = min(input)
  maxNumber = max(input)

  encryptionWeakness = minNumber + maxNumber

  return encryptionWeakness

print("The encryption weakness is", dayNinePartTwo(144381670, partTwoPuzzleInput))

# 144381670