import copy

ingredientsLists = []
allergenMatches = {}
safeIngredients = set()

with open("input.txt") as input:
    for line in input:
        line = line.strip('\n')
        pieces = line.split(" (")
        ingredients = pieces[0].split(' ')
        for i in ingredients:
            safeIngredients.add(i)
        allergens = pieces[1][9:-1].split(", ")
        for a in allergens:
            if a not in allergenMatches:
                allergenMatches[a] = set(ingredients)
            else:
                allergenMatches[a] = allergenMatches[a] & set(ingredients)
        ingList = {}
        ingList["ing"] = ingredients
        ingList["all"] = allergens
        ingredientsLists.append(ingList)

finalAllergens = {}
totalAllergens = len(allergenMatches)
# Map allergens to ingredients
while len(finalAllergens) < totalAllergens:
    for a in list(allergenMatches.keys()):
        if len(allergenMatches[a]) == 1:
            i = allergenMatches[a].pop()
            finalAllergens[a] = i
            safeIngredients.remove(i)
            del allergenMatches[a]
        else:
            for i in list(allergenMatches[a]):
                if i in finalAllergens.values():
                    allergenMatches[a].remove(i)

print(str(finalAllergens))
#print(str(safeIngredients))

print(",".join([v for k, v in sorted(finalAllergens.items())]))

    