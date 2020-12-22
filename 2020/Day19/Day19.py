# rule 117 is a b
# rule 54 is an a

def dayNineteen(rules, messages):
  count = 0

  for message in messages:
    splitMessage = list(message)
    if not checkValidity(rules, 0, splitMessage):
      continue

    count += 1

  print("The answer to part one is", count)

def checkValidity(rules, ruleToCheck, message):

  for i, rule in rules[ruleToCheck]:
    if rules[rule] == []:
      if not checkValidity(rules, rule, message):
        return False
      continue

    if message[i] == rules[rule]:
      continue

  return True