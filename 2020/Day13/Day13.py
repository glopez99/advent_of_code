from sympy.ntheory.modular import crt

buses = [19,'x','x','x','x','x','x','x','x',41,'x','x','x','x','x','x','x','x','x',743,'x','x','x','x','x','x','x','x','x','x','x','x',13,17,'x','x','x','x','x','x','x','x','x','x','x','x','x','x',29,'x',643,'x','x','x','x','x',37,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',23]

def DayThirteenPartTwo(puzzleInput):
  buses = [x for x in puzzleInput if type(x) is int]
  
  for bus in puzzleInput:
    if bus != 'x':
      buses.append(bus)

  moduloBuses = []
  
  for i, bus in enumerate(puzzleInput):
    if bus != 'x':
      moduloBuses.append(-i % bus)
  
  partTwoAnswer = crt(buses, moduloBuses)
  print ("the answer to part two is", partTwoAnswer[0])


def DayThirteenPartOne(puzzleInput):
  time = 1015292
  buses = []
  busToTake = 0
  earliestTime = time * 2

  for bus in puzzleInput:
    if bus != 'x':
      buses.append(bus)

  for bus in buses:
    nearestTime = bus * round(time/bus)
  
    if time < nearestTime < earliestTime:
      earliestTime = nearestTime
      busToTake = bus

  print("The answer to part one is", busToTake * (earliestTime - time)) 

DayThirteenPartOne(buses)
DayThirteenPartTwo(buses)
