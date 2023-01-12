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

    rope_part_one = Rope()
    rope_part_one.add_segment_to_end(Rope_Segment())
    rope_part_one.add_segment_to_end(Rope_Segment())

    rope_part_two = Rope()
    for i in range(10):
      rope_part_two.add_segment_to_end(Rope_Segment())

    tail_locations_part_one = set()
    tail_locations_part_two = set()

    for instruction in instructions:
      tail_locations_part_one.update(self.move_rope(instruction, rope_part_one))
      tail_locations_part_two.update(self.move_rope(instruction, rope_part_two))

    print("The answer to part one is", len(tail_locations_part_one))
    print("The answer to part two is", len(tail_locations_part_two))

  def move_rope(self, instruction, rope):
    tail_locations = set()

    for i in range(instruction.get_times()):
      rope.move_segments(instruction.get_direction())
      tail_locations.add((rope.get_tail().get_x(), rope.get_tail().get_y()))

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
    x_diff = rope_segment.get_x() - self.x
    y_diff = rope_segment.get_y() - self.y

    if max(abs(x_diff), abs(y_diff)) <= 1:
      return

    self.x += self.signum(x_diff)
    self.y += self.signum(y_diff)

  def signum(self, n):
    return 0 if n == 0 else n / abs(n)

  def get_x(self):
    return self.x

  def get_y(self):
    return self.y


class Rope(object):
  rope_segments: []

  def __init__(self):
    self.rope_segments = []

  def get_head(self):
    return self.rope_segments[0]

  def get_tail(self):
    return self.rope_segments[-1]

  def add_segment_to_end(self, rope_segment):
    self.rope_segments.append(rope_segment)

  def move_segments(self, direction):
    self.rope_segments[0].move(direction)

    for i in range(1, len(self.rope_segments)):
      self.rope_segments[i].follow(self.rope_segments[i-1])


if __name__ == "__main__":
  Day_Nine().day_nine()