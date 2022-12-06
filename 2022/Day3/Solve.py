import sys
from iteration_utilities import grouper
import itertools

sys.path.append("..")

from Parsers import Parse


def day_three():
  parse = Parse()
  rucksacks = parse.equally_split_line("PuzzleInput.txt")
  print("The answer to part one is", part_one(rucksacks))
  print("The answer to part two is", part_two(rucksacks))


def part_one(rucksacks):
  total_priority_sum = 0

  for rucksack in rucksacks:
    compartment_one, compartment_two = set(rucksack[0]), set(rucksack[1])
    shared_component = compartment_one.intersection(compartment_two)

    total_priority_sum += prioritize_item(shared_component.pop())

  return total_priority_sum


def part_two(rucksacks):
  total_priority_sum = 0

  for group in grouper(rucksacks, 3):
    elf_one, elf_two, elf_three = set(list(itertools.chain.from_iterable(group[0]))), \
                                  set(list(itertools.chain.from_iterable(group[1]))), \
                                  set(list(itertools.chain.from_iterable(group[2])))
    badge = elf_one.intersection(elf_two)
    badge = badge.intersection(elf_three)

    total_priority_sum += prioritize_item(badge.pop())

  return total_priority_sum


def prioritize_item(item):
  if item.isupper():
    return ord(item) - ord("A") + 27
  else:
    return ord(item) - ord("a") + 1


if __name__ == "__main__":
  day_three()
