import math

rawPuzzleInput =  open('PuzzleInput.txt', 'r')
formattedPuzzleInput = rawPuzzleInput.readlines()

def dayFive(puzzleInput):
  maxSeatID = 0
  seatIDS = []

  for line in puzzleInput:
    seatID = getRow(line) * 8 + getColumn(line)

    if seatID > maxSeatID:
      maxSeatID = seatID

    seatIDS.append(seatID)

  mySeatID = findSeatID(seatIDS)

  return maxSeatID, mySeatID

def getRow(line):
  minRow = 0
  maxRow = 127

  parsedLine = list(line)

  for letter in parsedLine:
    if letter == "F":
      maxRow = maxRow  - math.ceil((maxRow - minRow) / 2)

    if letter == "B":
      minRow = minRow + math.ceil((maxRow - minRow) / 2)

  if parsedLine[6] == "F":
    return minRow
  else:
    return maxRow

def getColumn(line):
  minColumn = 0
  maxColumn = 7

  parsedLine = list(line)

  for letter in parsedLine:
    if letter == "L":
      maxColumn = maxColumn  - math.ceil((maxColumn - minColumn) / 2)

    if letter == "R":
      minColumn = minColumn + math.ceil((maxColumn - minColumn) / 2)

  if parsedLine[9] == "L":
    return minColumn
  else:
    return maxColumn

def findSeatID(array):
  takenSeats = sorted(array)

  mySeatID = 48

  for seatID in takenSeats:
    if seatID == mySeatID:
      mySeatID += 1
    elif seatID - 1 == mySeatID:
      return mySeatID


print(dayFive(formattedPuzzleInput))