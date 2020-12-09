import linecache

# helping a kid turn on his game console (infinity loop)
# for part 2 - manually backtraced and changed until it didn't loop

rawPuzzleInput = "PuzzleInput.txt"

def dayEight(number, puzzleInput, accumulator, linesSeen):
  accumulator = accumulator
  linesSeen = linesSeen

  line = linecache.getline(puzzleInput, number)
  # print("the line is:", line)

  accumulator += findValue(line)

  linesSeen.append(number)

  lastNumber = number
  # print("the last number was" , lastNumber)

  number += getNextLine(line)
  # print("the new number is:", number)

  if number in linesSeen:
    print("The accumulator is currently at", accumulator, "when a line is repeated.")
    print("The last number was at line:", lastNumber)
  elif number == 648:
     print("The accumlator is currently at", accumulator, "and the program has finished running.")
  else:
    dayEight(number, puzzleInput, accumulator, linesSeen)


def findValue(line):
  if line.startswith("nop") or line.startswith("jmp"):
    return 0
  else:
    numbersOnly = line[4:]
    # print("The accumulator should increase by:", numbersOnly)
    return int(numbersOnly)

def getNextLine(line):
  if line.startswith("nop") or line.startswith("acc"):
    return 1
  else:
    numbersOnly = line[4:]
    # print("The next line should be increased  by:", numbersOnly)
    return int(numbersOnly)


dayEight(1, rawPuzzleInput, 0, [])