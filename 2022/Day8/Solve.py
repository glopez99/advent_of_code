class Day_Eight(object):
  def parse(self, input):
    forest = []
    with open(input, "r") as f:
      for line in f:
        row = []
        for tree in list(line.strip()):
          row.append(Tree(int(tree)))
        forest.append(row)

    for row in forest:
      row_index = forest.index(row)
      for tree in row:
        tree_index = row.index(tree)

        if row_index == 0:
          up = None
          down = forest[row_index + 1][tree_index]
        elif row_index == len(forest) - 1:
          up = forest[row_index - 1][tree_index]
          down = None
        else:
          up = forest[row_index - 1][tree_index]
          down = forest[row_index + 1][tree_index]

        if tree_index == 0:
          left = None
          right = row[tree_index+1]
        elif tree_index == len(row)-1:
          left = row[tree_index-1]
          right = None
        else:
          left = row[tree_index-1]
          right = row[tree_index+1]

        tree.add_neighbor(left, right, up, down)

    return sum(forest, [])

  def day_eight(self):
    forest = self.parse("PuzzleInput.txt")
    visible_trees = list(filter(self.is_visible, forest))
    scenic_scores = list(map(self.find_scenic_score, forest))
    print("The answer to part one", len(visible_trees))
    print("The answer to part two is", max(scenic_scores))

  def is_visible(self, tree):
    return tree.check_left(tree.height) or \
           tree.check_right(tree.height) or \
           tree.check_up(tree.height) or \
           tree.check_down(tree.height)

  def find_scenic_score(self, tree):
    if tree.is_edge():
      return 0

    return tree.find_distance_left(tree.height) * \
           tree.find_distance_right(tree.height) * \
           tree.find_distance_up(tree.height) * \
           tree.find_distance_down(tree.height)


class Tree(object):
  height: int
  left = None
  right = None
  up = None
  down = None

  def __init__(self, height):
    self.height = height

  def add_neighbor(self, left, right, up, down):
    self.left = left
    self.right = right
    self.up = up
    self.down = down

  def check_left(self, height_to_check):
    if self.is_edge():
      return True
    elif height_to_check > self.left.height:
      return self.left.check_left(height_to_check)
    else:
      return False

  def check_right(self, height_to_check):
    if self.is_edge():
      return True
    elif height_to_check > self.right.height:
      return self.right.check_right(height_to_check)
    else:
      return False

  def check_down(self, height_to_check):
    if self.is_edge():
      return True
    elif height_to_check > self.down.height:
      return self.down.check_down(height_to_check)
    else:
      return False

  def check_up(self, height_to_check):
    if self.is_edge():
      return True
    elif height_to_check > self.up.height:
      return self.up.check_up(height_to_check)
    else:
      return False

  def is_edge(self):
    if self.left is None or \
      self.right is None or \
      self.up is None or \
      self.down is None:
      return True
    else:
      return False

  def find_distance_left(self, height_to_check):
    if self.is_edge():
      return 0
    elif height_to_check > self.left.height:
      return 1 + self.left.find_distance_left(height_to_check)
    else:
      return 1

  def find_distance_right(self, height_to_check):
    if self.is_edge():
      return 0
    elif height_to_check > self.right.height:
      return 1 + self.right.find_distance_right(height_to_check)
    else:
      return 1

  def find_distance_up(self, height_to_check):
    if self.is_edge():
      return 0
    elif height_to_check > self.up.height:
      return 1 + self.up.find_distance_up(height_to_check)
    else:
      return 1

  def find_distance_down(self, height_to_check):
    if self.is_edge():
      return 0
    elif height_to_check > self.down.height:
      return 1 + self.down.find_distance_down(height_to_check)
    else:
      return 1


if __name__ == "__main__":
  Day_Eight().day_eight()
