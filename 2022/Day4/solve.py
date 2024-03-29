def parse_input(input):
  section_assignments = []

  with open(input, "r") as f:
    for line in f:
      assignments = []
      split_line = line.split(",")

      for range in split_line:
        start, end = range.split("-")
        assignment = camp_section(int(start), int(end))
        assignments.append(assignment)

      section_assignments.append(assignments)

  return section_assignments


def part_one(camp):
  contained_sections = list(filter(check_full_containment, camp))
  print("The solution to part one is", len(contained_sections), "sections are fully contained in another.")


def part_two(camp):
  contained_sections = list(filter(check_partial_containment, camp))
  print("The solution to part two is", len(contained_sections), "sections are partially contained in another.")


def check_full_containment(sections):
  s1_start, s1_end = sections[0].start, sections[0].end
  s2_start, s2_end = sections[1].start, sections[1].end

  if s1_start <= s2_start and s2_end <= s1_end or s2_start <= s1_start and s1_end <= s2_end:
    return True

  return False


def check_partial_containment(sections):
  s1_start, s1_end = sections[0].start, sections[0].end
  s2_start, s2_end = sections[1].start, sections[1].end

  if s1_start <= s2_start <= s1_end or s2_start <= s1_start <= s2_end:
    return True

  return False


def day_four():
  camp = parse_input("PuzzleInput.txt")
  part_one(camp)
  part_two(camp)


class camp_section(object):
  start: int
  end: int

  def __init__(self, start, end):
    self.start = start
    self.end = end


if __name__ == "__main__":
  day_four()
