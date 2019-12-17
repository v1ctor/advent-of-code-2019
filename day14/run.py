import sys

class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __repr__(self):
        return "{} {}".format(self.amount, self.name)

class Reaction:
    def __init__(self, ingredients, result):
        self.ingredients = ingredients
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
        reactions.append(Reaction(ingredients, result))

    return reactions



def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines()

    reactions = parse(lines)

    print(reactions)



if __name__== "__main__":
    main()
