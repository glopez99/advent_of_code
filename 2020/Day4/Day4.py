import re

rawPuzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = rawPuzzleInput.readlines()


def dayFour(PuzzleInput):
  totalValidPassports = 0

  byr, iyr, eyr, hgt, hcl, ecl, pid = 0, 0, 0, 0, 0, 0, 0

  for line in PuzzleInput:
    strippedLine = line.strip('\n')
    parsedLine = re.split(' |, |:', strippedLine)
    

    if len(parsedLine) <= 1:
      byr, iyr, eyr, hgt, hcl, ecl, pid = 0, 0, 0, 0, 0, 0, 0

    if 'byr' in parsedLine:
      byr = checkBYRValidity(parsedLine)
    
    if 'iyr' in parsedLine:
      iyr = checkIYRValidity(parsedLine)
    
    if 'eyr' in parsedLine:
      eyr = checkEYRValidity(parsedLine)
    
    if 'hgt' in parsedLine:
      hgt = checkHGTValidity(parsedLine)
    
    if 'hcl' in parsedLine:
      hcl = checkHCLValidity(parsedLine)

    if 'ecl' in parsedLine:
      ecl = checkECLValidity(parsedLine)
    
    if 'pid' in parsedLine:
      pid = checkPIDValidity(parsedLine)

    if byr + iyr + eyr + hgt + hcl + ecl + pid == 7:
      totalValidPassports += 1
      byr, iyr, eyr, hgt, hcl, ecl, pid = 0, 0, 0, 0, 0, 0, 0
  
  return totalValidPassports

def checkBYRValidity(parsedLine):
  index = parsedLine.index("byr")

  if 1920 <= int(parsedLine[index + 1]) <= 2002:
    return 1
  else:
    return 0

def checkIYRValidity(parsedLine):
  index = parsedLine.index("iyr")

  if 2010 <= int(parsedLine[index + 1]) <= 2020:
    return 1
  
  return 0

def checkEYRValidity(parsedLine):
  index = parsedLine.index("eyr")

  if 2020 <= int(parsedLine[index + 1]) <= 2030:
    return 1

  return 0

def checkHGTValidity(parsedLine):
  index = parsedLine.index("hgt")

  if re.search("in", parsedLine[index + 1]):
    removedWhiteSpace = ''.join(parsedLine[index + 1].split())
    height = removedWhiteSpace[:-2]
    if 59 <= int(height) <= 76:
      return 1
  
  if re.search("cm", parsedLine[index + 1]):
    removedWhiteSpace = ''.join(parsedLine[index + 1].split())
    height = removedWhiteSpace[:-2]
    if 150 <= int(height) <= 193:
      return 1
  
  return 0

def checkHCLValidity(parsedLine):
  index = parsedLine.index("hcl")

  if re.search('#', parsedLine[index + 1]):
    if len(parsedLine[index + 1]) == 7:
      return 1
    else:
      return 0
  
  return 0

def checkECLValidity(parsedLine):
  index = parsedLine.index("ecl")

  if parsedLine[index + 1] == "amb" or parsedLine[index + 1] == "blu" or parsedLine[index + 1] == "brn" or parsedLine[index + 1] == "gry" or parsedLine[index + 1] == "grn" or parsedLine[index + 1] == "hzl" or  parsedLine[index + 1] == "oth":
    return 1
  
  return 0

def checkPIDValidity(parsedLine):
  index = parsedLine.index("pid")

  if len(parsedLine[index + 1]) == 9:
    return 1
  
  return 0

print(dayFour(formattedPuzzleInput))