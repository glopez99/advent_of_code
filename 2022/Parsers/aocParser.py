class Parse(object):
  def list_of_lists_int(self, puzzle_input):
    list_of_lists = []

    with open(puzzle_input, "r") as f:
      list_of_ints = []
      for line in f:
        if line.strip():
          list_of_lists.append(int(line))
        else:
          list_of_lists.append(list_of_ints)
          list_of_ints = []
      list_of_lists.append(list_of_ints)

    return list_of_lists

  def list_with_stripped_whitespaces(self, puzzle_input):
    parsed_list = []

    with open(puzzle_input, "r") as f:
      for line in f:
        parsed_list.append("".join(line.split()))

    return parsed_list

  def equally_split_line(self, puzzle_input):
    list_of_lists = []

    with open(puzzle_input, "r") as f:
      for line in f:
        line = "".join(line.split())
        first_half, second_half = list(line[:len(line) // 2]), \
                                  list(line[len(line) // 2:])
        list_of_lists.append([first_half, second_half])

    return list_of_lists
