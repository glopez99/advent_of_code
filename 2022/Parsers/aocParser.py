class parse(object):
  def list_of_lists_int(puzzle_input):
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

  def list_with_stripped_whitespaces(puzzle_input):
    parsed_list = []

    with open(puzzle_input, "r") as f:
      for line in f:
        parsed_list.append("".join(line.split()))

    return parsed_list
