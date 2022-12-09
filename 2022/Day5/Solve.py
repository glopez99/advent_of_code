from collections import deque


class Day_Five(object):

  def parse(self, puzzle_input):
    directions = []
    cargo_hold = Cargo_Hold()

    with open(puzzle_input, "r") as f:
      for line in f:

        if "[" in line:
          boxes = [line[i:i + 4] for i in range(0, len(line), 4)]

          for i in range(len(boxes)):
            box = boxes[i][1].strip()
            if box:
              cargo_hold.add_boxes(box, i+1)
          continue

        if line.startswith("move"):
          split_line = line.strip().split(" ")
          instruction = Instructions(split_line[1], split_line[3], split_line[5])
          directions.append(instruction)

    return cargo_hold, directions

  def day_five(self):
    cargo_hold, directions = self.parse("PuzzleInput.txt")
    self.part_one(cargo_hold, directions)

  def part_one(self, cargo_hold, directions):
    for direction in directions:
      cargo_hold.move_boxes(direction)

    print("The answer to part one is", "".join(cargo_hold.get_top_boxes()))


class Cargo_Hold(object):
  stacks = dict()

  def add_boxes(self, box, stack):
    stack = str(stack)
    if stack in self.stacks:
      self.stacks[stack].append(box)
    else:
      new_stack = deque()
      new_stack.append(box)
      self.stacks[stack] = new_stack

  def move_boxes(self, instructions):
    from_stack = self.stacks[instructions.from_stack]
    to_stack = self.stacks[instructions.to_stack]

    for i in range(instructions.number_of_boxes):
      box = from_stack.popleft()
      to_stack.appendleft(box)

  def get_top_boxes(self):
    top_boxes = []

    for i in range(len(self.stacks)):
      box = self.stacks[str(i+1)][0]
      top_boxes.append(box)

    return top_boxes


class Instructions(object):
  number_of_boxes: int
  from_stack: int
  to_stack: int

  def __init__(self, number_of_boxes, from_stack, to_stack):
    self.number_of_boxes = int(number_of_boxes)
    self.from_stack = from_stack
    self.to_stack = to_stack


if __name__ == "__main__":
  Day_Five().day_five()
