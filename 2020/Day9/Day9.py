# create class for puzzle input - have a copy method and have a checkForSum method
# OO - defining a way to store data and providing methods to use data - tie logic with data into one contigous piece
# by doing this - we can add methods or change how the data is stored without having to change it in every place
# class - you're defining the contract - as long as it's robust it won't break - but if you have a bad contract - things break
# keep it simple - just because you CAN divide the data - doesn't mean you SHOULD - make sure that it provides benefit before abstracting


# could make a base class called AOC puzzle - what's in here - this is where you put in the method to read the data

class Solution: # if putting () here - that's where you define where this inherits from
  # formattedPuzzleInput = []
  
  def __init__(self): # if putting parameters in to define things - this is where they would come in
    # put things in here that you only need to do once
    rawPuzzleInput = open('PuzzleInput.txt', 'r')
    self.formattedPuzzleInput = [ int(line) for line in rawPuzzleInput.readlines() ]
    # can leave here and pass into other defs as self.formatted.... - but when you change you need to use .deepcopy()
  
  def dayNinePartOne (self, startingPoint, puzzleInput):
  # this checks the validity if two numbers in the previous 25 equal
  # the number in the starting Point location. If it returns true,
  # it will move one number down the list and keep checking. If it returns
  # false, it will print that number.
    if self.checkValidity(startingPoint, puzzleInput):
      startingPoint += 1

      self.dayNinePartOne(startingPoint, puzzleInput)
    else:
      number = puzzleInput[startingPoint]
      print("the number that returned as false is", number)

  def checkValidity(self, startingPoint, lineToCheck):
    previous25 = lineToCheck[(startingPoint - 25):(startingPoint)]
    numberToCheck = lineToCheck[startingPoint]

    for numberOne in previous25:
      for numberTwo in previous25:
        if numberOne != numberTwo:
          if numberOne + numberTwo == numberToCheck:
            return True

    return False

  def dayNinePartTwo (self, numberToCheck):
  # loops through the puzzle input walking from the front of the list
  # to the back of the list until it finds the solution
    partTwoPuzzleInput = self.formattedPuzzleInput[:562] #make a deepcopy here and then go forth

    encryptionWeakness = self.checkForSum(numberToCheck, partTwoPuzzleInput)

    if  encryptionWeakness == None or encryptionWeakness == 0:
      if len(puzzleInput) > 1:
        puzzleInput = puzzleInput[1:]
        self.dayNinePartTwo(numberToCheck, puzzleInput)
      else:
        print("there is an error")
    elif encryptionWeakness != 0 or encryptionWeakness != None:
      print("The encryption weakness is", encryptionWeakness)

  def checkForSum (self, numberToCheck, puzzleInput):
  # loops through the puzzle inputs to see if the current input
  # has the list that equals the number. If it's too large, it
  # slices a number off the end, if it's too small, it returns 0,
  # if it does equal the number - it returns the encryption weakness (aka solution)
    if sum(puzzleInput) == numberToCheck:
      return min(puzzleInput) + max(puzzleInput)
    elif sum(puzzleInput) > numberToCheck:
      newPuzzleInput = puzzleInput[:-1]
      # print("the number was too large. the new puzzle input is:", puzzleInput)
      return self.checkForSum(numberToCheck, newPuzzleInput)
    elif sum(puzzleInput) < numberToCheck:
      return 0

  def runSolution(self):
    # found the location of my number -  you don't have to check past this number as 
    # everything past this number will be larger
    self.dayNinePartOne(25, formattedPuzzleInput)
    self.dayNinePartTwo(144381670, partTwoPuzzleInput)


if __name__ == "__main__":
  s = Solution() # this constructs an INSTANCE of the Solution class - could have an s2 = Solution() but that doesn't mean it's the same
  s.runSolution() # this then executes it
