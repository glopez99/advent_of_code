puzzleInput = open('PuzzleInput.txt', 'r')
formattedPuzzleInput = puzzleInput.readlines()

def dayTwelve(input):
  partOneShipCoordinates = findShipCoordinatesPartOne(input)
  print("The ship coordinates for part one are", partOneShipCoordinates)

  print("The manhattan distance for the part one coordinates is", sum(partOneShipCoordinates))

  partTwoShipCoordinates = findShipCoordinatesPartTwo(input)
  print("The ship coordinates for part two are", partTwoShipCoordinates)

  print("The manhattan distance for the part two coordinates is", sum(partTwoShipCoordinates))

def findShipCoordinatesPartOne(input):
  east = 0
  west = 0
  north = 0
  south = 0
  directionFacing = "East"

  for line in input:
    if line.startswith("E") or (line.startswith("F") and directionFacing == "East"):
      east += int(line[1:])
    if line.startswith("W") or (line.startswith("F") and directionFacing == "West"):
      west += int(line[1:])
    if line.startswith("N") or (line.startswith("F") and directionFacing == "North"):
      north += int(line[1:])
    if line.startswith("S") or (line.startswith("F") and directionFacing == "South"):
      south += int(line[1:])
    if line.startswith("R") or line.startswith("L"):
      directionFacing = findDirectionFacing(directionFacing, line)

  return abs(east - west), abs(north - south)

def findDirectionFacing(currentDirection, line):
  compass = ["North", "East", "South", "West"]
  currentLocation = compass.index(currentDirection)
  turn = int(line[1:])/90
  # print("The turn ask is", int(line[1:]))
  # print("the boat is turning", turn, "degrees")

  if line.startswith("R"):
    newLocation = int((currentLocation + turn)) % 4
    # print("the new direction facing is", newLocation)
    return compass[newLocation]

  if line.startswith("L"):
    newLocation = int((currentLocation - turn)) % 4
    return compass[newLocation]

def findShipCoordinatesPartTwo(input):
  east = 0
  west = 0
  north = 0
  south = 0
  waypointArray = [1, 10, 0, 0]

  for line in input:
    if line.startswith("N"):
      waypointArray[0] = waypointArray[0] + int(line[1:])
    
    if line.startswith("E"):
      waypointArray[1] = waypointArray[1] + int(line[1:])
    
    if line.startswith("S"):
      waypointArray[2] = waypointArray[2] + int(line[1:])
    
    if line.startswith("W"):
      waypointArray[3] = waypointArray[3] + int(line[1:])
    
    if line.startswith("R") or line.startswith("L"):
      waypointArray = findWayPoint(waypointArray, line)
    
    if line.startswith("F"):
      north += int(line[1:]) * waypointArray[0]
      east += int(line[1:]) * waypointArray[1]
      south += int(line[1:]) * waypointArray[2]
      west += int(line[1:]) * waypointArray[3]

  return abs(east - west), abs(north - south)

def findWayPoint(currentWaypoint, line):
  turn = int(line[1:])/90
  newWayPoint = [0, 0, 0, 0]

  if line.startswith("R"):
    northIndex = int(0 + turn) % 4
    eastIndex = int(1 + turn) % 4
    southIndex = int(2 + turn) % 4
    westIndex = int(3 + turn) % 4

    newWayPoint[northIndex] = currentWaypoint[0]
    newWayPoint[eastIndex] = currentWaypoint[1]
    newWayPoint[southIndex] = currentWaypoint[2]
    newWayPoint[westIndex] = currentWaypoint[3]
  
  if line.startswith("L"):
    northIndex = int(0 - turn) % 4
    eastIndex = int(1 - turn) % 4
    southIndex = int(2 - turn) % 4
    westIndex = int(3 - turn) % 4

    newWayPoint[northIndex] = currentWaypoint[0]
    newWayPoint[eastIndex] = currentWaypoint[1]
    newWayPoint[southIndex] = currentWaypoint[2]
    newWayPoint[westIndex] = currentWaypoint[3]

  return newWayPoint


dayTwelve(formattedPuzzleInput)
