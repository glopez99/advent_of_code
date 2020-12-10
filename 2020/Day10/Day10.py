import numpy

rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = [ int(line) for line in rawPuzzleInput.readlines() ]

def dayTen (puzzleInput):
  sortedList = sorted(puzzleInput)

  print("The answer to Part One is", partOne(sortedList, len(puzzleInput)))
  print("The answer to Part Two is", partTwo(sortedList))

def partOne (sortedPuzzleInput,length):
  # this number by number and sees if they are 1, 2, or 3 difference. If it is
  # more than 3 it will throw an error.
  currentVoltage = 0
  differenceOf1 = 0
  differenceOf2 = 0
  differenceOf3 = 1

  while (differenceOf1 + differenceOf2 + differenceOf3) <= length:
    difference = sortedPuzzleInput[0] - currentVoltage

    if difference == 1:
      differenceOf1 += 1
    elif difference == 2:
      differenceOf2 += 1
    elif difference == 3:
      differenceOf3 += 1
    elif difference > 3:
      print("There is an error in how the list is being sorted. The number it got stuck on is", sortedList[0])
      break

    currentVoltage = sortedPuzzleInput[0]
    sortedPuzzleInput = sortedPuzzleInput[1:]

  return differenceOf1 *  differenceOf3

def partTwo (sortedPuzzleInput):
  # this adds in 0 and max +3 to account for the charger and the device
  # then going by position by position it finds where the numbers are 3 apart
  # it then splits the range at that point and checks the length to find the permutations possible
  # then you multiple all of those up and get your answer
  sortedPuzzleInput.insert(0, 0)
  sortedPuzzleInput.append(max(sortedPuzzleInput)+3)
  
  start = 0
  previousNumber = 0
  possibleVariations = 1

  for i in range(len(sortedPuzzleInput)):
    if previousNumber + 3 == sortedPuzzleInput[i]:
      paths = findPaths(sortedPuzzleInput[start:i])
      possibleVariations = possibleVariations * paths
      start = i
    
    previousNumber = sortedPuzzleInput[i]

  return possibleVariations

def findPaths(rangeToCheck):
  # finds how many paths are possible based on the length of the range to check
  # I manually counted out each possible number of variations dependent on length
  paths = 0
  
  if len(rangeToCheck) == 0:
    return 0
  if len(rangeToCheck) == 1:
    return 1
  if len(rangeToCheck) == 2:
    return 1
  if len(rangeToCheck) == 3:
    return 2
  if len(rangeToCheck) == 4:
    return 4
  if len(rangeToCheck) == 5:
    return 7

  return paths

dayTen(formattedPuzzleInput)