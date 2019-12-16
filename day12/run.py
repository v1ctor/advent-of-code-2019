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
        self.energy = 0

def gravity(x, y):
    if x == y:
        return 0
    if x > y:
        return -1
    if x < y:
        return 1

def compute_energy(moons, itter):
    energy = 0
    for k in range(itter):
        energy = 0
        for m in moons:
            print("pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>".format(m.x, m.y, m.z, m.vX, m.vY, m.vZ))
        for i in range(len(moons)):
            m1 = moons[i]
            for j in range(len(moons)):
                if i != j:
                    m2 = moons[j]
                    m1.vX += gravity(m1.x, m2.x)
                    m1.vY += gravity(m1.y, m2.y)
                    m1.vZ += gravity(m1.z, m2.z)

            m1.x += m1.vX
            m1.y += m1.vY
            m1.z += m1.vZ
            energy += (m1.x + m1.y + m1.z) * (m1.vX + m1.vY + m1.vZ)
        print("")

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

    print(compute_energy(moons, 100))


if __name__== "__main__":
    main()
