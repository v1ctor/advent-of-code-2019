import sys
import math

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return "{} {}".format(self.amount, self.name)

class Reaction:
    def __init__(self, ingredients, amount, result):
        self.ingredients = ingredients
        self.amount = amount
        self.result = result

    def __repr__(self):
        return "{} => {}".format(self.ingredients, self.result)

def parse_ingredient(line):
    parts = line.strip().split(" ")
    return Ingredient(parts[1].strip(), int(parts[0].strip()))


def parse(lines):
    reactions = []
    for line in lines:
        parts = line.split("=>")
        result = parse_ingredient(parts[1].strip())
        payloads = parts[0].split(",")
        ingredients = []
        for payload in payloads:
            ingredients.append(parse_ingredient(payload.strip()))
        reactions.append(Reaction(ingredients, result.amount, result))

    return reactions

def compute_resources(reactions, leftovers, target, amount, base):
    if target in leftovers and leftovers[target] > 0:
        amount -= leftovers[target]
        leftovers[target] = 0
    if target == base:
        return amount
    reaction = reactions[target]
    result = 0
    count = math.ceil(amount / reaction.amount)

    print("target {} amount {} reactions {}".format(target, amount, count))
    
    if target not in leftovers:
        leftovers[target] = 0 
    leftovers[target] += (reaction.amount * count - amount) 
    for ingredient in reaction.ingredients:
        base_ingredient = compute_resources(reactions, leftovers, ingredient.name, count * ingredient.amount, base)
        print("root: {} name: {} base: {}".format(target, ingredient.name, base_ingredient))
        result += base_ingredient
    return result


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines()

    reactions = parse(lines)

    print(reactions)


    leftovers = {}
    reactions_map = {}
    for reaction in reactions:
        reactions_map[reaction.result.name] = reaction


    print(compute_resources(reactions_map, leftovers, "FUEL", 1, "ORE"))

if __name__== "__main__":
    main()
