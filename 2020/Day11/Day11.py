# finding where people are going to sit. It's a cellular automata problem.
# The code below is very long, repetitive, and probably could be done better,
# but it's AoC and I'm new to coding, so I got the right answer and went and
# celebrated and rested for Day 12.

src_code = []
with open("TestInput.txt", "r") as f:
    for line in f:
        src_code.append(list(line.strip("\n")))

def dayEleven(puzzleInput):
  currentSeating = puzzleInput.copy()
  previousSeating = []

  while previousSeating != currentSeating:
    previousSeating = currentSeating.copy()
    print("previous seating", previousSeating)

    currentSeating = findCurrentSeating(currentSeating)
    print("current seating", currentSeating)
  
  print("The number of occupied seats is", countOccupiedSeats(currentSeating))

def findCurrentSeating(currentSeating):
  newSeating = []

  for i in range(len(currentSeating)):
    newRow = []
    for j in range(len(currentSeating[i])):
      if currentSeating[i][j] == "L" and switchSeat(i, j, currentSeating) == 0:
        newRow.append("#")
      elif currentSeating[i][j] == "#" and switchSeat(i, j, currentSeating) >= 5:
        newRow.append("L")
      else:
        newRow.append(currentSeating[i][j])
    newSeating.append(newRow)
      
  return newSeating

def switchSeat(i, j, currentSeating):
  count = 0

  if i == 0:
    count = count + checkTopRow(i, j, currentSeating)
  elif i == len(currentSeating) - 1:
    count = count + checkBottomRow(i, j, currentSeating)
  elif j == 0:
    count = count + checkLeftEdge(i, j, currentSeating)
  elif j == len(currentSeating[i]) - 1:
      count = count + checkRightEdge(i, j, currentSeating)
  else:
    if findFirstLUDiagonal(i-1, j-1, currentSeating) == "#":
      count += 1
    if findFirstUpSeat(i-1, j, currentSeating) == "#":
      count += 1
    if findFirstRUDiagonal(i-1, j+1, currentSeating) == "#":
      count += 1
    if findFirstLeftSeat(i, j-1, currentSeating) == "#":
      count += 1
    if findFirstRightSeat(i, j+1, currentSeating) == "#":
      count += 1
    if findFirstLDDiagonal(i+1, j-1, currentSeating) == "#":
      count += 1
    if findFirstDownSeat(i+1, j, currentSeating) == "#":
      count += 1
    if findFirstRDDiagonal(i+1, j+1, currentSeating) == "#":
      count += 1

  return count

def checkTopRow(i, j, currentSeating):
  count = 0

  if j == 0:
    if findFirstRightSeat(i, j+1, currentSeating) == "#":
      count += 1
    if findFirstDownSeat(i+1, j, currentSeating) == "#":
      count += 1
    if findFirstRDDiagonal(i+1, j+1, currentSeating) == "#":
      count += 1
  elif j == len(currentSeating[i]) - 1:
    if findFirstLeftSeat(i, j-1, currentSeating) == "#":
      count += 1
    if findFirstLDDiagonal(i+1, j-1, currentSeating) == "#":
      count += 1
    if findFirstDownSeat(i+1, j, currentSeating) == "#":
      count += 1
  else:
    if findFirstLeftSeat(i, j-1, currentSeating) == "#":
      count += 1
    if findFirstRightSeat(i, j+1, currentSeating) == "#":
      count += 1
    if findFirstLDDiagonal(i+1, j-1, currentSeating) == "#":
      count += 1
    if findFirstDownSeat(i+1, j, currentSeating) == "#":
      count += 1
    if findFirstRDDiagonal(i+1, j+1, currentSeating) == "#":
      count += 1

  return count

def checkBottomRow(i, j, currentSeating):
  count = 0

  if j == 0:
    if findFirstUpSeat(i-1, j, currentSeating) == "#":
      count += 1
    if findFirstRUDiagonal(i-1, j+1, currentSeating) == "#":
      count += 1
    if findFirstRightSeat(i, j+1, currentSeating) == "#":
      count += 1
  elif j == len(currentSeating[i]) - 1:
    if findFirstLUDiagonal(i-1, j-1, currentSeating) == "#":
      count += 1
    if findFirstUpSeat(i-1, j, currentSeating) == "#":
      count += 1
    if findFirstLeftSeat(i, j-1, currentSeating) == "#":
      count += 1
  else:
    if findFirstLUDiagonal(i-1, j-1, currentSeating) == "#":
      count += 1
    if findFirstUpSeat(i-1, j, currentSeating) == "#":
      count += 1
    if findFirstRUDiagonal(i-1, j+1, currentSeating) == "#":
      count += 1
    if findFirstLeftSeat(i, j-1, currentSeating) == "#":
      count += 1
    if findFirstRightSeat(i, j+1, currentSeating) == "#":
      count += 1

  return count

def checkLeftEdge(i, j, currentSeating):
  count = 0

  if findFirstUpSeat(i-1, j, currentSeating) == "#":
    count += 1
  if findFirstRUDiagonal(i-1, j+1, currentSeating) == "#":
    count += 1
  if findFirstRightSeat(i, j+1, currentSeating) == "#":
    count += 1
  if findFirstDownSeat(i+1, j, currentSeating) == "#":
    count += 1
  if findFirstRDDiagonal(i+1, j+1, currentSeating) == "#":
    count += 1

  return count

def checkRightEdge(i, j, currentSeating):
  count = 0

  if findFirstLUDiagonal(i-1, j-1, currentSeating) == "#":
    count += 1
  if findFirstUpSeat(i-1, j, currentSeating) == "#":
    count += 1
  if findFirstLeftSeat(i, j-1, currentSeating) == "#":
    count += 1
  if findFirstLDDiagonal(i+1, j-1, currentSeating) == "#":
    count += 1
  if findFirstDownSeat(i+1, j, currentSeating) == "#":
    count += 1

  return count

def countOccupiedSeats(currentSeating):
  occupiedSeats = 0

  for row in  currentSeating:
    for seat in row:
      if seat == "#":
        occupiedSeats += 1
  
  return occupiedSeats

def findFirstUpSeat(i, j, currentSeating):
  if currentSeating[i][j] == ".":
    i = i - 1
    if i >= 0:
      return findFirstUpSeat(i, j, currentSeating)
    else:
      return "L"
  else:
    return currentSeating[i][j]

def findFirstDownSeat(i, j, currentSeating):
  if currentSeating[i][j] == ".":
    i = i + 1
    if i < len(currentSeating):
      return findFirstDownSeat(i, j, currentSeating)
    else:
      return "L"
  else:
    return currentSeating[i][j]

def findFirstLeftSeat(i, j, currentSeating):
  if currentSeating[i][j] == ".":
    j = j - 1
    if j >= 0:
      return findFirstLeftSeat(i, j, currentSeating)
    else:
      return "L"
  else:
    return currentSeating[i][j]

def findFirstRightSeat(i, j, currentSeating):
  if currentSeating[i][j] == ".":
    j = j + 1
    if j < len(currentSeating[i]):
      return findFirstRightSeat(i, j, currentSeating)
    else:
      return "L"
  else:
    return currentSeating[i][j]

def findFirstRUDiagonal(i, j, currentSeating):
  if currentSeating[i][j] == ".":
    i = i - 1
    j = j + 1
    if i >= 0 and j < len(currentSeating[i]):
      return findFirstRUDiagonal(i, j, currentSeating)
    else:
      return "L"
  else:
    return currentSeating[i][j]

def findFirstLUDiagonal(i, j, currentSeating):
  if currentSeating[i][j] == ".":
    i = i - 1
    j = j - 1
    if i >= 0 and j >= 0:
      return findFirstLUDiagonal(i, j, currentSeating)
    else:
      return "L"
  else:
    return currentSeating[i][j]

def findFirstRDDiagonal(i, j, currentSeating):
  if currentSeating[i][j] == ".":
    i = i + 1
    j = j + 1
    if i < len(currentSeating) and j < len(currentSeating[i]):
      return findFirstRDDiagonal(i, j, currentSeating)
    else:
      return "L"
  else:
    return currentSeating[i][j]

def findFirstLDDiagonal(i, j, currentSeating):
  if currentSeating[i][j] == ".":
    i = i + 1
    j = j - 1
    if i < len(currentSeating) and j >= 0:
      return findFirstLDDiagonal(i, j, currentSeating)
    else:
      return "L"
  else:
    return currentSeating[i][j]

dayEleven(src_code)