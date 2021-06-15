import re

rawPuzzleInput = open("TestPartTwoInput.txt", "r")
formattedPuzzleInput = rawPuzzleInput.readlines()

def dayFourteenPartTwo(puzzleInput):
  memory = {}
  mask = []
  count = mask.count('X')

  for line in puzzleInput:
    formattedLine = line.replace(" ", '').replace('\n', '')
    splitLine = formattedLine.split("=")
    if splitLine[0] == 'mask':
      mask = list(splitLine[1])
    elif splitLine[0].startswith("mem"):
      number = int(splitLine[1])
      memoryLocation = re.findall(r'\d+', splitLine[0])
      newMemoryLocation = applyMaskToLocation(mask, memoryLocation[0])
      for location in newMemoryLocation:
        memory[location] = number
    else:
      print("There is an error in your day Fourteen logic")

  partTwoAnswer = sum(memory.values())

  return partTwoAnswer

def get_bit(x, n):
  return format(x, 'b').zfill(n)

def applyMaskToLocation(mask, memoryLocation):
  bitLocationList = list((get_bit(int(memoryLocation), 36)))
  maskApplied = []

  for i, number in enumerate(mask):
    if number == 'X':
      maskApplied.append('X')
    elif number == '1':
      maskApplied.append('1')
    elif number == '0':
      maskApplied.append(bitLocationList[i])

  locationsToReturn = applyFloat(maskApplied)

  locationsToReturn = [''.join(location) for location in locationsToReturn]

  return [int(location,2) for location in locationsToReturn]

def applyFloat (location):
  firstLocation = location.copy()
  secondLocation = location.copy()

  xLocation = location.index('X')

  firstLocation[xLocation] = '0'
  secondLocation[xLocation] ='1'
  
  if "X" not in firstLocation:
    return [firstLocation, secondLocation]
  
  locationsFromFirst = applyFloat(firstLocation)
  locationsFromSecond = applyFloat(secondLocation)
  allLocations = locationsFromFirst
  allLocations.extend(locationsFromSecond)
  return allLocations 

def dayFourteenPartOne(puzzleInput):
  memory = {}
  mask = []

  for line in puzzleInput:
    formattedLine = line.replace(" ", '').replace('\n', '')
    splitLine = formattedLine.split("=")
    if splitLine[0] == 'mask':
      mask = list(splitLine[1])
      # print("the mask is", mask)
    elif splitLine[0].startswith("mem"):
      number = applyMaskToNumber(mask, splitLine[1])
      memoryLocation = re.findall(r'\d+', splitLine[0])
      memory[memoryLocation[0]] = number
    else:
      print("There is an error in your day Fourteen logic")
  
  partOneAnswer = sum(memory.values())

  return partOneAnswer

def applyMaskToNumber(mask, number):
  bitNumberList = list((get_bit(int(number), 36)))
  numberToReturn = []

  for i, number in enumerate(mask):
    if number == 'X':
      numberToReturn.append(bitNumberList[i])
    elif number == '1':
      numberToReturn.append('1')
    elif number == '0':
      numberToReturn.append('0')

  numberToReturn = ''.join(numberToReturn)

  return int(numberToReturn,2)
    
if __name__ == "__main__":
    print("The answer to part one is", dayFourteenPartOne(formattedPuzzleInput))
    print("The answer to part two is", dayFourteenPartTwo(formattedPuzzleInput))