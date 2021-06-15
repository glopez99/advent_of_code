# create a set that has only the black tiles
# give each tile a location that I can check against

# puzzleInput = open("TestInput.txt","r")
# puzzleInput = puzzleInput.readlines()
directions = []

with open("TestInput.txt", "r") as f:
  for line in f:
    split = list(line.strip())
    direction = []
    while len(split) != 0:
      if split[0] == "s" or split[0] == "n":
        direction.append(split[0] + split[1])
        split = split[2:]
      else:
        direction.append(split[0])
        split = split[1:]
    directions.append(direction)

def dayTwentyFour(input):
  blackTiles = set()

  for directions in input:
    location = getLocation(directions)

    if location in blackTiles:
      blackTiles.remove(location)
    else:
      blackTiles.add(location)

  print("The answer to Part One is:", len(blackTiles))

  for i in range(100):
    print(i)
    blackTiles = calculateNextState(blackTiles)

  print("The answer to Part Two is:", len(state))


def getLocation(line):
  # based on the direction, change the location, starting location is 0,0
  # return the location
  x = 0
  y = 0
  z = 0

  for direction in line:
    if direction == "e":
      x += 1
      y -= 1
    
    if direction == "se":
      y -= 1
      z += 1

    if direction == "sw":
      x -= 1
      z += 1

    if direction == "w":
      x -= 1
      y += 1
    
    if direction == "nw":
      y += 1
      z -= 1
    
    if direction == "ne":
      x += 1
      z -= 1

  return (x,y,z)


def calculateNextState(previous):
  nextState = stayBlack(previous).union(turnBlack(previous))

  return nextState

def getNeighbor(location):
  neighbors = []

  for dx in range(-1, 2):
    x = location[0] + dx
    for dy in range(-1, 2):
      y = location[1] + dy
      for dz in range(-1, 2):
        z = location[2] + dz
        if x == location[0] and y == location[1] and z == location[2]:
          continue
  
        neighbors.append((x, y, z))
  
  return neighbors

def stayBlack(previous):
  stayingBlack = set()
  
  for location in previous:
    if countActiveNeighbors(location, previous) == 1 or countActiveNeighbors(location, previous) == 2:
      stayingBlack.add(location)

  return stayingBlack
  
def turnBlack(previous):
  turningBlack = set()

  for location in previous:

      for neighbor in getNeighbor(location):
      
        if neighbor in previous:
          continue

        if countActiveNeighbors(neighbor, previous) == 2:
          turningBlack.add(neighbor)
  
  return turningBlack

def countActiveNeighbors(location, state):
  count = 0

  for neighbor in getNeighbor(location):
    if neighbor in state:
      count += 1

  return count

if __name__ == "__main__":
  dayTwentyFour(directions)