import sys

def compute_orbits(root, path, orbits):
    if root not in orbits:
        return path
    count = 0
    children = orbits[root]
    for child in children:
        count += compute_orbits(child, path + 1, orbits)
    return count + path

def indirect_orbits(orbits):
    return compute_orbits("COM", 0, orbits)


def main():
    filename = "input.txt"
    steps = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    orbits = {}
    for s in f.readlines():
        pair = s.strip().split(")")
        key = pair[0]
        value = pair[1]
        if key not in orbits:
            orbits[key] = []
        orbits[key].append(value)

    print(indirect_orbits(orbits))


if __name__== "__main__":
    main()
