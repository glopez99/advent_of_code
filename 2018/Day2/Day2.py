input = []

with open("PuzzleInput.txt", "r") as f:
    for line in f:
        no_break = line.strip("\n")
        input.append(no_break)


def day_two_part_one(input):
    two_letters = 0
    three_letters = 0

    for line in input:
        twice = 0
        thrice = 0
        for letter in line:
            count = line.count(letter)
            if count == 2 and twice == 0:
                twice += 1
            if count == 3 and thrice == 0:
                thrice += 1
        two_letters = two_letters + twice
        three_letters = three_letters + thrice

    print("The answer to part 1 is ", two_letters*three_letters)


def day_two_part_two(input):
    next_line = 1

    for line in input:
        match_one = list(line)
        match_two = list()
        i = next_line

        while i < len(input) - 1:
            match_two = input[i]
            differing_letters = [
                letter for letter in match_one if letter not in match_two]

            if len(differing_letters) == 1:
                j = 0
                count = 0
                while j < len(line)-1:
                    if count > 1:
                        break
                    if line[j] != input[i][j]:
                        count += 1
                        j += 1
                    else:
                        j += 1
                if count == 1:
                    match_one.remove(differing_letters[0])
                    print("The answer to part 2 is ",
                          ''.join(match_one))
                    break
                i += 1
            else:
                i += 1

        next_line += 1


if __name__ == "__main__":
    day_two_part_one(input)
    day_two_part_two(input)
