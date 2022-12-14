class Day_Six(object):
  def parse(self, input):
    with open(input, "r") as f:
      return f.read()

  def day_six(self):
    puzzle_input = self.parse("PuzzleInput.txt")
    print("The answer to part one is", self.detection(puzzle_input, 4))
    print("The answer to part two is", self.detection(puzzle_input, 14))

  def detection(self, puzzle_input, number_of_chars):
    for i in range(len(puzzle_input)):
      if len(set(puzzle_input[i:i+number_of_chars])) == number_of_chars:
        return i + number_of_chars


if __name__ == "__main__":
  Day_Six().day_six()
