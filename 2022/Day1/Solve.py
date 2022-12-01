# RFC:

elvesCaloricInventories = []
with open("PuzzleInput.txt", "r") as f:
  elfInventory = []
  for line in f:
    if line.strip():
      elfInventory.append(int(line))
    else:
      elvesCaloricInventories.append(elfInventory)
      elfInventory = []
  elvesCaloricInventories.append(elfInventory)

def dayOne():
  sumCaloricInventories = []

  for elf in elvesCaloricInventories:
    sumCaloricInventories.append(sum(elf))

  sumCaloricInventories.sort(reverse=True)

  print("The solution to part one is ", max(sumCaloricInventories))
  print("The solution to part two is", sum(sumCaloricInventories [:3]))


if __name__ == "__main__":
  dayOne()
