parsed_list = []

with open("PuzzleInput.txt", "r") as f:
  for line in f:
    parsed_list.append("".join(line.split()))

def day_two():
  # see RFC.md for how the scores are calculated
  possible_total_score_outcomes_part_one = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2,"CZ": 6}
  possible_total_score_outcomes_part_two = {"AX": 3, "AY": 4, "AZ": 8, "BX": 1, "BY": 5, "BZ": 9, "CX": 2, "CY": 6,"CZ": 7}
  total_score_part_one = 0
  total_score_part_two = 0

  for game in parsed_list:
    total_score_part_one += possible_total_score_outcomes_part_one[game]
    total_score_part_two += possible_total_score_outcomes_part_two[game]

  print("The answer to part one is", total_score_part_one, "and the answer for part two is", total_score_part_two)

if __name__ == "__main__":
  day_two()
