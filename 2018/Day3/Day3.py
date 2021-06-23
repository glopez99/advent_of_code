import numpy

input = {}

with open("PuzzleInput.txt", "r") as f:
    for line in f:
        split = line.removesuffix("\n").removeprefix("#").split(" ")
        bounds = split[2].removesuffix(":").split(",")
        size = split[3].split("x")
        input[split[0]] = {"top": int(bounds[1]), "bottom": int(bounds[1]) +
                           int(size[1]), "right": int(bounds[0]) + int(size[0]), "left": int(bounds[0])}


def part_one(input):
    part_two_answer = "None"
    fabric = numpy.zeros((1000, 1000))

    for claim in input:
        fabric[input[claim]["left"]:input[claim]["right"],
               input[claim]["top"]:input[claim]["bottom"]] += 1

    for claim in input:
        if fabric[input[claim]["left"]:input[claim]["right"],
                  input[claim]["top"]:input[claim]["bottom"]].max() == 1:
            part_two_answer = claim

    part_one_answer = numpy.size(numpy.where(fabric >= 2)[0])

    print("The answer to part one is ", part_one_answer,
          " and the answer to part two is ", part_two_answer)


if __name__ == "__main__":
    part_one(input)
