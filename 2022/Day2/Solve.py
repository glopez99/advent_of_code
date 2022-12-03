parsed_list = []

with open("PuzzleInput.txt", "r") as f:
  for line in f:
    parsed_list.append("".join(line.split()))

def day_two():
  possible_total_score_outcomes = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2,"CZ": 6}
  total_score = 0

  for game in parsed_list:
    total_score += possible_total_score_outcomes[game]

  print("The answer to part one is", total_score)

if __name__ == "__main__":
  day_two()
