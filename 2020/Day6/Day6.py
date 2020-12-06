from collections import Counter

# after flying we need to fill out customs
# for everyone on the plane

rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = rawPuzzleInput.readlines()

def daySixPartOne(puzzleInput):
  # this counts each time a single person in the group
  # answered yes to a question and sums the entire plane
  sum = 0
  groupYeses = set()

  for line in puzzleInput:
    line = line.strip('\n')
    line = list(line)

    if len(line) == 0:
      sum = sum + len(groupYeses)
      groupYeses.clear()

    groupYeses.update(line)

  sum = sum + len(groupYeses)

  return sum

print("The sum of a single person in the group answering yes:", daySixPartOne(formattedPuzzleInput))

def daySixPartTwo(puzzleInput):
  # this counts each time a EVERY person in the group
  # answered yes to a question and sums the entire plane
  sum = 0
  groupSize = 0
  groupYesses = []

  for line in puzzleInput:
    line = line.strip('\n')
    line = list(line)

    if len(line) == 0:
      counts = Counter(groupYesses)
      allAnsweredYes = set([letter for letter in groupYesses if counts[letter] == groupSize])
      sum = sum + len(allAnsweredYes)
      groupYesses.clear()
      groupSize = 0
    else:
      groupSize += 1
      groupYesses.extend(line)

  counts = Counter(groupYesses)
  allAnsweredYes = set([letter for letter in groupYesses if counts[letter] == groupSize])
  sum = sum + len(allAnsweredYes)

  return sum

print("The sum of everyone in the group answering yes:", daySixPartTwo(formattedPuzzleInput))