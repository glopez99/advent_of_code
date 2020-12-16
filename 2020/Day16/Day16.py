tickets =  []
with open("Tickets.txt", "r") as f:
  for line in f:
    line = line.replace("\n","").split(",")
    lineType = [int(number) for number in line]
    tickets.append(lineType)

rules = {}

with open("Rules.txt", 'r') as f:
  for line in f:
    splitLine = line.strip().split(":")
    splitLine[1] = splitLine[1].replace("or","-").strip().split("-")
    splitLine[1] = [int(number) for number in splitLine[1]]
    rules[splitLine[0]] = splitLine[1]

myTicket = [157,101,107,179,181,163,191,109,97,103,89,113,167,127,151,53,83,61,59,173]

def daySixteen(rules, tickets, myTicket):
  errorRateNumbers = []
  numbersByLocation = {}

  for ticket in tickets:
    invalidNumbers = checkValidity(rules, ticket)
    if invalidNumbers == 0:
      # creates a new object that organizes the numbers by location vs by ticket
      for i, number in enumerate(ticket):
        if not i in numbersByLocation.keys():
          numbersByLocation[i] = []
        numbersByLocation[i].append(number)
    else: 
      errorRateNumbers.extend(invalidNumbers)

  possibleFields = {}
  takenFields = []

  while len(takenFields) < len(rules.keys()): 
    # simple while loop to keep iterating until every thing has one field
    for key in numbersByLocation:
      # going position (i.e. place in the ticket) and leaving out fields already taken
      # this narrows down the possible fields each number matches the rules
      fields = checkForFields(rules, numbersByLocation[key], takenFields)
      if len(fields) == 0:
        pass
      elif len(fields) == 1:
        takenFields.extend(fields)
        possibleFields[key] = fields
      else:
        possibleFields[key] = fields

  print("The answer to part one is", sum(errorRateNumbers))
  print("The answer to part two is", partTwoAnswer(possibleFields, myTicket) )

def checkValidity(rules, ticket):
  # returns the invalid numbers based on the rules
  invalidNumbers = []
  for number in ticket:
    if rules['departure location'][0] <= number <= rules['departure location'][1] or rules['departure location'][2] <= number <= rules['departure location'][3]:
      continue

    if rules['departure station'][0] <= number <= rules['departure station'][1] or rules['departure station'][2] <= number <= rules['departure station'][3]:
      continue

    if rules['departure platform'][0] <= number <= rules['departure platform'][1] or rules['departure platform'][2] <= number <= rules['departure platform'][3]:
      continue

    if rules['departure track'][0] <= number <= rules['departure track'][1] or rules['departure track'][2] <= number <= rules['departure track'][3]:
      continue

    if rules['departure date'][0] <= number <= rules['departure date'][1] or rules['departure date'][2] <= number <= rules['departure date'][3]:
      continue

    if rules['departure time'][0] <= number <= rules['departure time'][1] or rules['departure time'][2] <= number <= rules['departure time'][3]:
      continue

    if rules['arrival location'][0] <= number <= rules['arrival location'][1] or rules['arrival location'][2] <= number <= rules['arrival location'][3]:
      continue

    if rules['arrival station'][0] <= number <= rules['arrival station'][1] or rules['arrival station'][2] <= number <= rules['arrival station'][3]:
      continue

    if rules['arrival platform'][0] <= number <= rules['arrival platform'][1] or rules['arrival platform'][2] <= number <= rules['arrival platform'][3]:
      continue

    if rules['arrival track'][0] <= number <= rules['arrival track'][1] or rules['arrival track'][2] <= number <= rules['arrival track'][3]:
      continue

    if rules['class'][0] <= number <= rules['class'][1] or rules['class'][2] <= number <= rules['class'][3]:
      continue

    if rules['duration'][0] <= number <= rules['duration'][1] or rules['duration'][2] <= number <= rules['duration'][3]:
      continue

    if rules['price'][0] <= number <= rules['price'][1] or rules['price'][2] <= number <= rules['price'][3]:
      continue

    if rules['route'][0] <= number <= rules['route'][1] or rules['route'][2] <= number <= rules['route'][3]:
      continue

    if rules['row'][0] <= number <= rules['row'][1] or rules['row'][2] <= number <= rules['row'][3]:
      continue

    if rules['seat'][0] <= number <= rules['seat'][1] or rules['seat'][2] <= number <= rules['seat'][3]:
      continue

    if rules['train'][0] <= number <= rules['train'][1] or rules['train'][2] <= number <= rules['train'][3]:
      continue

    if rules['type'][0] <= number <= rules['type'][1] or rules['type'][2] <= number <= rules['type'][3]:
      continue

    if rules['wagon'][0] <= number <= rules['wagon'][1] or rules['wagon'][2] <= number <= rules['wagon'][3]:
      continue

    if rules['zone'][0] <= number <= rules['zone'][1] or rules['zone'][2] <= number <= rules['zone'][3]:
      continue

    invalidNumbers.append(number)
  
  if len(invalidNumbers) == 0:
    return 0
  else:
    return invalidNumbers

def checkForFields(rules, numbers, takenFields):
  # passing in fields that have already been taken, this iterates through each number and updates
  # only the valid fields. It then returns the valid fields for that key
  invalidFields = takenFields.copy()
  possibleFields = rules.keys()
  fields = []

  for number in numbers:
    if not (rules['departure location'][0] <= number <= rules['departure location'][1]) and not (rules['departure location'][2] <= number <= rules['departure location'][3]):
      invalidFields.append('departure location')

    if not (rules['departure station'][0] <= number <= rules['departure station'][1]) and not (rules['departure station'][2] <= number <= rules['departure station'][3]):
      invalidFields.append('departure station')

    if not (rules['departure platform'][0] <= number <= rules['departure platform'][1]) and not (rules['departure platform'][2] <= number <= rules['departure platform'][3]):
      invalidFields.append('departure platform')

    if not (rules['departure track'][0] <= number <= rules['departure track'][1]) and not (rules['departure track'][2] <= number <= rules['departure track'][3]):
      invalidFields.append('departure track')

    if not (rules['departure date'][0] <= number <= rules['departure date'][1]) and not (rules['departure date'][2] <= number <= rules['departure date'][3]):
      invalidFields.append('departure date')

    if not (rules['departure time'][0] <= number <= rules['departure time'][1]) and not (rules['departure time'][2] <= number <= rules['departure time'][3]):
      invalidFields.append('departure time')

    if not (rules['arrival location'][0] <= number <= rules['arrival location'][1]) and not (rules['arrival location'][2] <= number <= rules['arrival location'][3]):
      invalidFields.append('arrival location')

    if not (rules['arrival station'][0] <= number <= rules['arrival station'][1]) and not (rules['arrival station'][2] <= number <= rules['arrival station'][3]):
      invalidFields.append('arrival station')

    if not (rules['arrival platform'][0] <= number <= rules['arrival platform'][1]) and not (rules['arrival platform'][2] <= number <= rules['arrival platform'][3]):
      invalidFields.append('arrival platform')

    if not (rules['arrival track'][0] <= number <= rules['arrival track'][1]) and not (rules['arrival track'][2] <= number <= rules['arrival track'][3]):
      invalidFields.append('arrival track')

    if not (rules['class'][0] <= number <= rules['class'][1]) and not (rules['class'][2] <= number <= rules['class'][3]):
      invalidFields.append('class')

    if not (rules['duration'][0] <= number <= rules['duration'][1]) and not (rules['duration'][2] <= number <= rules['duration'][3]):
      invalidFields.append('duration')

    if not (rules['price'][0] <= number <= rules['price'][1]) and not (rules['price'][2] <= number <= rules['price'][3]):
      invalidFields.append('price')

    if not (rules['route'][0] <= number <= rules['route'][1]) and not (rules['route'][2] <= number <= rules['route'][3]):
      invalidFields.append('route')

    if not (rules['row'][0] <= number <= rules['row'][1]) and not (rules['row'][2] <= number <= rules['row'][3]):
      invalidFields.append('row')

    if not (rules['seat'][0] <= number <= rules['seat'][1]) and not (rules['seat'][2] <= number <= rules['seat'][3]):
      invalidFields.append('seat')

    if not (rules['train'][0] <= number <= rules['train'][1]) and not (rules['train'][2] <= number <= rules['train'][3]):
      invalidFields.append('train')

    if not (rules['type'][0] <= number <= rules['type'][1]) and not (rules['type'][2] <= number <= rules['type'][3]):
      invalidFields.append('type')

    if not (rules['wagon'][0] <= number <= rules['wagon'][1]) and not (rules['wagon'][2] <= number <= rules['wagon'][3]):
      invalidFields.append('wagon')

    if not (rules['zone'][0] <= number <= rules['zone'][1]) and not (rules['zone'][2] <= number <= rules['zone'][3]):
      invalidFields.append('zone')

  for field in possibleFields:
    if field not in invalidFields:
      fields.append(field)

  return fields

def partTwoAnswer(fieldLocation, ticket):
  # then it finds the keys that have the `departure` field as a value
  # and multiplies them up
  total = 1

  for key in fieldLocation:
    if fieldLocation[key][0].startswith('departure'):
      total = total * ticket[key]
  
  return total

if __name__ == "__main__":
    daySixteen(rules, tickets, myTicket)
