rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = rawPuzzleInput.readlines()

def dayThree (puzzleInput):
  treeTotalCount = 1
  increase = [0, 2, 4, 6, 8]
  slopes = [1, 1, 3, 1, 5, 1, 7, 1, 1, 2]
  
  for i in increase:
    # the slopes to check are listed above. The increase is my hacky way
    # to get the coordinates input correctly. There is assuredly a better
    # solution to this, but hey - it worked.

    treesForSlope = treeCounter(puzzleInput, slopes[i], slopes[i + 1])
    treeTotalCount = treeTotalCount * treesForSlope
  
  
  return treeTotalCount

def treeCounter(puzzleInput, xSlope, ySlope):
  # counts the trees (#) encountered based on the x Slope
  # (dictates how many spots to move right) and y slope 
  # (dictates how many lines to go down). 

  treeCount = 0
  xCoordinate = 0

  for line in puzzleInput[::ySlope]:
    if len(line) == 32:
      # this is again my hacky way to catch the "/n" at
      # the end of the line that was throwing off my length
      # and thus modulo.
      line = line[:-1]

    if line[xCoordinate % len(line)] == ".":
      # this uses the % as it accounts for the repeating nature of the line
      # a "." is an open space and thus no increase in tree count
      xCoordinate += xSlope
    else:
      treeCount += 1
      xCoordinate += xSlope

  return treeCount


print(dayThree(formattedPuzzleInput))