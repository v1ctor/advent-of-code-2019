import sys
import re
class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vX = 0
        self.vY = 0
        self.vZ = 0
        self.gX = 0
        self.gY = 0
        selg.gZ = 0

def compute_energy(moons):
    return 0


def parse(lines):
    moons = []
    for line in lines:


    return moons


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines()
    moons = parse(lines)

    print(compute_energy(moons))


if __name__== "__main__":
    main()
