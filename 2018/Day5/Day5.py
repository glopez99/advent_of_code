import copy
from string import ascii_lowercase

input = list(open("PuzzleInput.txt", "r").readline())


def dayFive(input):
    print("The answer to part one is", polymerLength(input))

    shortest = len(input)
    for letter in ascii_lowercase:
        polymer_less_letter = removeLetter(input, letter)

        if polymerLength(polymer_less_letter) < shortest:
            shortest = polymerLength(polymer_less_letter)

    print("The answer to part two is ", shortest)


def polymerLength(input):
    polymer = copy.deepcopy(input)
    i = 0

    while i + 1 < len(polymer):
        if sameType(polymer[i], polymer[i + 1]) and polarization(polymer[i], polymer[i+1]):
            polymer.pop(i)
            polymer.pop(i)
            i -= 1
        else:
            i += 1

    return len(polymer)


def sameType(letter_one, letter_two):
    if letter_one.lower() == letter_two.lower():
        return True
    return False


def polarization(letter_one, letter_two):
    if letter_one.islower() and letter_two.isupper():
        return True
    elif letter_one.isupper() and letter_two.islower():
        return True
    return False


def removeLetter(input, letter):
    new_polymer = copy.deepcopy(input)
    letters = [letter, letter.upper()]

    new_polymer[:] = [i for i in new_polymer if i not in letters]

    return new_polymer


if __name__ == "__main__":
    dayFive(input)
