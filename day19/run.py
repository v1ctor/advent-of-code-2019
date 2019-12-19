import sys
from computer import Computer            


def main():
    filename = "input.txt"
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    f = open(filename)
    s = f.readline()
    memory = list(map(int, s.split(",")))

    beam = 0
    for i in range(50):
        for j in range(50):
            computer = Computer(memory)
            computer.send(i)
            computer.send(j)
            computer.run()
            if computer.receive() == 1:
                beam += 1

    print(beam)

if __name__== "__main__":
    main()
