input = {}

with open("PuzzleInput.txt", "r") as f:
    for line in f:
        split = line.removesuffix("\n").removeprefix("#").split(" ")
        bounds = split[2].removesuffix(":").split(",")
        size = split[3].split("x")
        input[split[0]] = {"top": int(bounds[1]), "bottom": int(bounds[1]) +
                           int(size[1]), "right": int(bounds[0]) + int(size[0]), "left": int(bounds[0])}


def part_one(input):
    overlap = 0

    for key1 in input:
        vertical1 = range(input[key1]["top"], input[key1]["bottom"])
        horizontal1 = range(input[key1]["left"], input[key1]["right"])
        for key2 in input:
            if key2 <= key1:
                continue
            overlap = overlap + \
                checkRanges(input[key2], vertical1, horizontal1)

    print("The answer to part one is ", overlap)


def checkRanges(rec_to_check, vertical, horizontal):
    overlap = 0
    vert_to_check = range(rec_to_check["top"], rec_to_check["bottom"])
    hort_to_check = range(rec_to_check["left"], rec_to_check["right"])

    verticalSet = set(vertical)
    horizontalSet = set(horizontal)

    vert_intersection = verticalSet.intersection(vert_to_check)
    hort_intersection = horizontalSet.intersection(hort_to_check)

    if len(vert_intersection) > 0 and len(hort_intersection) > 0:
        return overlap + len(vert_intersection) + len(hort_intersection)

    return overlap


if __name__ == "__main__":
    part_one(input)
