recipes = []

with open("PuzzleInput.txt", "r") as f:
  for line in f:
    justRecipe = line[:line.find('(')].split()
    justAllergens = line[line.find('('):].replace("(", " ").replace(")", " ").replace(",", " ").split()[1:]
    recipe = {
      'ingredients': justRecipe,
      'allergens': justAllergens
    }
    recipes.append(recipe)

def dayTwentyOne(recipes):
  allergens = set()
  allIngredients = set()

  for recipe in recipes:
    allergens.update(recipe['allergens'])
    allIngredients.update(recipe['ingredients'])

  dangerousIngredients = set()
  ingredientAllergies = {}

  while len(ingredientAllergies.keys()) != len(allergens):
    for allergen in allergens:
      potentiallyDangerous = set()
      
      for recipe in recipes:
        if allergen in recipe['allergens']:
          if len(potentiallyDangerous) == 0:
            potentiallyDangerous.update(recipe['ingredients'])
          else:
            potentiallyDangerous = potentiallyDangerous.intersection(recipe['ingredients'])

      potentiallyDangerous = potentiallyDangerous.difference(dangerousIngredients)

      if len(potentiallyDangerous) == 1:
        dangerousIngredients.update(potentiallyDangerous)
        ingredientAllergies[allergen] = potentiallyDangerous

  nonallergenic = allIngredients.difference(dangerousIngredients)

  sortedIngredients = []

  for allergen in sorted(allergens):
    sortedIngredients.append(ingredientAllergies[allergen])
  
  print("the answer to part one is", countTimes(nonallergenic, recipes))
  print("the answer to part two is", sortedIngredients)

def countTimes(nonallergenic, recipes):
  count = 0

  for ingredient in nonallergenic:
    for recipe in recipes:
      if ingredient in recipe['ingredients']:
        count += 1
  
  return count

if __name__ == "__main__":
  dayTwentyOne(recipes)