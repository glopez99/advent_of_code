class Day_Six(object):
  def day_six(self):
    computer = self.parse("PuzzleInput.txt")
    computer.calculate_size()
    print("The answer to part one is", computer.sum_all_subdirectories_under_limit(100000))

  def parse(self, puzzle_input):
    current_directory = []
    computer = Directory("dir /")
    with open(puzzle_input, "r") as f:
      for line in f:
        if "cd /" in line:
          current_directory = []
          continue
        if ".." in line:
          current_directory.pop()
          continue
        elif "$ cd" in line:
          current_directory.append("dir " + line.split()[2])
          continue
        elif "$" not in line:
          if "dir" in line:
            item = Directory(line.strip())
          else:
            item = File(line)
          computer.add_files(current_directory, item)

    return computer


class Directory(object):
  name: str
  size: int
  contents: {}

  def __init__(self, name):
    self.name = name
    self.contents = {}
    self.size = 0

  def calculate_size(self):
    for key in self.contents.keys():
      if "dir" in key:
        self.size += self.contents[key].calculate_size()
      else:
        self.size += self.contents[key].get_size()
    return self.size

  def get_size(self):
    return self.size

  def add_files(self, directory_path, new_file):
    if not directory_path:
      self.contents[new_file.name] = new_file
    else:
      self.contents[directory_path[0]].add_files(directory_path[1:], new_file)

  def sum_all_subdirectories_under_limit(self, limit):
    sum_directories = 0

    for key in self.contents.keys():
      if "dir" in key:
        if self.contents[key].get_size() <= limit:
          sum_directories += self.contents[key].get_size()
        sum_directories += self.contents[key].sum_all_subdirectories_under_limit(limit)

    return sum_directories


class File(object):
  name: str
  size: int

  def __init__(self, file_info):
    info = file_info.split()
    self.size = int(info[0])
    self.name = info[1]

  def get_size(self):
    return self.size


if __name__ == "__main__":
  Day_Six().day_six()