import re
from collections import Counter

input = []

with open("PuzzleInput.txt", "r") as f:
    for line in f:
        input.append(line)
    input.sort()


def day4(input):
    guards_schedule = create_guard_schedule(input)

    print("The answer to part one is ", strategy_one(guards_schedule))
    print("The answer to part two is ", strategy_two(guards_schedule))


def create_guard_schedule(input):
    guards_schedule = {}
    last_guard = 0

    for shift in input:
        matches = re.match(r'\[[\d-]+ \d+:(\d+)\] ((.*#(\d+).*)|(.*))', shift)
        minutes = int(matches[1])
        guard_number = matches[4]
        wake_sleep = matches[5]

        if guard_number != None:
            last_guard = guard_number
            if guard_number not in guards_schedule:
                guards_schedule[guard_number] = {
                    "falls asleep": [],
                    "wakes": [],
                    "sleep total": 0
                }
            continue
        elif wake_sleep == "falls asleep":
            guards_schedule[last_guard]["falls asleep"].append(minutes)
        else:
            guards_schedule[last_guard]["wakes"].append(minutes)
            guards_schedule[last_guard]["sleep total"] += minutes - \
                guards_schedule[last_guard]["falls asleep"][-1]

    return guards_schedule


def strategy_one(guard_schedule):
    sleepiest_guard = 0
    guard_sleep_total = 0

    for key in guard_schedule:
        if (guard_schedule[key]["sleep total"]) > guard_sleep_total:
            sleepiest_guard = key
            guard_sleep_total = guard_schedule[key]["sleep total"]

    return int(sleepiest_guard) * find_sleepiest_minute(guard_schedule[sleepiest_guard])[0]


def find_sleepiest_minute(guard):
    i = 0
    minutes = []

    while i < len(guard["falls asleep"]):
        min_asleep = range(guard["falls asleep"][i], guard["wakes"][i])
        minutes.extend(min_asleep)
        i += 1

    sleepiest_minute = Counter(minutes).most_common(1)[0]

    return sleepiest_minute


def strategy_two(guards_schedule):
    guard = 0
    minute = 0
    highest_count = 0

    for key in guards_schedule:
        if guards_schedule[key]["sleep total"] == 0:
            continue

        sleepiest_minute, sleepiest_minute_count = find_sleepiest_minute(
            guards_schedule[key])

        if sleepiest_minute_count > highest_count:
            guard = key
            minute = sleepiest_minute
            highest_count = sleepiest_minute_count

    return int(guard) * minute


if __name__ == "__main__":
    day4(input)
