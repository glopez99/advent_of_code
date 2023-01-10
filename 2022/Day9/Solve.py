class Day_Nine(object):
  def parse(self, puzzle_input):
    instructions = []
    with open(puzzle_input, "r") as f:
      for line in f:
        split_line = line.split()
        instruction = Instruction(split_line[0], split_line[1])
        instructions.append(instruction)

    return instructions

  def day_nine(self):
    instructions = self.parse('PuzzleInput.txt')
    head = Rope_Segment()
    tail = Rope_Segment()
    tail_locations = set()

    for instruction in instructions:
      tail_locations.update(self.move_rope(instruction, head, tail))

    print("The answer to part one is", len(tail_locations))

  def move_rope(self, instruction, head, tail):
    i = 0
    tail_locations = set()

    while i < instruction.get_times():
      head.move(instruction.get_direction())
      tail.follow(head)
      tail_locations.add((tail.get_x(), tail.get_y()))
      i += 1

    return tail_locations


class Instruction(object):
  direction: str
  times: int

  def __init__(self, direction, times):
    self.direction = direction
    self.times = int(times)

  def get_direction(self):
    return self.direction

  def get_times(self):
    return self.times


class Rope_Segment(object):
  x: int
  y: int

  def __init__(self):
    self.x = 0
    self.y = 0

  def move(self, direction):
    if direction.upper() == "R":
      self.x += 1
    elif direction.upper() == "L":
      self.x -= 1
    elif direction.upper() == "U":
      self.y += 1
    elif direction.upper() == "D":
      self.y -= 1
    else:
      print("There is an error in the move method.", direction)

  def follow(self, rope_segment):
    x_diff = self.x - rope_segment.get_x()
    y_diff = self.y - rope_segment.get_y()
    move_diagonally = self.move_diagonally(x_diff, y_diff)

    if x_diff < -1:
      self.x += 1
    elif x_diff > 1:
      self.x -= 1
    elif x_diff == -1 and move_diagonally:
      self.x += 1
    elif x_diff == 1 and move_diagonally:
      self.x -= 1

    if y_diff < -1:
      self.y += 1
    elif y_diff > 1:
      self.y -= 1
    elif y_diff == -1 and move_diagonally:
      self.y += 1
    elif y_diff == 1 and move_diagonally:
      self.y -= 1

  def move_diagonally(self, x_diff, y_diff):
    if (-1 > y_diff or y_diff > 1) and (x_diff == -1 or x_diff == 1):
      return True
    elif (-1 > x_diff or x_diff > 1) and (y_diff == -1 or y_diff == 1):
      return True
    else:
      return False

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y


if __name__ == "__main__":
  Day_Nine().day_nine()