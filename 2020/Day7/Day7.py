import re

# We're now dealing with baggage rules
# bags must be color-coded and must contain specific quantities of 
# other color-coded bags. Part one counts: How many bag colors can 
# eventually contain at least one shiny gold bag? Part two counts:
# How many individual bags are required inside your single shiny gold bag?

rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = rawPuzzleInput.readlines()

def daySix(puzzleInput):
  # this function has the wrong answer and I don't know why
  # my recursion function has the right answer and I don't see
  # why it's dropping items when returning
  totalBags = 0

  totalBags = bagCount("shiny gold", puzzleInput) 

  print("This is the right answer:", totalBags)

def bagCount(color, input):
  totalBags = 0

  line = findLine(color, input)
  #print("This is the line with the bag in it:", line)

  splitLine = line.split(',')

  for section in splitLine:
    # print("this is the section:", section)
    number = re.findall('[0-9]+', section)
    # print("the number is:", number)
    if len(number) > 0:
      color = findColor(section, number[0])
      #print("The next color is:", color)
      totalBags += int(number[0]) + (int(number[0]) * bagCount(color, input))
      #print("Total Bags is currently at:", totalBags)

  return totalBags

def findLine(color, input):
  for line in input:
    if line.startswith(color):
      return line

def findColor(line, number):
  splitLine = line.split()
  # print("the split line is:", splitLine)
  index = splitLine.index(number[0])
  # print("the index is:", index)
  color = splitLine[index + 1] + ' ' + splitLine[index + 2]

  return color
  
def possibleBagsPartOne(colors, knownBags, puzzleInput):
  # this recursive function gives you the correct answer by going through
  # the colors given to it, and finding how many bags are in it. It
  # then repeats with the new colors until the set no longer has new items 
  # added to it

  bagColors  = colors
  newBagColors = []
  bagsToCarry = set(knownBags)
  count = len(bagsToCarry)

  for color in bagColors:
    for line in puzzleInput:
      if color in line:
        splitLine = line.split()
        bagColor = str(splitLine[0] + ' ' + splitLine[1])
        if bagColor != color:
          newBagColors.append(bagColor)
  
  bagsToCarry.update(newBagColors)

  if len(bagsToCarry) > count:
    possibleBagsPartOne(newBagColors, bagsToCarry, puzzleInput)
    return count
  
  print("Use this number:", count)
  return count


daySix(formattedPuzzleInput)