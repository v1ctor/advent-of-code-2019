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

def path(root, orbits, destination):
    if root == destination:
        return [root]
    if root not in orbits:
        return []
    children = orbits[root]
    for child in children:
        p = path(child, orbits, destination)
        if len(p) != 0:
            return [root] + p
    return []

def switch_orbits(orbits):
    p1 = path("COM", orbits, "YOU")
    p2 = path("COM", orbits, "SAN")
    i = 0
    while len(p1) > i and len(p2) > i and p1[i] == p2[i]:
        i+=1
    return len(p1) + len(p2) - 2 * (i + 1) 

def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2 and sys.argv[2] == "--find-path":
        find_path = True
    f = open(filename)
    orbits = {}
    for s in f.readlines():
        pair = s.strip().split(")")
        key = pair[0]
        value = pair[1]
        if key not in orbits:
            orbits[key] = []
        orbits[key].append(value)

    if not find_path:  
        print(indirect_orbits(orbits))
    else:
        print(switch_orbits(orbits))


if __name__== "__main__":
    main()
