# RFC:

elves_caloric_inventories = []
with open("PuzzleInput.txt", "r") as f:
  elf_inventory = []
  for line in f:
    if line.strip():
      elf_inventory.append(int(line))
    else:
      elves_caloric_inventories.append(elf_inventory)
      elf_inventory = []
  elves_caloric_inventories.append(elf_inventory)


def day_one():
  sum_caloric_inventories = []

  for elf in elves_caloric_inventories:
    sum_caloric_inventories.append(sum(elf))

  sum_caloric_inventories.sort(reverse=True)

  print("The solution to part one is ", max(sum_caloric_inventories))
  print("The solution to part two is", sum(sum_caloric_inventories[:3]))


if __name__ == "__main__":
  day_one()
