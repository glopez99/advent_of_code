rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = [ int(line) for line in rawPuzzleInput.readlines() ]

def dayFive(puzzleInput):
  exitPoint = len(puzzleInput)
  count = 0
  steps = 0
  instruction = 0

  while count < exitPoint:
    jump = int(puzzleInput[instruction])

    if jump >= 3:
      # this if statement is only  for part 2
      # if doing part one - just do the else statement
      puzzleInput[instruction] = jump - 1
    else:
      puzzleInput[instruction] = jump + 1

    count = count + jump
    instruction = instruction + jump
    steps += 1
  
  return steps

print(dayFive(formattedPuzzleInput))
