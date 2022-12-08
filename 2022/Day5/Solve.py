class Day_Five(object):

  def parse(self, puzzle_input):
    directions = []
    cargo_hold = Cargo_Hold()

    with open(puzzle_input, "r") as f:
      # do things here

    return cargo_hold, directions


  def day_five(self):
    cargo_hold, directions = self.parse("TestInput.txt")
    self.part_one(cargo_hold, directions)


  def part_one(self, cargo_hold, directions):
    top_boxes = ""
    print("The answer to part one is", top_boxes)

class Cargo_Hold(object):




if __name__ == "__main__":
  Day_Five.day_five()