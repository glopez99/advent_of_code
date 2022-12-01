rawPuzzleInput = open('logs2.txt', 'r')
formattedPuzzleInput = list(rawPuzzleInput)


def parse(logsFile):
  differences = 0
  for line in logsFile:
    ml_map, java_map = split(line)

    differences += compare(ml_map, java_map)

  return differences


def split(line):
  line_split = line.split("]")
  ml_map = turnIntoMap(line_split[0])
  java_map = turnIntoMap(line_split[1])

  return ml_map, java_map


def turnIntoMap(string_for_map):
  string_map = string_for_map.split("[")[1]
  key_value = string_map.split(",")
  new_dict = dict()

  for key_pair in key_value:
    split = key_pair.split("=")
    new_dict[split[0]] = split[1]

  return new_dict


def compare(ml_map, java_map):
  differences = 0
  for key in ml_map.keys():
    if ml_map[key] not in java_map[key]:
      if java_map[key] == '<null>':
        continue
      if key == 'upperBound':
        if round(float(ml_map[key]), 5) == round(float(java_map[key]), 5):
          continue

      differences += 1
      print("key: ", key, " ml: ", ml_map[key], " java: ", java_map[key])
      print("full map: ml: ", ml_map, " java: ", java_map)

  return differences


print(parse(formattedPuzzleInput))
