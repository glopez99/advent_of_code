import re
from collections import Counter

input = []

with open("PuzzleInput.txt", "r") as f:
    for line in f:
        input.append(line)

    input.sort()


def day4(input):
    guards_sleep = {}
    last_guard = 0
    sleepiest_guard = 0

    for shift in input:
        shift_list = re.findall(r'\w+', shift)

        if len(shift_list) == 9:
            last_guard = shift_list[6]
            if last_guard not in guards_sleep:
                guards_sleep[last_guard] = {
                    "asleep": False,
                    "falls asleep": [],
                    "wakes": [],
                    "sleep total": 0
                }
                sleepiest_guard = shift_list[6]
            continue

        guards_sleep[last_guard] = totalSleep(
            guards_sleep[last_guard], shift_list)

        if guards_sleep[sleepiest_guard]["sleep total"] < guards_sleep[last_guard]["sleep total"]:
            sleepiest_guard = last_guard

    sleepiest_minute = findSleepiestMinute(
        guards_sleep[sleepiest_guard])

    part_two_answer = findPartTwo(guards_sleep)

    print("The answer to part one is: ",
          (int(sleepiest_guard) * sleepiest_minute[0]))

    print("The answer to part two is: ", part_two_answer)


def totalSleep(guard_record, shift):
    if guard_record["asleep"] == False:
        guard_record["falls asleep"].append(int(shift[4]))
        guard_record["asleep"] = True
    else:
        wakes = int(shift[4])
        guard_record["wakes"].append(wakes)
        last_awake = len(guard_record["falls asleep"]) - 1
        guard_record["sleep total"] += (wakes -
                                        guard_record["falls asleep"][last_awake])
        guard_record["asleep"] = False

    return guard_record


def findSleepiestMinute(guard):
    i = 0
    minutes = []

    while i < len(guard["falls asleep"]):
        min_asleep = range(guard["falls asleep"][i], guard["wakes"][i])
        minutes.extend(min_asleep)
        i += 1

    return(Counter(minutes).most_common(1)[0])


def findPartTwo(guards_schedule):
    guard = 0
    minute = 0
    counter = 0

    for key in guards_schedule:
        if guards_schedule[key]["sleep total"] == 0:
            continue

        sleepiestMinute = findSleepiestMinute(guards_schedule[key])

        if sleepiestMinute[1] > counter:
            guard = key
            minute = sleepiestMinute[0]
            counter = sleepiestMinute[1]

    return int(guard) * minute


if __name__ == "__main__":
    day4(input)
