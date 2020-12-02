rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = rawPuzzleInput.readlines()

def dayTwo(PuzzleInput):
  validPasswords = 0
  for password in PuzzleInput:
    if checkValidity(password) == True:
      validPasswords += 1
  
  return validPasswords

# def checkValidity(passwordRule):
#   # for part One
#   splitPasswordRule = passwordRule.split(':')
#   splitRule = splitPasswordRule[0].split(' ')
#   splitValues = splitRule[0].split('-')
#   
#   password = splitPasswordRule[1]
#   
#   if int(splitValues[0]) <= password.count(splitRule[1]) <= int(splitValues[1]):
#     return True
#   else:
#     return False

def checkValidity(passwordRule):
  # for part Two
  splitPasswordRule = passwordRule.split(':')
  splitRule = splitPasswordRule[0].split(' ')
  splitValues = splitRule[0].split('-')
  
  password = list(splitPasswordRule[1])
  letterToFind = splitRule[1]
  firstLocation = int(splitValues[0])
  secondLocation = int(splitValues[1])

  if checkForLetter(password, firstLocation, letterToFind) == True and checkForLetter(password, secondLocation, letterToFind) == True:
    return False

  if checkForLetter(password, firstLocation, letterToFind) == True and checkForLetter(password, secondLocation, letterToFind) == False:
    return True

  if checkForLetter(password, firstLocation, letterToFind) == False and checkForLetter(password, secondLocation, letterToFind) == True:
    return True

  return False

def checkForLetter(password, location, letter):
  if location >= len(password):
    return False

  if password[location] == letter:
    return True
  else:
    return False
 

print(dayTwo(formattedPuzzleInput))