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
    velocity = 0
    k = 0
    while k < itter:
        energy = 0
        velocity = 0
        for i in range(len(moons)):
            m1 = moons[i]
            for j in range(i + 1, len(moons)):
                m2 = moons[j]
                m1.vX += gravity(m1.x, m2.x)
                m1.vY += gravity(m1.y, m2.y)
                m1.vZ += gravity(m1.z, m2.z)
                m2.vX += gravity(m2.x, m1.x)
                m2.vY += gravity(m2.y, m1.y)
                m2.vZ += gravity(m2.z, m1.z)

            m1.x += m1.vX
            m1.y += m1.vY
            m1.z += m1.vZ
            velocity += (abs(m1.vX) + abs(m1.vY) + abs(m1.vZ))
            energy += (abs(m1.x) + abs(m1.y) + abs(m1.z)) * (abs(m1.vX) + abs(m1.vY) + abs(m1.vZ))
        if velocity == 0:
            print("itterations to the end of the universe: {}".format(k + 1))
            return
        k += 1

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
    print(compute_energy(moons, itter))


if __name__== "__main__":
    main()
