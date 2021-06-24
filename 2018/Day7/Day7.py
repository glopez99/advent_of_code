import copy

input = {}
first_letter = None

with open("TestInput.txt", "r") as f:
    for line in f:
        split = line.removesuffix("can begin.").removeprefix("Step").split()

        if first_letter == None:
            first_letter = split[0]

        if split[0] not in input:
            input[split[0]] = []

        input[split[0]].append(split[6])


def daySevenPartOne(input):
    order = [first_letter]
    print(order)
    next_steps = input[first_letter]
    print(next_steps)

    while len(next_steps) != 0:
        order.append(nextAlphabetical(next_steps))
        next_steps.extend(input[order[len(order) - 1]])

    print(order)


def nextAlphabetical(next_steps):
    alphabetical = copy.deepcopy(next_steps)
    print(alphabetical)

    return alphabetical[0]


if __name__ == "__main__":
    daySevenPartOne(input)
