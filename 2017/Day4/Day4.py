
rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = rawPuzzleInput.readlines()

def dayFourPartOne (input):
  count = 0

  for phrase in input:
    count = count + checkForDuplicates(phrase)

  return count


def checkForDuplicates(passphrase):
  phrase = passphrase.split()
  distinct = set(phrase)
  if len(distinct) == len(phrase):
    anagram = checkForAnagram(phrase)
    return anagram
  return 0

def checkForAnagram(passphrase):
  for word in passphrase:
    sortedWord = sorted(word)
    for nextWord in passphrase:
      if word == nextWord: pass
      elif sorted(nextWord) == sortedWord: return 0
  return 1


print(dayFourPartOne(formattedPuzzleInput))