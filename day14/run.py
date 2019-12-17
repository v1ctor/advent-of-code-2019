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

#    print("target {} amount {} reactions {}".format(target, amount, count))
    
    if target not in leftovers:
        leftovers[target] = 0 
    leftovers[target] += (reaction.amount * count - amount) 
    for ingredient in reaction.ingredients:
        base_ingredient = compute_resources(reactions, leftovers, ingredient.name, count * ingredient.amount, base)
#       print("root: {} name: {} base: {}".format(target, ingredient.name, base_ingredient))
        result += base_ingredient
    return result


def binary_search(start, end, target, reactions):
    if start == end:
        return start
    mid = (start + end) // 2
    resources = compute_resources(reactions, {}, "FUEL", mid, "ORE")
    if resources < target:
        return binary_search(mid + 1, end, target, reactions)
    elif resources > target:
        return binary_search(start, mid - 1, target, reactions)
    else:
        return mid



def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines()

    reactions = parse(lines)

    print(reactions)


    reactions_map = {}
    for reaction in reactions:
        reactions_map[reaction.result.name] = reaction



    print(compute_resources(reactions_map, {}, "FUEL", 1, "ORE")) 
    print(compute_resources(reactions_map, {}, "FUEL", 5000000, "ORE"))
    print(compute_resources(reactions_map, {}, "FUEL", 2595245, "ORE"))
   
    print(binary_search(1, 5000000, 1000000000000, reactions_map))


if __name__== "__main__":
    main()
