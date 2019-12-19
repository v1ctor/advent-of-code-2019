import sys
import re
class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.vel = [0, 0, 0]
        self.energy = 0

def gravity(x, y):
    if x == y:
        return 0
    if x > y:
        return -1
    if x < y:
        return 1

def simulate_dimension(moons, dimension, itter):
    k = 0
    while k < itter:
        for i in range(len(moons)):
            m1 = moons[i]
            for j in range(i + 1, len(moons)):
                m2 = moons[j]
                m1.vel[dimension] += gravity(m1.pos[dimension], m2.pos[dimension])
                m2.vel[dimension] += gravity(m2.pos[dimension], m1.pos[dimension])

            m1.pos[dimension] += m1.vel[dimension]
        k += 1
        


def simulate(moons, itter):
    for i in range(3):
        simulate_dimension(moons, i, itter)

def compute_energy(moons):
    energy = 0
    for m in moons:
        kinetic = 0
        potential = 0
        for p in range(3):
            kinetic += abs(m.pos[p])
            potential += abs(m.vel[p])
        energy += kinetic * potential 

    return energy


def parse(lines):
    moons = []
    for line in lines:
         m = re.match("<x=([-]?[0-9]+), y=([-]?[0-9]+), z=([-]?[0-9]+)", line)
         x = int(m.group(1))
         y = int(m.group(2))
         z = int(m.group(3))
         moons.append(Moon(x, y, z))

    return moons


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    lines = f.readlines()
    moons = parse(lines)


    itter = int(input("enter number of itterations: "))
    simulate(moons, itter)
    print(compute_energy(moons))


if __name__== "__main__":
    main()
