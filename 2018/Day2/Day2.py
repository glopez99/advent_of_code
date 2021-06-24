from Levenshtein import distance as levenshtein_distance

input = []

with open("PuzzleInput.txt", "r") as f:
    for line in f:
        no_break = line.strip("\n")
        input.append(no_break)


def day_two(input):
    two_letters = 0
    three_letters = 0
    part_two_answer = "None"

    for line in input:
        twice, thrice = count(line)
        two_letters += twice
        three_letters += thrice

        if part_two_answer == "None":
            part_two_answer = find_diff(line, input)

    print("The answer to part 1 is ", two_letters*three_letters)

    print("The answer to part two is ", part_two_answer)


def count(line):
    twice = 0
    thrice = 0
    letters = set(line)

    if len(letters) < len(line):
        for letter in letters:
            count = line.count(letter)

            if count == 2:
                twice = 1

            if count == 3:
                thrice = 1

    return twice, thrice


def find_diff(line, input):
    next_line = 1

    while next_line < len(input):

        if levenshtein_distance(line, input[next_line]) == 1:
            return line

        next_line += 1

    return "None"


if __name__ == "__main__":
    day_two(input)
