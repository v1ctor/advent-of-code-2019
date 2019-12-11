import sys

class Orbit:
    def __init__(self, parent, child):
        self.parent = parent
        self.child = child

    def __repr__(self):
        return "{}->{}".format(self.parent, self.child)

def indirect_orbits(orbits):
    pass

def main():
    filename = "input.txt"
    steps = False
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    orbits = []
    for s in f.readlines():
        pair = s.strip().split(")")
        orbits.append(Orbit(pair[0], pair[1]))

    print(indirect_orbits(orbits))

if __name__== "__main__":
    main()
