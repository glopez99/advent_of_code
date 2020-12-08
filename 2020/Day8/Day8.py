import linecache

rawPuzzleInput = "PuzzleInput.txt"

def dayEight(number, puzzleInput, accumulator, linesSeen):
  accumulator = accumulator
  linesSeen = linesSeen

  line = linecache.getline(puzzleInput, number)
  print("the line is:", line)

  accumulator += findValue(line)
  # print("the accumulator currently is:", accumulator)

  linesSeen.append(number)
  # print("the new lines seen is:", linesSeen)

  lastNumber = number
  print("the last number was" , lastNumber)

  number += getNextLine(line)
  print("the new number is:", number)

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

def getSwitchedLine(line):
  if line.startswith("nop"):
    numbersOnly = line[4:]
    # print("The next line should be increased  by:", numbersOnly)
    return int(numbersOnly)
  elif line.startswith("jmp") or line.startswith("acc"):
    return 1

def checkIfThisIsTheLineToSwitch(count, switch):
  if count == switch:
    return True
  else:
    return False

def addtoCount(line):
  if line.startswith("acc"):
    return 0
  else:
    return 1

dayEight(1, rawPuzzleInput, 0, [])