class Day_Seven(object):
  def day_seven(self):
    computer = self.parse("PuzzleInput.txt")
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
          if line.startswith("dir "):
            item = Directory(line.strip())
          else:
            item = File(line)
          computer.add_files(current_directory, item)

    return computer


class Directory(object):
  name: str
  contents: {}

  def __init__(self, name):
    self.name = name
    self.contents = {}

  def get_size(self):
    size = 0
    for item in self.contents.values():
      size += item.get_size()
    return size

  def add_files(self, directory_path, new_file):
    if not directory_path:
      self.contents[new_file.name] = new_file
    else:
      self.contents[directory_path[0]].add_files(directory_path[1:], new_file)

  def sum_all_subdirectories_under_limit(self, limit):
    sum_directories = 0

    for item in self.contents.values():
      if item.get_size() <= limit:
        sum_directories += item.get_size()
      sum_directories += item.sum_all_subdirectories_under_limit(limit)

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

  def sum_all_subdirectories_under_limit(self, limit):
    return 0


if __name__ == "__main__":
  Day_Seven().day_seven()