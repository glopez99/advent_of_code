# keeping track of those locations lets you decide what turns on or off?
# like, all you care about is location really. So as long as you know what’s on - 
# you know everything else is off
# Yeah, that's one way to deal with infinite space - you define all "on" cells as 
# "in the set", and all "off" cells as "not in the set"
# then each round you move cells based on the rules (which are checked by the sets)
# use sets so you never get a duplicate and thus don’t have to worry about duplicates 
# living there
# so you can write everything to either be added/removed
# thus getting rid of (if in set already ) type logic
# Though... one thing with cellular automata is that the rules are always based on 
# the previous state, so instead of add/remove on the existing state, 
# it may be easier to just craft the new state.

startingState = set()

with open("PuzzleInput.txt", "r") as f:
  z = 0
  w = 0
  for y, line in enumerate(f):
    splitLine = list(line)
    for x, activity in enumerate(splitLine):
      if activity == '#':
        startingState.add((x, y, z, w))

def daySeventeen(state):
  for round in range(6):
    state = calculateNextState(state)

  print("The answer to Part Two is:", len(state))

def calculateNextState(previous):
  nextState = stayOn(previous).union(turnOn(previous))

  return nextState

def getNeighbor(location):
  neighbors = []

  for dx in range(-1, 2):
    x = location[0] + dx
    for dy in range(-1, 2):
      y = location[1] + dy
      for dz in range(-1, 2):
        z = location[2] + dz
        for dw in range(-1, 2):
          w = location[3] + dw
          if x == location[0] and y == location[1] and z == location[2] and w == location[3]:
           continue
  
          neighbors.append((x, y, z, w))
  
  return neighbors

def stayOn(previous):
  stayingOn = set()
  
  for location in previous:
    if 2 <= countActiveNeighbors(location, previous) <= 3:
      stayingOn.add(location)

  return stayingOn
  
def turnOn(previous):
  turningOn = set()

  for location in previous:

      for neighbor in getNeighbor(location):
      
        if neighbor in previous:
          continue

        if countActiveNeighbors(neighbor, previous) == 3:
          turningOn.add(neighbor)
  
  return turningOn

def countActiveNeighbors(location, state):
  count = 0

  for neighbor in getNeighbor(location):
    if neighbor in state:
      count += 1

  return count

if __name__ == "__main__":
  daySeventeen(startingState)