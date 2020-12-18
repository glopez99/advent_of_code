puzzleInput = []

with open("PuzzleInput.txt", "r") as f:
  for line in f:
    splitLine = line.replace("(", "( ").replace(")", " )").split()
    puzzleInput.append(splitLine)

def dayEighteen(puzzleInput):
  partTwoAnswer = 0

  for line in puzzleInput:
    # print("the line being mathed is", line)
    partTwoAnswer = partTwoAnswer + doMath(line)
  
  print("The answer to part two is", partTwoAnswer)

def doMath(line):
  total = 0
  nextNumber = 0
  position = -1
  numbersToBeMultipled = []
  # print("the numbers to be multipled", numbersToBeMultipled)

  for i, element in enumerate(line):
    if i <= position:
      continue
    # print("the element being looked at is", element, ", the i is", i, ", the positon is", position)
    if element == "(":
      copiedLine = line.copy()[i+1:]
      parenthesis = doMath(copiedLine)
      # print("the parenthis being returned is", parenthesis)
      total = add(total, parenthesis[0])
      # print("the new total is", total)
      position = parenthesis[1] + i + 1
      continue
    
    if element == ")":
      numbersToBeMultipled.append(total)

      total = 1

      for number in numbersToBeMultipled:
        total = total * number
      return total, i

    if element == "+":
      position = i
      continue

    if element == "*":
      numbersToBeMultipled.append(total)
      # print("the numbers to be multipled is", numbersToBeMultipled)
      position = i
      total = 0
      continue

    position = i
    total = add(total, int(element))
    # print("the new total is", total)

  numbersToBeMultipled.append(total)

  total = 1

  for number in numbersToBeMultipled:
    total = total * number

  return total

def add(total, number):
  return total + number

def multiple(total, number):
  return total * number



if __name__ == "__main__":
  dayEighteen(puzzleInput)