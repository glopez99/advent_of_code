import re

input = []

with open("TestInput.txt", "r") as f:
    for line in f:
        input.append(line)

    input.sort()


def part_one(input):
    guards_total_sleep = {}

    for shift in input:
        list = re.findall(r'\w+', shift)

        if len(list) == 9:
            if list[6] not in guards_total_sleep:
                guards_total_sleep[list[6]] = {}

            guards_total_sleep[list[6]]["asleep"] = 0
            guards_total_sleep[list[6]]["sleep total"] = 0
            print(guards_total_sleep[list[6]])
            continue

        if guards_total_sleep[list[6]]["asleep"] == 0:
            guards_total_sleep[list[6]]["asleep"] = int(list[4])
        else:
            wakes = int(list[4])
            guards_total_sleep[list[6]]["sleep total"] += (
                wakes - guards_total_sleep[list[6]]["asleep"])
            guards_total_sleep[list[6]]["asleep"] = None

    print(guards_total_sleep)


if __name__ == "__main__":
    part_one(input)
