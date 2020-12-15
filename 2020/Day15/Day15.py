puzzleInput = [17,1,3,16,19,0]

def dayFifteen(puzzleInput):
  numbersSaid = puzzleInput.copy()[:-1]
  turnSaid = {17: 1, 1: 2, 3: 3, 16: 4, 19: 5}
  lastNumberSaid = puzzleInput[-1]
  turn = len(puzzleInput)+1
  

  while turn <= 2020:
    if lastNumberSaid in numbersSaid:
      currentSaid = (turn - 1) - turnSaid[lastNumberSaid]
      turnSaid[lastNumberSaid] = turn - 1
      lastNumberSaid = currentSaid
    else:
      numbersSaid.append(lastNumberSaid)
      turnSaid[lastNumberSaid] = turn - 1
      lastNumberSaid = 0

    turn += 1

  print("The answer to part one is", lastNumberSaid)

      



if __name__ == "__main__":
    dayFifteen(puzzleInput)